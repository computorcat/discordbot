import discord
import os
from dotenv import load_dotenv
from modules.revelation import revelation
from modules.niv import niv
from modules.dnd import dnd
# you need a .env file i fear
load_dotenv()

# TODO
# markov feature
# !search <query> will search for a query on google and return the first result 
# evilbot should not react to command messages!
# umm the ah!!! calculator code and what ever else i add that is complex in a seperate file please
# moderation commands <--  remember to give evilbot the perms to do this
# a levelling system?? 
# i guess all those make it count as an "general purpose" bot
# also - reverse image search and music player < -- will get to this when i read more discord documentation
intents = discord.Intents.default()
intents.message_content = True
prefix = os.getenv('PREFIX')
client = discord.Client(intents=intents)
n = niv.RandomVerse()
r = revelation.Revelation()
d = dnd.Dnd()
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
        say = message.content.split(' ')[2:] # everyhing after "evilbot say" (well should be)
        say = ' '.join(say)
        if say == "":
            await message.channel.send("you didn't give me anything to say!")
        else:
            await message.channel.send(say)
        #print(say) <-- debug

    if client.user.mentioned_in(message):
        await message.channel.send('hey!')
        
    if message.content.startswith(prefix + 'help'):
        # ok thiis sucks but it does the job i think
        await message.channel.send('\n\n prefix is ``'+prefix+'``. \n\n ``'+prefix+'help`` - shows this message \n\n``'+prefix+'say <message>`` - makes the bot say whatever is in <message> \n\n ``'+prefix+'hello`` - evilbot will say hi! \n\n if you ping evilbot they will say "hey!"')
        
    if message.content.startswith(prefix + 'calc'):
        # calculate the math in the message
        await message.channel.send("still workin' on it!")
        math = message.content.split(' ')[2:]
        math = ' '.join(math)
        if math == "":
            await message.channel.send("you didn't give me anything to calculate!")
        else:
            await message.channel.send("you're asking me to calculate " + math + ", right?")
            
    # you can comment this out if you want the people say its chaotic!
    #if "evilbot" in message.content:
    #    await message.add_reaction('☣️')
    
    # random niv verse
    if message.content.startswith(prefix + 'niv'):
        verse = n.pull_verse()
        await message.channel.send(verse)
    
    if message.content.startswith(prefix + 'quran'):
        verse = n.pull_quran()
        await message.channel.send(verse)
        
    if message.content.startswith(prefix + 'bbq'):
        verse = n.rand_pull()
        await message.channel.send(verse)
       
    # random revelation (5 random words generated form a dictionary - thank you terry davis!) 
    if message.content.startswith(prefix + 'what') or message.content.startswith(prefix + 'why') or message.content.startswith(prefix + 'how'):
        question = message.content.split(' ')[2:]
        if question == []:
            await message.channel.send("you didn't ask me anything!")
        else:
            revelation = r.generate_revelation()
            await message.channel.send(revelation)
        
    if message.content.startswith(prefix + 'roll a'):
        dice = message.content.split(' ')[3:]
        print(dice)
        if dice == []:
            await message.channel.send("you didn't give me anything to roll!")
        else:
            await message.channel.send(d.diceRoll(dice[0]))
        
        
client.run(os.getenv('TOKEN'))