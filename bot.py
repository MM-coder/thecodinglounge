# OwGN-Helper by BluePhoenixGame
import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix=commands.when_mentioned_or('-'))
bot.remove_command('help')

startup_extensions = ["normal", "levelsystem"]

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
async def load(extension_name: str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("Loaded {}.".format(extension_name))


@bot.command()
async def unload(extension_name: str):
    bot.unload_extension(extension_name)
    await bot.say("Unloaded {}.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load {}\n{}'.format(extension, exc))

bot.run(os.getenv('TOKEN'))
