import os
from dotenv import load_dotenv

import discord
from discord.ext import commands

INITIAL_EXTENSIONS = [
    'cogs.about',
    'cogs.bj-bc',
    'cogs.colors',
    'cogs.flip',
    'cogs.help',
    'cogs.moderation',
    'cogs.ping',
    'cogs.roll',
    'cogs.slots'
]

COMMAND_PREFIX = '&'
DESCRIPTION = 'something I needed'

def load_token():
    load_dotenv()
    return os.getenv('DISCORD_TOKEN')

class Kassandra(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=COMMAND_PREFIX, description=DESCRIPTION,
                         pm_help=None, help_attrs=dict(hidden=True),
                         fetch_offline_members=False, heartbeat_timeout=150.0)

        self.token = load_token()

        self.remove_command('help')

        for extension in INITIAL_EXTENSIONS:
            try:
                self.load_extension(extension)
            except Exception as e:
                print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    async def on_ready(self):
        print('Username: ' + self.user.name)
        print('ID: ' + str(self.user.id))
        print('-----------------------')

    def run(self):
        super().run(self.token, reconnect=True)

if __name__ == '__main__':
    client = Kassandra()
    client.run()
