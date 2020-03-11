import os
import requests
from PIL import Image

from random import randrange

valid_endings = (".jpg", ".png", ".jpeg")

def get_memes():
    limit = 50

    # Get 50-ish hot memes from r/dankmemes
    payload = {"limit": limit}
    headers = {"User-Agent": "python:meme-stealer:v0.0.2 (by /u/altarrel)"}
    r = requests.get("https://www.reddit.com/r/dankmemes/hot.json", params=payload, headers=headers)
    if r.status_code != requests.codes.ok:
        print("Something went wrong with the request.")
        print(r.status_code)
        print(r.headers)
        r.raise_for_status()
        exit()
    img_urls = []
    for post in r.json()["data"]["children"]:
        
        if "url" not in post["data"]:
            print("Missing url")
            continue
        if any(post["data"]["url"].endswith(x) for x in valid_endings):
            img_urls.append(post["data"]["url"])
            print("Added {} to img_urls".format(post["data"]["url"]))

    i = randrange(len(img_urls))
    url = img_urls[i]

    extension = url[url.rfind("."):]
    img = requests.get(url)
    path = "meme{}".format(extension)
    with open(path, "wb") as f:
        f.write(img.content)
    print ("Downloaded {}".format(url))
    
    im = Image.open('./meme{}'.format(extension))
    im.save("./meme.png")
