import json
import os


def LoadKeys(fname="id.json"):
    f = open(fname, 'r', encoding="UTF-8")
    return json.load(f)
