import json
import os

ID_FILE_NAME = "id.json"
CID_FILE_NAME = "cid.json"


def _LoadKeysFromFile(fname=ID_FILE_NAME):
    f = open(fname, 'r', encoding="UTF-8")
    return json.load(f)


def _LoadKeysFromEnv():
    return {"APP_ID": os.environ["APP_ID"], "PUB_KEY": os.environ["PUB_KEY"], "TOKEN": os.environ["TOKEN"]}


def _LoadChannelIDFromFile(fname="cid.json"):
    f = open(fname, 'r', encoding="UTF-8")
    return json.load(f)


def GetDiscordKeys():
    if os.path.isfile(ID_FILE_NAME):
        return _LoadKeysFromFile()
    else:
        return _LoadKeysFromEnv()


def GetDiscordChannelID():
    if os.path.isfile(CID_FILE_NAME):
        return _LoadChannelIDFromFile()
