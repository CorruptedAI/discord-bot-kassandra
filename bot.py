import discord
from discord.ext import commands

from settings import load_bot_token, load_db_password, load_db_host, load_db_port

import asyncpg

INITIAL_EXTENSIONS = [
    "cogs.admin",
    "cogs.avatar",
    "cogs.baccarat",
    "cogs.balance",
    "cogs.blackjack",
    "cogs.config",
    "cogs.daily",
    "cogs.duel",
    "cogs.events",
    "cogs.flip",
    "cogs.gift",
    "cogs.help",
    "cogs.info",
    "cogs.leaderboard",
    "cogs.m8b",
    "cogs.mafia",
    "cogs.moderation",
    "cogs.ping",
    "cogs.profile",
    "cogs.roll",
    "cogs.roulette",
    "cogs.shop",
    "cogs.slots",
    "cogs.topgg",
    "cogs.weather",
]

COMMAND_PREFIX = "&"
DESCRIPTION = "I'm just a bot"

CHIPS = "\U0001F4BF"
TICKETS = "\U0001F3AB"


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
                print(f"Failed to load extension {extension}\n{type(e).__name__}: {e}")

    async def on_ready(self):
        await self.change_presence(
            activity=discord.Activity(type=discord.ActivityType.listening, name="&help")
        )
        print(
            f"""
            Username: {self.user.name}
            ID: {self.user.id}
            -----------------------
        """
        )

    async def create_db_pool(self):
        self.pg_con = await asyncpg.create_pool(
            host=load_db_host(),
            port=load_db_port(),
            user="postgres",
            database="kassandra_economy",
            password=load_db_password(),
        )

    def run(self):
        super().run(self.token, reconnect=True)


if __name__ == "__main__":
    client = Kassandra()
    client.loop.run_until_complete(client.create_db_pool())
    client.run()
