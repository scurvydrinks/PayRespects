import discord
import os
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot is online and logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.strip().lower() == 'f':
        await message.channel.send(f"{message.author.mention} has paid respects")

client.run(os.getenv("HUSHHUSHTOKEN"))
