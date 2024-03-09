import json
import os

ID_FILE_NAME = "id.json"


def LoadKeysFromFile(fname=ID_FILE_NAME):
  f = open(fname, 'r', encoding="UTF-8")
  return json.load(f)


def LoadKeysFromEnv():
  return {"APP_ID": os.environ["APP_ID"], "PUB_KEY": os.environ["PUB_KEY"]}


def GetDiscordKeys():
  if os.path.isfile(ID_FILE_NAME):
    return LoadKeysFromFile()
  else:
    return LoadKeysFromEnv()
