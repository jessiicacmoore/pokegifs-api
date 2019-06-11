import json
import requests

import os

key = os.environ.get("GIPHY_KEY")
url = "https://api.giphy.com/v1/gifs/search?api_key={}&q=pikachu&rating=g".format(key)
gif_res = requests.get(url)
gif_body = json.loads(gif_res.content)

for key in gif_body['data'][0].keys():
    print(key)

# type
# id
# slug
# url
# bitly_gif_url
# bitly_url
# embed_url
# username
# source
# rating
# content_url
# source_tld
# source_post_url
# is_sticker
# import_datetime
# trending_datetime
# user
# images
# title
# analytics

# -----------------------------

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)

name = body["name"]
poke_id = body["id"]
poke_type = body["types"]

