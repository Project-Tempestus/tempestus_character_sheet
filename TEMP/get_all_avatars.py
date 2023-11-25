
import os
import json
import wget
from urllib.request import urlretrieve


with open('objs.json', encoding="utf-8") as f:
    list_of_dict = json.load(f)
    for dict in list_of_dict:
        avatar_url = dict["avatar"]
        if avatar_url == "":
            continue
        filename = (avatar_url.split("/")[-1])
        id, f = filename.split("?")[-1], filename.split("?")[0]
        f = f.split(".")
        f, ext = f[0], f[-1]
        fname = "out/"+str(f)+"_"+str(id)+"."+str(ext)
        print(fname)
        if os.path.exists(fname):
            continue
        else:
            urlretrieve(avatar_url, fname)
        
        
        
    