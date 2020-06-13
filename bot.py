import discord
from discord.ext import commands

from settings import load_bot_token

INITIAL_EXTENSIONS = [
    "cogs.about",
    "cogs.invite",
    "cogs.baccarat",
    "cogs.blackjack",
    "cogs.colors",
    "cogs.help",
    "cogs.moderation",
    "cogs.ping",
    "cogs.fun",
    "cogs.weather",
    "cogs.slots",
]

COMMAND_PREFIX = "&"
DESCRIPTION = "something I needed"


class Kassandra(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=COMMAND_PREFIX,
            description=DESCRIPTION,
            pm_help=None,
            help_attrs=dict(hidden=True),
            fetch_offline_members=False,
            heartbeat_timeout=150.0,
        )

        self.token = load_bot_token()

        for extension in INITIAL_EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(
                    "Failed to load extension {}\n{}: {}".format(
                        extension, type(e).__name__, e
                    )
                )

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name=COMMAND_PREFIX + "help"))
        print("\n    KASSANDRA BOT")
        print("Author: Ghosteon#2776\n")
        print("-----------------------")
        print("Username: " + self.user.name)
        print("ID: " + str(self.user.id))
        print("-----------------------")

    def run(self):
        super().run(self.token, reconnect=True)


if __name__ == "__main__":
    client = Kassandra()
    client.run()
