import yaml
import os
import argparse
from jinja2 import Environment, FileSystemLoader
import common
from pathlib import Path


def load_yml(path):
    """
    Every YAML file used should have an array ITEM_OPTIONS,
    the length of this array will be added to the yaml_text,
    which is used by the jinja template.
    """
    with open(path, "r", encoding="utf-8") as file:
        yaml_text = yaml.safe_load(file)
    ITEM_OPTIONS_LEN = len(yaml_text["ITEM_OPTIONS"])
    yaml_text["ITEM_OPTIONS_LEN"] = ITEM_OPTIONS_LEN
    return yaml_text


def load_template(path):
    """
    Loads jinja template from path
    """
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template(path)
    return template


def build_elements(filesDict, templatePath):
    elements_dict = filesDict.copy()
    template = load_template(path=templatePath)
    for key, value in filesDict.items():
        yaml_text = load_yml(path="data/" + value)
        # FIXME: Dirty hack for special skill case
        if templatePath != "translation_row.j2":
            if key == "SPECIAL_SKILL":
                template = load_template(path="skill_input.j2")

        elements_dict[key] = template.render(yaml_text)

    return elements_dict


def build_file(outputFile, filesDict, entryTemplate, fullTemplate):
    elements_dict = build_elements(filesDict, templatePath=entryTemplate)
    template = load_template(path=fullTemplate)
    content = template.render(elements_dict)
    with open(outputFile, "w", encoding="utf-8") as file:
        file.write(content)
    file.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Optional app description")
    parser.add_argument(
        "--output_dir",
        required=False,
        type=str,
        help="Output directory",
        default="../release/",
    )
    args = parser.parse_args()

    outputDir = Path(args.output_dir)
    translations_dir = outputDir / "translations"

    if not os.path.exists(translations_dir):
        os.makedirs(translations_dir)

    outputHTML = outputDir / "project_tempestus.html"
    outputJSON = translations_dir / "pl.json"

    build_file(outputHTML, common.FILES_DICT, "sheet_row.j2", "character_sheet.j2")
    build_file(outputJSON, common.FILES_DICT, "translation_row.j2", "pl.j2")
