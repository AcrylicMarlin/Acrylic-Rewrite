import discord
from discord.ext import commands
import asqlite
import os
import aiofiles
import asqlite
class Acrylic(commands.Bot):
    database:asqlite.Connection
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
                await self.database.execute(schema)
    
    async def update_database_schema(self):
        async with aiofiles.open('utils/schema.sql') as file:
            schemas = await file.read()
            for schema in schemas.split(';'):
                ...
    

    async def run(self):
        async with self, asqlite.connect(
            'data.db'
        ) as connection:
            self.database = connection
            try:
                await self.start(TOKEN)
            except KeyboardInterrupt:
                await self.close()