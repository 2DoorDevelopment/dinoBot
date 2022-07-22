import os
import discord
import config

from discord.ext import commands


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = ".", case_insensitive = True, intents = discord.Intents.all())

        # - Database
        self.database = config.connection["dinoBot"]
        self.accounts = self.database["accounts"]

    async def on_ready(self):
        print(f"- {self.user} has successfully started, and is connected to {len(self.guilds)} servers")

    async def setup_hook(self) -> None:
        pass

    async def close(self) -> None:
        await super(Client, self).close()


client = Client()
client.run(config.token)
