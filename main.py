#!/usr/bin/env python
# coding: utf-8

import steamapi
import time
import os
from dotenv import load_dotenv

load_dotenv(".env")
steam_api_key = os.getenv('STEAM_DEV_API_KEY')

if steam_api_key is None:
    raise(".env file not set up correctly")

steamapi.core.APIConnection(api_key=steam_api_key, validate_key=True)
sleep_between_calls = 3  # seconds

inputs = []
with open('steam_ids.txt') as my_file:
    for line in my_file:
        if len(line) > 10:
            inputs.append(line.replace("\n", ""))

def norm_end(string):
    if string[-1] == "/":
        string = string[:-1]
    return string


def extract_id_from_profile_url(url):
    return url.split("/")[-1]


def extract_id_from_id_url(url):
    steam_profile_name = url.split("/")[-1]
    steamid = str(steamapi.user.SteamUser(userurl=steam_profile_name).steamid)
    time.sleep(2)
    return steamid

def get_id64(inputs_norm_end):
    output = []
    for input_url in inputs_norm_end:
        print("running for",input_url)
        if (
            "://steamcommunity.com/profiles/" in
            input_url[0:len('https://steamcommunity.com/profiles/')]):
            output.append(extract_id_from_profile_url(input_url))
        else:
            output.append(extract_id_from_id_url(input_url))
    return output


inputs_norm_end = [norm_end(string) for string in inputs]
id_64s = get_id64(inputs_norm_end)

f = open("steam_ids_output.csv", "w")
f.write("URL, steamid64 \n")
for i in range(len(inputs_norm_end)):
    f.write(inputs_norm_end[i]+","+id_64s[i]+'\n')
f.close()
