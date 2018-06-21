#cog example:
import discord
from discord.ext import commands
from discord.ext.commands import Bot

class ClassName():
    def __init__(self, bot):
        self.bot = bot

    #remember the 1 indent
    #see the commands.command instead of bot.command

    @commands.command(pass_context=True)
    async def repeat(self, ctx, *, text: str = None):
        #remember to import self ^
        if text != None:
            #put self before every bot. thing, like a say or send_message
            await self.bot.send_message(ctx.message.author, text)
        else:
            await self.bot.send_message(ctx.message.author, ctx.message.content)

def setup(bot):
    bot.add_cog(ClassName(bot))
