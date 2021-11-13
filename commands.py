from sqlite3.dbapi2 import IntegrityError
import discord
from discord.ext import commands
from discord.utils import get
import sqlite3

db = sqlite3.connect("test.db")
cursor = db.cursor()


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createRole(self, ctx, roleName):
        if get(ctx.guild.roles, name=roleName):
            await ctx.send("Role exists.")
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

    @commands.command()
    @commands.has_role("test role")
    async def names(self, ctx):
        msg = ""
        sql = "SELECT name FROM USERS"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if (any(rows)):
                msg = ", ".join(i[0] for i in rows)
                await ctx.channel.send(msg)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(Commands(bot))
