import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
        ```
        Commands:
        %help - Displays this list
        %play (url) - Plays a song from Youtube
        %queue - Displays the queue of songs
        %skip - Skips the current song
        %clear - Stops the music and clears the queue
        %leave - Clears the queue and leaves the vc
        %pause - Pauses current song
        %resume - Resumes paused song```
        """

        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)
    
    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name="help", help = "Displays all the available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)