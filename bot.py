import discord
import responses

// sends the message input by user
async def send(message, user_message, dm):
    try:
        response = responses.respond(user_message)
        await message.author.send(response) if dm else await message.channel.send(response)

    except Exception as err:
        print(err)

def run_bot():
    // bot token here
    TOKEN = 'MTA4MTU2MDkwNDg4MzI1MzI5OQ.GFpeet.f6gqqx8Qa4tPbo0yhZ0LQQneySjUDZJfNcDPxs'
    // used to enable bot to read msgs
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        // indicates bot is running
        print(f'{client.user} is now running.')
    
    // set msg details
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        // print msg
        print(f'{username} said: "{user_message}" ({channel})')
        
        // determine if response should be public or dm
        // preceded by '$' if dm
        if user_message[0] == '$':
            user_message = user_message[1:]
            await send(message, user_message, dm=True)
        else:
            await send(message, user_message, dm=False)
    // run bot
    client.run(TOKEN)
