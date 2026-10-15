import discord
import os
import random
import asyncio
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

STATUSES = [
    "Emotional support in one keystroke. Therapy sold separately.",
    "Mr. Stark, I don't feel so good. Press F.",
    "Not all heroes wear capes. Some just type F.",
    "F = ma, where m is mourning and a is a lot.",
    "Nobody in the history of Skyrim has ever said 'F' at a funeral. I'm here to change that.",
    "It's dangerous to go alone. Take this F",
    "Your ex, your Wi-Fi, your last slice of pizza: all gone, all to press F for.",
    "I'm 100% organic, free-range, grief-fed.",
    "F is for 'friends who show up.' I'm just the bot who does.",
    "Hasn't missed a funeral since launch. Hasn't been invited to one either.",
    "F is the 6th letter and the 1st priority.",
    "I only know one letter and it's the right one.",
    "Born at a Call of Duty funeral.",
    "The most meaningful thing to come out of Advanced Warfare. Fight me.",
    "Fus Ro Dah? More like Fus Ro F.",
    "Red was not the impostor. Press F.",
    "F around and find out.",
    "Helping you pay respects is my F-unction.",
    "When life gives you lemons, press F."
]

STATUS_INTERVAL = 10

_status_task_started = False


async def rotate_status():
    await client.wait_until_ready()
    show_sentence = True
    while not client.is_closed():
        if show_sentence:
            text = random.choice(STATUSES)
        else:
            count = len(client.guilds)
            text = f"In {count} server" + ("" if count == 1 else "s")
        await client.change_presence(
            status=discord.Status.dnd,
            activity=discord.CustomActivity(name=text),
        )
        show_sentence = not show_sentence
        await asyncio.sleep(STATUS_INTERVAL)


@client.event
async def on_ready():
    global _status_task_started
    print(f"Bot is online and logged in as {client.user}")
    await client.change_presence(status=discord.Status.dnd)
    if not _status_task_started:
        _status_task_started = True
        client.loop.create_task(rotate_status())

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.strip().lower() == 'f':
        await message.channel.send(f"{message.author.mention} has paid respects")

client.run(os.getenv("HUSHHUSHTOKEN"))
