from http.client import HTTPException
from typing import Annotated
from fastapi import UploadFile, File, APIRouter, Request, HTTPException
from fastapi.templating import Jinja2Templates
from docx import Document

import json

from methods.FontStyle import checking_styles_in_document
from methods.ParagraphFormat import checking_paragraphs_on_line_spacing
from methods.Margin import checking_margin_in_document

ReportPostRouter = APIRouter()
templates_report = Jinja2Templates(directory = "templates/report")

def open_base_rules(file: str) -> dict:
    """
    Функция для открытия файла с правилами
    :param file:
    :return:
    """
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        base_rules = data["base_rules"]
        return base_rules

@ReportPostRouter.post("/check_document")
async def check_document(file: Annotated[UploadFile, File()],
                         request: Request):
    try:
        document = Document(file.file)
        font_rules = open_base_rules('rules/font_rules.json')
        margin_rules = open_base_rules('rules/margin_rules.json')
        font_style_status = checking_styles_in_document(font_rules, document)
        paragraph_format_status = checking_paragraphs_on_line_spacing(font_rules, document)
        margin_format_status = checking_margin_in_document(margin_rules, document)
        result = {
            "Отчет по стилям в документе": font_style_status,
            "Отчет по абзацам (параграфам)": paragraph_format_status,
            "Отчет по полям": margin_format_status
        }
        return templates_report.TemplateResponse(
            "get_result_report.html",
            context = {"request": request,
                       "result": result}
        )
    except Exception as e:
        raise HTTPException(status_code = 404, detail = str(e))