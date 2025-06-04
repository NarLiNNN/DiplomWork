from docx import Document
import json

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

def checking_margin_in_document(base_rules: dict, document: Document):
    """
    Функция для проверки размеров полей в документе
    :param base_rules:
    :param document:
    :return:
    """
    margin_status = {

    }
    for i, section in enumerate(document.sections, start = 1):
        left_margin = section.left_margin.cm
        right_margin = section.right_margin.cm
        top_margin = section.top_margin.cm
        bottom_margin = section.bottom_margin.cm
        margin_status[f"Раздел: {i}"] = {
            "Левое поле": round(left_margin, 2),
            "Правое поле": round(right_margin, 2),
            "Верхнее поле": round(top_margin, 2),
            "Нижнее поле": round(bottom_margin, 2)
        }
    return margin_status



# def main(path: str):
#     document = Document(path)
#     check_result = checking_margin_in_document(open_base_rules('../rules/margin_rules.json'), document)
#     dictionary_output(check_result)
#     with open('../style_result.json', 'w', encoding='utf-8') as f:
#         json.dump(check_result, f, ensure_ascii = False, indent = 1)
#
# if __name__ == "__main__":
#     main("C:\\Users\\danil\\Desktop\\Lectures\\DiplomWork\\ВКР, текст.docx")