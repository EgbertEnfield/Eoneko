import discord
import random
from discord.ext import commands
from LoadKeys import GetDiscordKeys
from LoadKeys import GetDiscordChannelID

DEBUG = True

Keys = GetDiscordKeys()
Channels = GetDiscordChannelID()

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


@tree.command()
async def chooserandom(inter: discord.Integration):
    await inter.response.send_message(random.random())


def Main():
    client.run(Keys["TOKEN"])


if __name__ == "__main__":
    Main()
