import discord 

def on_message(client):
    @client.event
    async def on_ready():
        print("Logged in")

    @client.event
    async def on_message(message):
        if message.author == client.user: return 

        if message.content.startswith("ping"): await message.channel.send("pong")