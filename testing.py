import json
from settings import get_level

with open(get_level("levels.json"), "r") as json_file:
    level_file = json.load(json_file)

    print(level_file["level_1"][0]["data"])