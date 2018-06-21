import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

startup_extensions = ['bot', 'filename']

bot = commands.Bot(command_prefix='-')
bot.remove_command('help')
async def loop():
    while True:
        await bot.change_presence(game=discord.Game(name="-help", type=2))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="The Coding Lounge", type=2))
        await asyncio.sleep(15)
        await bot.change_presence(game=discord.Game(name="prefix -> -", type=2))
        await asyncio.sleep(15)


@bot.event
async def on_ready():
    print ("Bot has Booted!")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name="mmgamerbot.com", url="https://twitch.tv/MMgamerBOT", type=1))
    await loop()

@bot.event
async def on_member_join(member: discord.Member):
    if member.server.id == '422083182167588864':
        embed = discord.Embed(title="User Joined!", description="{} Has Just Joined Us! Welcome to the Coding Lounge!".format(member.name), color=0x7289DA)
        embed.set_thumbnail(url=member.avatar_url)
        await bot.send_message(bot.get_channel('437163805512826899'), embed=embed)
    else:
        for i in member.server.channels:
            if i.name.upper() == 'Welcome':
                chl = i

        embed = discord.Embed(title="User Joined!", description="{} Has Just Joined Us! Welcome them to The Coding Lounge!".format(member.name), color=0x7289DA)
        embed.set_thumbnail(url=member.avatar_url)
        try:
            await bot.send_message(chl, embed=embed)
        except Exception as e:
            print(e)

@bot.command()
async def load(cog: str):
    try:
        bot.load_extension(cog)
    except (AttributeError, ImportError) as e:
        await bot.say("Error loading cog.")
        await bot.say("```{}```".format(str(e)))
        return
    await bot.say("Loaded {}.".format(cog))


@bot.command()
async def unload(cog: str):
    bot.unload_extension(cog)
    await bot.say("Unloaded {}.".format(cog))


if __name__ == "__main__":
    for cog in startup_extensions:
        try:
            bot.load_extension(cog)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load {}\n{}'.format(cog, exc))


bot.run(os.getenv('TOKEN'))
