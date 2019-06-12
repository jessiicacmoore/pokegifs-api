from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from random import randint

import json
import os
import requests


def pokegif(request, pokemon):
        api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(pokemon)
        res = requests.get(api_url)
        body = json.loads(res.content)
        name = body["name"]
        poke_id = body["id"]
        types = body["types"]
        types_list = []
        for type in types:
                types_list.append(type['type']['name'])

        key = os.environ.get("GIPHY_KEY")
        giphy_url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating=g".format(key, pokemon)
        gif_res = requests.get(giphy_url)
        gif_body = json.loads(gif_res.content)
        random_gif_num = randint(0, len(gif_body['data']))
        gif_url = gif_body['data'][random_gif_num]['url']

        return JsonResponse({"name": name, "id": poke_id, "types": types_list, "url": gif_url})
