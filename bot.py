import discord
from discord import guild
from dotenv import load_dotenv
import os

import random

load_dotenv()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



client.run(os.environ.get('BOT_TOKEN'))
