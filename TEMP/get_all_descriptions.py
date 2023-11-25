
import os
import json
import wget
from urllib.request import urlretrieve


with open('descriptions.txt', encoding="utf-8") as f:
    Lines = f.readlines()

    
json_list = []

for id, line in enumerate(Lines):
    if id == (len(Lines)-1):
        break
    
    if not id % 2:
        # print(f"line {id}: {line.strip()}")
        # print(f"line {id+1}: {Lines[id+1].strip()}")
        json_entry = {}
        json_entry["name"] = Lines[id].replace('"',"")
        json_entry["text"] = Lines[id+1].replace('"',"")
        json_list.append(json_entry)


print(json_list)

# Serializing json
json_object = json.dumps(json_list, indent=4,ensure_ascii=False).encode('utf8')
 
# Writing to sample.json
with open("sample.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object.decode())