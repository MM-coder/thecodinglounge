import sqlite3
import discord

class LevelSystem():
    def __init__(self, bot):
        self.bot = bot
        self.conn = sqlite3.connect('users.db')
        self.conn.execute("CREATE TABLE IF NOT EXISTS Users(UserID TEXT, Xp INTERGER, Level INTERGER)")

    def create_user_not_exists(self, user_id):
        res = self.conn.execute("SELECT COUNT FROM Users WHERE UserID=?", (user_id,))
        user_count = res.fetchone()[0]
        if user_count < 1:
            print("Creating user with id: " + user_id)
            self.conn.execute("INSERT INTO Users VALUES (?, ?, ?)", (user_id, 0, 0))
        self.conn.commit()

    def get_xp(self, user_id):
        res = self.conn.execute("SELECT Xp FROM Users WHERE UserID=?", (user_id))
        user_xp = int(res.fetchone()[0])
        return user_xp

    def change_xp(self, user_id, amount: int, what: int):
        if what == 1 or what == 'add'
            xp = int(self.get_xp(user_id) + amount)
            self.conn.execute("UPDATE Users SET Xp=? WHERE UserID=?" (xp, user_id))
            self.conn.commit()
        elif what == 0 or what == 'remove' or what == 'delete':
            xp = int(self.get_xp(user_id) - amount)
            self.conn.execute("UPDATE Users SET Xp=? WHERE UserID=?" (xp, user_id))
            self.conn.commit()

    def level(self, user_id):
        res = self.conn.execute("SELECT Level FROM Users WHERE UserID=?", (message.author.id))
        user_level = res.fetchone()][0]
        res = self.get_xp(user_id)


        return user_level


    @commands.command(pass_context=True)
    async def xp(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.message.author
        await bot.say(str(self.get_xp(member)) + " Xp")

    async def on_message(message):

        self.create_user_not_exists(user_id)
        self.change_xp(message.author.id, 1, 1)
        user_level = self.level(message.author.id)

        if user_level == 0 and res < 20:
            self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (1, message.author.id))
            try:
                level = discord.utils.get(message.server.roles, name="Level 1")
                await self.bot.add_roles(message.author, level)
            except Exception:
                level = await self.bot.create_roles(message.server, name="Level 1")
                await self.bot.add_roles(message.author, level)

        elif user_level == 1 and res < 40:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (2, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 2")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 2")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 2 and res < 80:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (3, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 3")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 3")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 3 and res < 160:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (4, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 4")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 4")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 4 and res < 320:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (5, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 5")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 5")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 5 and res < 640:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (6, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 6")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 6")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 6 and res < 1280:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (7, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 7")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 7")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 7 and res < 2560:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (8, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 8")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 8")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 8 and res < 5120:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (9, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 9")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 9")
                 await self.bot.add_roles(message.author, level)

        elif user_level == 9 and res < 10240:
             self.conn.execute("UPDATE Users SET Level=? WHERE UserID=?" (10, message.author.id))
             try:
                 level = discord.utils.get(message.server.roles, name="Level 10")
                 await self.bot.add_roles(message.author, level)
             except Exception:
                 level = await self.bot.create_roles(message.server, name="Level 10")
                 await self.bot.add_roles(message.author, level)



def setup(bot):
    bot.add_cog(LevelSystem(bot))
