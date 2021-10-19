import discord
from discord import guild
from dotenv import load_dotenv
import os

import random

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = discord.Client(intents=intents)

greetings = [
    "Hola there, ",
    "Wilkkomen, ",
    "Glad to see you, ",
    "Nice to have you here, "
]


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    print('New user here')
    channel = client.get_channel(899924394971893830)
    greeting = random.choice(greetings) + member.display_name
    await channel.send(greeting)

client.run(os.environ.get('BOT_TOKEN'))


@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    sender = message.author.display_name
    user = payload.member.display_name
    await channel.send("{0} Reacted to {1}'s message".format(user, sender))
