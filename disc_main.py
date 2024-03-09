import discord
from LoadKeys import GetDiscordKeys


class DiscordMain(discord.Client):
    async def on_ready(self):
        print("logged in")
        return

    async def on_message(self, message):
        return


def main():
    keys = GetDiscordKeys()
    intents = discord.Intents.default()
    intents.message_content = True
    client = DiscordMain(intents=intents)
    client.run(keys["TOKEN"])
    return


if __name__ == "__main__":
    main()
