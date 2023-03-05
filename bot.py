import discord
import responses

async def send(message, user_message, dm):
    try:
        response = responses.respond(user_message)
        await message.author.send(response) if dm else await message.channel.send(response)

    except Exception as err:
        print(err)

def run_bot():
    TOKEN = 'MTA4MTU2MDkwNDg4MzI1MzI5OQ.GFpeet.f6gqqx8Qa4tPbo0yhZ0LQQneySjUDZJfNcDPxs'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running.')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '$':
            user_message = user_message[1:]
            await send(message, user_message, dm=True)
        else:
            await send(message, user_message, dm=False)

    client.run(TOKEN)