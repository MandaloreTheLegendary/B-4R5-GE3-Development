import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
   
    if message.content.startswith('ch.help'):
        help_menu()

    if message.content.startswith('ch.in'):
        login_user = message.author
        login_user_mention = message.author.mention
        await message.channel.send(str(login_user) + ' has logged in.')
        await message.channel.send(login_user_mention + ': test to see if this creates a mention.')


async def help_menu():
   await message.channel.send('Hello organic! I am B-4R5-GE3, tasked with maintaining control of the CTR account. Please see below for a list of my functionality\n.')
   await message.channel.send('ch.in - logs user as current pilot for CTR account')

#Need to create a .env file and environment variable for token for security
client.run('ODcxOTE3OTg4NjM3NDYyNTQ4.YQiS5w.dRJ54g6dzmQY-dJcGuus984c2A0')
