from sqlite3.dbapi2 import IntegrityError
import discord
from discord.ext import commands
import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createRole(self, ctx, roleName):
        role = await ctx.guild.create_role(name=roleName)
        await ctx.author.add_roles(role)
        await ctx.message.delete()

    @commands.command()
    async def register(self, ctx, name):
        sql = 'INSERT INTO USERS VALUES ("{0}")'.format(name)
        try:
            cursor.execute(sql)
        except IntegrityError:
            await ctx.channel.send("{0} is already registered".format(name))
        db.commit()
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Commands(bot))
