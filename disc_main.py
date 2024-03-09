import discord
from LoadKeys import GetDiscordKeys
from LoadKeys import GetDiscordChannelID

DEBUG = True

Keys = GetDiscordKeys()
Channels = GetDiscordChannelID()


class DiscordMain(discord.Client):
    async def on_ready(self):
        print("logged in")

    async def on_message(self, message):
        print(f"Received:\n{message.author}: {message.content}")
        if message.author == self.user:
            return

        if DEBUG:
            if message.channel.id == int(Channels["CHANNEL"]["TEST"]):
                await message.channel.send(message.content)
            else:
                return
        else:
            await message.channel.send(message.content)


def Main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = DiscordMain(intents=intents)
    client.run(Keys["TOKEN"])


if __name__ == "__main__":
    Main()
