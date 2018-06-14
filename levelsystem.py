import sqlite3

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

    @commands.command(pass_context=True)
    async def xp(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.message.author
        await bot.say(str(self.get_xp(member)) + " Xp")

    async def on_message(message):

        self.create_user_not_exists(user_id)
        self.change_xp(message.author.id, 1, 1)



def setup(bot):
    bot.add_cog(LevelSystem(bot))
