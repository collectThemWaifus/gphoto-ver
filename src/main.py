# This example requires the 'message_content' intent.
from os import environ

from commands.Roll import Roll
import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        self.bot.add_cog (Roll)

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(environ.get("APIKEY"))

