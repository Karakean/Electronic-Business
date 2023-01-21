import urllib.request
import json
import os

jf = open('data.json')
data = json.load(jf)
jf.close()

os.chdir("photo_import") #change folder to import
for idx, item in enumerate(data.values()):
    for jdx, url in enumerate(item["photos_urls"]):
        name = f"{idx+1:03}-{jdx+1:03}.jpg"
        urllib.request.urlretrieve(url, name)
