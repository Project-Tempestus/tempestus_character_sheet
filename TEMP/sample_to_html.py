
import os
import json


HTML = []
with open('hack_sample.json', encoding="utf-8") as f:
    list_of_dict = json.load(f)
f.close()

# for dict in list_of_dict:
#     
#     


    
with open('out.html', "w",encoding="utf-8") as f:
    for dict in list_of_dict:
        f.write(dict["name"])
        f.write(dict["text"])
