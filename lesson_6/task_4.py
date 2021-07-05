import json
import datetime

album_duration = 0

with open("acdc.json", "r") as file:
    acdc_dict = json.load(file)

for track in acdc_dict["album"]["tracks"]["track"]:
    album_duration += int(track["duration"])


album_duration = str(datetime.timedelta(seconds = album_duration))
print(album_duration)
