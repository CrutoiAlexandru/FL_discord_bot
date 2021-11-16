import discord
import config as config
import discord_bot.on_message as on_message

def connect():
    client = discord.Client()
    
    on_message.on_message(client)
    
    client.run(config.TOKEN)