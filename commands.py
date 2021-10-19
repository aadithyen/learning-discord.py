import discord
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def createRole(self, ctx, roleName):
        role = await ctx.guild.create_role(name=roleName)
        await ctx.author.add_roles(role)
        await ctx.message.delete()
        pass


def setup(bot):
    bot.add_cog(Commands(bot))
