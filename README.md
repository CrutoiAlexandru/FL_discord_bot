# Filelist discord bot
## Legal stuff
I do not condone any illegal activities.
In Romania it is illegal to share pirated software but legal to download and use.
This bot does none of those, it only requires torrent data from a website called filelist, the act of being logged in on the site is not illegal as well.

## What it does
This bot takes latest torrent names from torrents uploaded on filelist.io .
He can store a wishlist of the torrents you are looking forward to being uploaded on the site and tag you when that data is found.

## Commands:
fl.help - provides a list of the following commands

    fl.wl - create a wishlist for your favorite torrents as explained above, he does not retain the exact same name twice
    
    fl.rm - remove a torrent from the wishlist
    
    ping  - look if he is alive, if he is he will reply with pong

## How it works
The bot requires 2 files. One to store the last torrent returned to the user so he does not repeat it and another to store your personal data as a config.py file.
The config.py file requires the following parameters: TOKEN, USERNAME and PASSKEY. The TOKEN is the bot's own private token for runing in a server which will not be made public online. The USERNAME is the user's name on filelist.io and the PASSKEY is the user's passkey on filelist.io, to be noted that the passkey is not the password.

He connect's to a discord server and after he is live he automatically starts looking for the latest torrents on filelist. The torrent data is gathered by using the site's rss feed, which is simplified data about the latest torrents uploaded. 
He isolates the newest torrent title and checks it against the user's wishlist. If the torrent is inside the wishlist he tags @everyone that the torrent is found.
