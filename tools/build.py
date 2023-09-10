import yaml
import os
import argparse
from jinja2 import Template, Environment, FileSystemLoader

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
    # Inputs
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('--output_dir', required=False, type=str, help='Output directory', default="../release/")
    args = parser.parse_args()
    # Main
    filesDict = {
        "FACE" : "head_and_body/cialo_1_twarz.yml",
        "TATOO" : "head_and_body/cialo_2_tatuaze.yml",
        "AUGMENTICS" : "head_and_body/cialo_3_augmentacje.yml",
        "FACIAL_HAIR" : "head_and_body/cialo_4_zarost.yml",
        "HAIRSTYLE" : "head_and_body/cialo_5_wlosy.yml",
        "BOOTS" : "clothing/umundurowanie_1_obuwie.yml",
        "PANTS" : "clothing/umundurowanie_2_spodnie.yml",
        "LEG_ARMOR" : "clothing/umundurowanie_3_pancerz_na_nogi.yml",
        "SHIRT" : "clothing/umundurowanie_4_koszula.yml",
        "GLOVES" : "clothing/umundurowanie_5_rekawice.yml",
        "CHEST" : "clothing/umundurowanie_6_klatka_piersiowa.yml",
        "SHOULDERS" : "clothing/umundurowanie_7_naramiennik.yml",
        "HELMET" : "clothing/umundurowanie_8_nakrycie_glowy.yml",
        "BACKPACK" : "gear/rynsztunek_1_plecak.yml",
        "CLOAK" : "gear/rynsztunek_2_plaszcz.yml",
        "SHEATHED_WEAPON" : "gear/rynsztunek_3_bron_przy_pasie.yml",
        "SHOULDERBAG" : "gear/rynsztunek_4_podwieszka.yml",
        "WAIST" : "gear/rynsztunek_5_pas.yml",
        "NECKLACE" : "gear/rynsztunek_6_szyja.yml",
        "HEADGEAR" : "gear/rynsztunek_7_headgear.yml",
        "ADDITIONAL_HEADGEAR" : "gear/rynsztunek_8_dodatkowy_deadgear.yml",
        "MASK" : "gear/rynsztunek_9_maska.yml",
        "FIREARM" : "gear/rynsztunek_10_bron_dluga.yml",
        "PISTOL" : "gear/rynsztunek_11_bron_krotka.yml"
    }

    outputDir=args.output_dir
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    
    outputHTML = os.path.join(outputDir,"project_tempestus.html")
    outputJSON = os.path.join(outputDir,"translations","pl.json")

    build_file(outputHTML, filesDict,"sheet_row.j2","character_sheet.j2")
    build_file(outputJSON, filesDict,"translation_row.j2", "pl.j2")
    
