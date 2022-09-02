import discord
from discord.ext import commands
import asqlite
import os


class Acrylic(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.presneces = True
        super().__init__(
            command_prefix="a'",
            description="A multi-purpose bot to serve all your needs",
            intents = intents
        )

    
    async def setup_hook(self):
        self.status(discord.Status.online)
        self.activity(value=discord.Activity(name = "to your needs", type = discord.ActivityType.listening))
        with open('./utils/schema.sql') as file:
            schemas = (file.read()).split(';')
            for schema in schemas:
                print(schema)