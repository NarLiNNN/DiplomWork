from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates

ReportGetRouter = APIRouter()
templates_report = Jinja2Templates(directory = "templates/report")

@ReportGetRouter.get("/upload_file_form")
async def upload_file_form(request: Request):
    return templates_report.TemplateResponse(
        "upload_file_form.html",
        context = {"request": request}
    )