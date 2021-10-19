import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

import random

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
bot = commands.Bot(command_prefix="/", intents=intents)
bot.load_extension("commands")

greetings = [
    "Hola there, ",
    "Wilkkomen, ",
    "Glad to see you, ",
    "Nice to have you here, ",
]


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))


@bot.event
async def on_member_join(member):
    print("New user here")
    channel = bot.get_channel(899924394971893830)
    greeting = random.choice(greetings) + member.display_name
    await channel.send(greeting)


@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    sender = message.author.display_name
    user = payload.member.display_name
    await channel.send("{0} Reacted to {1}'s message".format(user, sender))


bot.run(os.environ.get("BOT_TOKEN"))
