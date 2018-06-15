import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import random
import time
import json
import requests
import datetime
import sqlite3
from datetime import datetime

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
async def on_command_error(ctx, error):
    if isinstance(ctx, discord.ext.commands.errors.CommandNotFound):
        embed = discord.Embed(title="Error:",
                              description="Damm it! I cant find that! Try `-help`.",
                              colour=0xe73c24)
        await bot.send_message(error.message.channel, embed=embed)
    else:
        embed = discord.Embed(title="Error:",
                              description=f"{ctx}",
                              colour=0xe73c24)
        await bot.send_message(error.message.channel, embed=embed)
        raise(ctx)


@bot.event
async def on_message(message):
    report_channel = bot.get_channel(456514477550993438)
    if message.content == "<@451794345629188097>":
        await bot.send_message(message.channel, "Hey, I'm The Coding Lounges custom bot!\n \n This bot is a branch of MMgamerBOT by MMgamer#3477 for more info visit https://mmgamerbot.com all info there\n \n To get familiar with my commands type `-help`\n If you want specific info about a category do\n `-help [category]`.\n \n It is highly recommended that you join the  Coding Lounge Server server for announcements and help : https://discord.gg/tTayqZA (permanant invite)\n \n By using this bot you agree that we may store some user data such as names of users, servers and channels to aid functionality Do `-tos`for more.\n \n Coded with :heart: MMgamer#3477 and  EpicShardGamingYT#6666 ")
    if message.content == "cookie":
        await bot.send_message(message.channel, ":cookie:")
    if message.content.upper() == "CHOCOLATE CHIP COOKIE":
        await bot.send_message(message.channel, ":cookie:")
    if message.content.upper() == "DADDY":
        await bot.send_message(message.channel, "<@279714095480176642>")
    if message.content.upper().startswith('-REPORT'):
        embed = discord.Embed(title="Tile",description="Desc", color=0x7289DA)
        embed.add_field(name="Reported by", value="{}".format(message.author.mention), inline=False)
        embed.add_field(name="Reported User", value="rUser", inline=False)
        await bot.send_message(report_channel, embed=embed)
    await bot.process_commands(message)

## report_channel = bot.get_channel(456514477550993438)

@bot.command(pass_context=True)
async def report(ctx,member=None):
    if member == None:
        return await bot.say("No member listed")
    else:
        chl = bot.get_channel('456514477550993438')
        await bot.say("report sent")
        await bot.send_message(chl, "{0.mention}".format(chl))
@bot.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(description="Here's what I could find:", color=0x7289DA)
    embed.add_field(name="Name", value=ctx.message.server.name)
    embed.add_field(name="Owner", value=ctx.message.server.owner)
    embed.add_field(name="Region", value=ctx.message.server.region)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles))
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.add_field(name="Channels", value=len(ctx.message.server.channels))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def cat(ctx):
    embed=discord.Embed(title="Cat", color=0x7289DA)
    embed.set_image(url="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def dog(ctx):
    embed=discord.Embed(title="A dog as requested:", color=0x7289DA)
    embed.set_image(url="https://media.giphy.com/media/Bc3SkXz1M9mjS/giphy.gif")
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def slap(ctx):
    embed=discord.Embed(title="Slap Slap Slap", color=0x7289DA)
    embed.set_image(url="https://media.giphy.com/media/s5zXKfeXaa6ZO/giphy.gif")
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def gif(ctx):
    embed=discord.Embed(title="Random GIF:", color=0x7289DA)
    embed.set_image(url=random.choice(["https://media1.giphy.com/media/kHzsbx2ZCRfkIS5BLo/200w.gif", "https://media2.giphy.com/media/1jkYrQtUrRoI2Y9Yoa/200w.gif", "https://media0.giphy.com/media/vN3fMMSAmVwoo/200w.gif", "https://media0.giphy.com/media/WyrdDeIxGOlQA/200w.gif", "https://media2.giphy.com/media/QHE5gWI0QjqF2/giphy.gif", "https://media2.giphy.com/media/5ntdy5Ban1dIY/200w.gif"]))
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)

@bot.command
async def tos(ctx):
    embed=discord.Embed(title="TOS", description=":shield: Terms of Service\n \n On August 20th, 2017 Discord updated their Terms of Service. Bot owners must now notify their users what kind of user data they store.\nBy using this bot you agree that we may store some user data, such as** names of users, servers and channels**.", color=0x7289DA)
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def bird(ctx):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('http://random.birb.pw/tweet/') as resp:
                _url = (await resp.read()).decode("utf-8")
                url = f"http://random.birb.pw/img/{str(_url)}"
                embed = discord.Embed(color=0x000000)
                embed.description = "**Random bird image :bird:**"
                embed.set_image(url=url)
                embed.set_footer(text=f"{self.bot.user.name}")
                embed.timestamp = datetime.utcnow()
                await bot.say(embed=embed)
    except:
        await bot.say(':WrongMark: **API is unavailable now. Try again later!**')

@bot.command(pass_context=True)
async def add(ctx, a: int, b: int):
    await bot.say(a+b)


@bot.command(pass_context=True)
async def multiply(ctx, a: int, b: int):
    await bot.say(a*b)


@bot.command(pass_context=True)
async def pfp(ctx, member: discord.Member):
     embed=discord.Embed(title="The users profile picture", color=0x7289DA)
     embed.set_image(url=member.avatar_url)
     embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
     await bot.say(embed=embed)

@bot.command()
async def meme(ctx, *choices: str):
    embed = discord.Embed(colour=0x7289DA)
    embed.set_image(url=random.choice([ "https://max-media.imgix.net/transfers/2016/6/2/35493eb9ea00b43d76f504388a7d98eac01d9471.jpg?w=640&fit=max&auto=format&q=70", "https://max-media.imgix.net/transfers/2016/6/2/7b4575d386865d39cf75d5446516fa638828622e.png?w=640&fit=max&auto=format&q=70", "https://max-media.imgix.net/transfers/2016/6/2/34df8440609218f69c7466a1f19ab5aef6120596.png?w=640&fit=max&auto=format&q=70", "https://max-media.imgix.net/transfers/2016/6/2/7d41985b2e8962398df13d1272a6c258470ed53d.jpg?w=640&fit=max&auto=format&q=70", "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwi0k8_b0NPbAhWDaVAKHWdJAOkQjRx6BAgBEAU&url=https%3A%2F%2Fwww.memecenter.com%2Fsearch%2Fcheese&psig=AOvVaw3u9-NYrnxSlBDWcRFEoGYG&ust=1529081497518231"]))
    embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx, module="all"):
    module = module.lower()
    if module == "info":
                embed=discord.Embed(title="Help", description="""
                Info Commands:
                •`-ftn pc <player>` - Gets fortnite players status (pc only).
                •`-info <@mention>` - Gets some info on the server.
                •`-all_servers` - Shows all servers the bot is in.
                •`-urban <querey>` -Searches the urbandic for your query
                •`-pfp <@user>` >` - Shows a users's profile picture
                •`-all_servers` - Shows all servers the bot is in.
                """)
                await bot.say(embed=embed)
    elif module == 'all':
        embed=discord.Embed(title="All Help", description="""
        Info Commands:
        •`-ftn pc <player>` - Gets fortnite players status (pc only).
        •`-info <@mention>` - Gets some info on the server.
        •`-all_servers` - Shows all servers the bot is in.
        •`-urban <querey>` -Searches the urbandic for your query
        •`-pfp <@user>` - Shows a users's profile picture
        •`-all_servers` - Shows all servers the bot is in.
        •`-server` - Gets you info on the server.
        Fun commands:
         •`-cat` - Gets you a select cat GIF.
         •`-dog` - Gets you a cool dog GIF.
         •`-slap` - Slapy Slpay Scratchy Bitey.
         •`-add` - Adds two numbers.
         •`-multipy` - Multipys two numbers.
         •`-gif` - Random GIF from giphy.
         •`-meme` - Random Meme.
        Moderation Commands:
        •`-warn <user> <reason>` - Warns a user (Also DM's)
        •`-kick <@user>` - Kicks the user from the server
        •`-ban <@user>` - Bans a user for the server
        •`-mute <@user>` - Mutes a user
        •`-leave` - Makes the bot leave the server
        •`-checkuser <@user>` - Checks if the user is an Alt or raid account.
        Misc Commands:
        •`-ami <@>|<rolename>` - Tells you if you have that specific role in the server
        •`-tos` - Shows the bots Terms Of Service.
        """, color=0x7289DA)
        embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
        await bot.say(embed=embed)
    elif module == 'info':
            embed=discord.Embed(title="Help", description="""
            Info Commands:
            •`-ftn pc <player>` - Gets fortnite players status (pc only).
            •`-info <@mention>` - Gets some info on the server.
            •`-all_servers` - Shows all servers the bot is in.
            •`-urban <querey>` -Searches the urbandic for your query
            •`-pfp <@user>` - Shows a users's profile picture
            •`-all_servers` - Shows all servers the bot is in.
            •`-server` - Gets you info on the server.
         """, colour=0x7289DA)
            embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
            await bot.say(embed=embed)
    elif module == 'fun':
            embed=discord.Embed(title="Help", description="""
            Fun commands:
             •`-cat` - Gets you a select cat GIF.
             •`-dog` - Gets you a cool dog GIF.
             •`-slap` - Slapy Slpay Scratchy Bitey.
             •`-add` - Adds two numbers.
             •`-multipy` - Multipys two numbers.
             •`-gif` - Random GIF from giphy.
         """, colour=0x7289DA)
            embed.set_footer(icon_url="https://i.imgur.com/yB0Lig7.png", text="Custom Bot For The Coding Lounge")
            await bot.say(embed=embed)


@bot.command(pass_context=True)
async def urban(ctx, *, message):
        r = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(' '.join(message)))
        r = json.loads(r.text)
        file = open('urban.txt', 'w')
        file.write("**Definition for {}** \n\n\n {}{}".format(r['list'][0]['word'],r['list'][0]['definition'],r['list'][0]['permalink']))
        file.close()
        tmp = open('urban.txt', 'rb')
        await bot.send_file(ctx.message.channel, 'urban.txt', content=tmp)


@bot.command(pass_context=True)
async def mute(ctx, member: discord.Member, time: int, *, reason):
    if ctx.message.author.server_permissions.administrator != True:
        return await bot.say("No perms!")
    await bot.send_message(member, f"You have been muted for {time} Seconds in {ctx.message.server.name}! Be sure to read the rules again! ")
    role = discord.utils.get(ctx.message.server.roles, name="Muted")
    await bot.add_roles(member, role)
    embed = discord.Embed(title="MUTED", description="{} You have been Muted for **{}** Seconds. Reason: {}".format(member.mention, time, reason), color=0x7289DA)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
    await bot.say(embed=embed)
    await asyncio.sleep(time)
    await bot.remove_roles(member, role)
    await bot.send_message(member, f"You have been unmuted! Be careful!")
    embed = discord.Embed(title="Member unmuted", description="{} Has been Unmuted".format(member.mention), color=0x7289DA)
    embed.set_author(name=member.name, icon_url=member.avatar_url)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def ami(ctx,*, role):
    if role in [role.name for role in ctx.message.author.roles]:
        await bot.say("Yes")
    else:
        await bot.say("No")


@bot.command(pass_context=True)
async def all_servers(ctx):
    if ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="All servers", description="lists all servers the bot is in.", color=0x7289DA)
        tmp = 1
        for i in bot.servers:
            embed.add_field(name=str(tmp), value=i.name, inline=False)
            tmp += 1
        await bot.say(embed=embed)

@bot.event
async def on_server_channel_create(channel):
    await bot.send_message(channel, random.choice(['First', 'I am first and u suck', 'i seriusly dont have a life', 'Calm your fucking tits when you’re being such a bitch for jerking off']))

@bot.command(pass_context=True)
async def ping(ctx):
        t1 = time.perf_counter()
        tmp = await bot.say("pinging...")
        t2 = time.perf_counter()
        await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))
        await bot.delete_message(tmp)

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if "451804048488792106" in [role.id for role in ctx.message.author.roles]:
        await bot.ban(user)
        await bot.say(f"{user.name} Has been Banned!")

@bot.command(pass_context=True)
async def kick(ctx, user: discord.User, *, reason: str):
    if "451804048488792106" in [role.id for role in ctx.message.author.roles]:
        await bot.kick(user)
        await bot.say(f"boom, user has been kicked for reason: {reason}")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name=ctx.message.author.display_name)
        embed.add_field(name=":desktop:ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name=":satellite:Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name=":star2:Joined server::", value=ctx.message.author.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=ctx.message.author.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":bust_in_silhouette:Nickname:", value=user.display_name)
        embed.add_field(name=":robot:Is Bot:", value=user.bot)
        embed.add_field(name=':ballot_box_with_check: Top role:', value=ctx.message.author.top_role.name, inline=True)
        embed.add_field(name=':video_game: Playing:', value=ctx.message.author.game, inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await asyncio.sleep(0.3)
        await bot.say(embed=embed)
    else:
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name=ctx.message.author.display_name)
        embed.add_field(name=":desktop:ID:", value=ctx.message.author.id, inline=True)
        embed.add_field(name=":satellite:Status:", value=ctx.message.author.status, inline=True)
        embed.add_field(name=":star2:Joined server::", value=ctx.message.author.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=ctx.message.author.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":bust_in_silhouette:Nickname:", value=user.display_name)
        embed.add_field(name=":robot:Is Bot:", value=user.bot)
        embed.add_field(name=':ballot_box_with_check: Top role:', value=ctx.message.author.top_role.name, inline=True)
        embed.add_field(name=':video_game: Playing:', value=ctx.message.author.game, inline=True)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        await asyncio.sleep(0.3)
        await bot.say(embed=embed)


@bot.command(pass_context=True)
async def checkuser(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name=ctx.message.author.name ,icon_url=ctx.message.author.avatar_url)
        embed.add_field(name=":star2:Joined server:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        await bot.say (embed=embed)
    else:
        embed = discord.Embed(color=0x7289DA)
        embed.set_author(name=ctx.message.author.name , icon_url=ctx.message.author.avatar_url)
        embed.add_field(name=":star2:Joined server:", value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        embed.add_field(name=":date:Created account:", value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
        await bot.say (embed=embed)


@bot.command(pass_context=True)
async def warn(ctx, userName: discord.Member ,*, reason: str):
    if "Staff" in [role.name for role in ctx.message.author.roles] or ctx.message.author.server_permissions.administrator:
        embed = discord.Embed(title="Warned", description="{} You have been warned for **{}**".format(userName.mention, reason), color=0x7289DA)
        embed.set_thumbnail(url=userName.avatar_url)
        embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
        await bot.say(embed=embed)
        await bot.send_message(userName, "You Have Been Warned. Reason: {}".format(reason))
    else:
        await bot.say("{} :x: You are not allowed to use this command!".format(ctx.message.author.mention))


@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def delete(ctx, number):
    msgs = []
    number = int(number)
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        msgs.append(x)
    await bot.delete_messages(msgs)
    embed = discord.Embed(title=f"{number} messages deleted", description="Wow, somebody's been spamming", color=0x7289DA)
    test = await bot.say(embed=embed)
    await asyncio.sleep(10)
    await bot.delete_message(test)



@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(title="test", description="my name jeff", color=0x7289DA)
    embed.set_footer(text="this is a footer")
    embed.set_author(name="MMgamer")
    embed.add_field(name="This is a field", value="no it isn't", inline=True)
    await bot.say(embed=embed)


@bot.command(pass_context=True)
async def get_inv(ctx):
    for i in bot.servers:
        var = await bot.create_invite(i.channels[0])
        await bot.say(str(var))


@bot.command(pass_context=True)
async def ball(ctx, question):
    await bot.say(random.choice(["NO", "Ofc", "Magic dosen't have all the awnsers", "No Idea"]))


@bot.command(pass_context=True)
async def leave(ctx):
    if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '397745647723216898':
        if ctx.message.author != bot.user:
            await bot.leave_server(ctx.message.server)
        else:
            await bot.say(":x: No Perms")
    else:
        await bot.say("To low perms")


@bot.command(pass_context=True)
async def remove_all_servers(ctx):
    if ctx.message.author.id == '279714095480176642':
        tmp = bot.servers
        for server in tmp:
            await bot.leave_server(server)
        await bot.say("Operation completed")


@bot.command(pass_context=True)
async def say(ctx, *, message):
    if ctx.message.author.id == bot.user.id:
        return
    else:
        await bot.say(message)


@bot.command(pass_context=True)
async def reboot(ctx):
    if not (ctx.message.author.id == '279714095480176642' or ctx.message.author.id == '449641568182206476'):
        return await bot.say(":x: You **Must** Be Bot Owner Or Developer")
    await bot.logout()


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
            

            





bot.run(os.getenv('TOKEN'))
