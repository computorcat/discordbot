import discord
from discord.ext import commands

TOKEN = "MTEyMTU0MzkxNTg4Mzk5MTE1MA.GJk_jW.LO6zzusEViNNls5oD1ov0GFHqRHsJaRpRF3i6I" 
# This example requires the 'message_content' intent.

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # color role giver bot. user can !color <color> to get a color role which will be given to them. the role will be named after the user, and will be changed if the user changes their name or color.
    if message.content.startswith('evilbot say hello'):
        await message.channel.send('hello')
client.run(TOKEN)
