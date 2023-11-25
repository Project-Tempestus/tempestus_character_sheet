import yaml
import os
import argparse
from jinja2 import Template, Environment, FileSystemLoader
import common

def load_yml(path):
    with open(path, "r", encoding="utf-8") as file:
        yaml_text = yaml.safe_load(file)
    ITEM_OPTIONS_LEN = len(yaml_text["ITEM_OPTIONS"])
    yaml_text["ITEM_OPTIONS_LEN"] = ITEM_OPTIONS_LEN
    return yaml_text


def load_template(path):
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template(path)
    return template


def render_template(template, data):
    content = template.render(data)
    return content


def build_elements(filesDict, templatePath):
    elements_dict = filesDict.copy()
    template = load_template(path=templatePath)
    for key, value in filesDict.items():
        yaml_text = load_yml(path="data/"+value)
        elements_dict[key] = render_template(template=template,data=yaml_text)
    return elements_dict


def build_file(outputFile, filesDict, entryTemplate, fullTemplate ):
    elements_dict = build_elements(filesDict, templatePath=entryTemplate)   
    template = load_template(path = fullTemplate)
    content = render_template(template=template, data=elements_dict)
    with open(outputFile, "w", encoding="utf-8") as file:
        file.write(content)
    file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('--output_dir', required=False, type=str, help='Output directory', default="../release/")
    args = parser.parse_args()

    outputDir=args.output_dir
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    outputHTML = os.path.join(outputDir,"project_tempestus.html")
    outputJSON = os.path.join(outputDir,"translations","pl.json")

    build_file(outputHTML, common.FILES_DICT, "sheet_row.j2", "character_sheet.j2")
    build_file(outputJSON, common.FILES_DICT, "translation_row.j2", "pl.j2")
    
