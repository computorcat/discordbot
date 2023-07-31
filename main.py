import discord
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# markov feature
# !search <query> will search for a query on google and return the first result 
# This example requires the 'message_content' intent.

intents = discord.Intents.default()
intents.message_content = True
prefix = "evilbot "
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(prefix + 'hello'):
        await message.channel.send('hello')
        
    if message.content.startswith(prefix + 'say'):
        # put everything after evilbot say into a variable
        say = message.content.split(' ')[2:]
        say = ' '.join(say)
        await message.channel.send(say)
        print(say)

    if client.user.mentioned_in(message):
        await message.channel.send('hey!')
        
    if message.content.startswith(prefix + 'help'):
        await message.channel.send('\n\n prefix is ``evilbot``. \n\n ``evilbot help`` - shows this message \n\n``evilbot say <message>`` - makes the bot say whatever is in <message> \n\n ``evilbot hello`` - evilbot will say hi! \n\n if you ping evilbot they will say "hey!"')
        
    if message.content.startswith(prefix + 'calc'):
        # calculate the math in the message
        await message.channel.send("still workin' on it!")
        
    if "evilbot" in message.content:
        await message.add_reaction('☣️')
        
client.run(os.getenv('TOKEN'))