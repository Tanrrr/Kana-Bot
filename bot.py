import settings
import discord
from discord.ext import commands
from discord import app_commands
import datetime
import asyncio

MY_GUILD = discord.Object(id=683022020753096775)

class MyClient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)

client = MyClient()

@client.event
async def on_ready():
    #Wake up message
    cur_time = datetime.datetime.now().strftime("%#I:%M %p")
    guild_ammount = len(client.guilds)

    if datetime.datetime.now().hour < 10:
        print(f"Good Morning! It is currently {cur_time}, and I'm currently connected to {guild_ammount} servers!")
    elif datetime.datetime.now().hour < 17:
        print(f"Good Afternoon! It is currently {cur_time}, and I'm currently connected to {guild_ammount} servers!")
    elif datetime.datetime.now().hour < 24:
        print(f"Good Evening! It is currently {cur_time}, and I'm currently connected to {guild_ammount} servers!")  

    #Bot status
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Activity(type=discord.ActivityType.watching, name="how to game like a gamer."))

@client.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    """
    Pong!
    """
    await interaction.response.send_message("Pong!", ephemeral=True)

@client.tree.command(name="sync", guilds=[MY_GUILD], description="Owner only command to sync commands")
async def sync(interaction: discord.Interaction):
    if interaction.user.id == 226802130667831296:
        await client.tree.sync()
        await interaction.response.send_message("Synced!", ephemeral=True)
    else:
        await interaction.response.send_message("You are not the bot owner!", ephemeral=True)

client.run(settings.DISCORD_API_TOKEN)




