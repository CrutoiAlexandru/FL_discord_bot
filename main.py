import discord_bot.connect as connect
from os.path import exists

if __name__ == '__main__':
    # allways start by creating a file that retains our last torrent value
    # this way it allows us to see the repeated torrent when we start the program but not whilst it is runing 
    with open("last_torrent.txt", "w") as file:
        file.write("empty")

    # start connection to our discord server
    connect.connect()