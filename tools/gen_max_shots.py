import yaml
import os
import argparse
from jinja2 import Environment, FileSystemLoader
import common
from pathlib import Path



environment = Environment(loader=FileSystemLoader("."))
template = environment.get_template("max.j2")
content = template.render()
with open("out_max.log", "w", encoding="utf-8") as file:
    file.write(content)
file.close()
