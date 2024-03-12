import discord
import random
import json
import enum
from discord.ext import commands
from LoadKeys import GetDiscordKeys
from LoadKeys import GetDiscordChannelID

DEBUG = True

Keys = GetDiscordKeys()
Channels = GetDiscordChannelID()

neko = {}

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)
bot = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    await tree.sync()
    print("logged in")


@client.event
async def on_message(message: discord.Message):
    print(f"Received:\n{message.author}: {message.content}")
    if message.author == client.user:
        return
    if DEBUG:
        if message.channel.id == int(Channels["CHANNEL"]["TEST"]):
            await message.channel.send(message.content)
        else:
            return
    else:
        await message.channel.send(message.content)


@tree.command()
async def debug(inter: discord.Interaction, arg: str):
    await inter.response.send_message(f"foo {arg}", ephemeral=True)


class Leng(enum.Enum):
    Long = "long"
    Short = "short"


@tree.command()
async def debug_chooserandom(inter: discord.Integration, length: Leng = None):
    await inter.response.send_message(f"index: {str(random.randint(0, 100))}" + " " + f"length type{length.value if length is not None else ''}")


@tree.command(name="nekomovie", description="ねこ動画をランダムで投下する")
@discord.app_commands.describe(length="Short: 1分以下の短い動画のみ，Long: YouTubeなどの数分の動画")
@discord.app_commands.rename(length="length_type")
async def SelectNekoMovie(inter: discord.Interaction, length: Leng = None):
    skey = ""
    if length is None:
        keys = list(neko)
        idx = random.randint(0, len(keys) - 1)
        skey = keys[idx]
    else:
        skey = length.value

    vidx = random.randint(0, len(neko[skey]) - 1)
    await inter.response.send_message(f"{neko[skey][vidx]}")


def ReadNekochanList(fname="NekoLists.json"):
    f = open(fname, 'r', encoding="UTF-8")
    return json.load(f)


def Main():
    global neko
    neko = ReadNekochanList()
    client.run(Keys["TOKEN"])


if __name__ == "__main__":
    Main()
