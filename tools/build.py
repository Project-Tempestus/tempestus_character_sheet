import yaml
import os
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

def build_html_elements():
    files_dict = {
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
    elements_dict = files_dict
    template = load_template(path="sheet_row.j2")
    for key, value in files_dict.items():
        yaml_text = load_yml(path="data/"+value)
        elements_dict[key] = render_template(template=template,data=yaml_text)
    return elements_dict

def build_html():
    elements_dict = build_html_elements()

    # Once parts are ready, modify the source HTML   
    template = load_template(path = "character_sheet.j2")
    content = render_template(template=template, data=elements_dict)
    with open("build/output.html", "w", encoding="utf-8") as file:
        file.write(content)
        
def build_translation_elements():
    files_dict = {
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
    elements_dict = files_dict
    template = load_template(path="translation_row.j2")
    for key, value in files_dict.items():
        yaml_text = load_yml(path="data/"+value)
        elements_dict[key] = render_template(template=template,data=yaml_text)
    return elements_dict

    
def build_translation():
    elements_dict = build_translation_elements()

    template = load_template(path = "pl.j2")
    content = render_template(template=template, data=elements_dict)
    with open("build/pl.json", "w", encoding="utf-8") as file:
        file.write(content)

if __name__ == "__main__":
    # Load input data
    input_dict = {
        "FACE" : "",
        "TATOO" : "",
        "AUGMENTICS" : "",
        "FACIAL_HAIR" : "",
        "HAIRSTYLE" : "",
        "BOOTS" : "",
        "PANTS" : "",
        "LEG_ARMOR" : "",
        "SHIRT" : "",
        "GLOVES" : "",
        "CHEST" : "",
        "SHOULDERS" : "",
        "HELMET" : "",
        "BACKPACK" : "",
        "CLOAK" : "",
        "SHEATHED_WEAPON" : "",
        "SHOULDERBAG" : "",
        "WAIST" : "",
        "NECKLACE" : "",
        "HEADGEAR" : "",
        "ADDITIONAL_HEADGEAR" : "",
        "MASK" : "",
        "FIREARM" : "",
        "PISTOL" : ""
    }
    
    build_html()
    build_translation()

    # yaml_text = load_yml(path="data/select.yml")
    # html_template = load_template(path="html.j2")
    # html_content = render_template(template=html_template,data=yaml_text)

    # translation_template = load_template(path="translation.j2")
    # translation_content = render_template(template=translation_template,data=yaml_text)

    # print(translation_content)

    # Assign data to final HTML structs


