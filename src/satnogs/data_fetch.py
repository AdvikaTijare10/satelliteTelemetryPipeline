import time
import os
import requests
from config.settings import SATELLITE_ID,URL,API_KEY


def get_frames_from_satNGOS():

    params = {
        "satellite": SATELLITE_ID,
        "start": "2026-06-02T00:00:00",
        "end": "2026-06-04T23:59:59",
        "format": "json"
    }

    headers = {}
    if API_KEY:
        headers["Authorization"] = f"Token {API_KEY}"

    url = URL
    
    frames=[]
    while url:

        if url == URL:
            response = requests.get(url, params=params, headers=headers)
        else:
            response = requests.get(url, headers=headers)

        print("Status:", response.status_code)

        # Handle rate limiting
        if response.status_code == 429:
            print("Rate limited. Waiting 60 seconds...")
            time.sleep(60)
            continue

        if response.status_code != 200:
            print("Request failed:", response.status_code)
            print(response.text)
            break

        data = response.json()
        

        for item in data["results"]:
            frames.append(
                {"timestamp":item["timestamp"],
                 "frame":item["frame"]}
                 )

        url = data["next"]       
        time.sleep(1)

   
    return frames
