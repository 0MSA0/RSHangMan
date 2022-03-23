import logging
import discord
#import logic.py
import json
from discord.ext import commands, tasks



logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log',
    encoding='utf-8',
    mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def get_config():
    with open("config.json", "r", encoding='utf-8') as f:
        config = json.load(f)
        global token
        token = config["token"]
        global prefix
        prefix = config["prefix"]
    print("Successfully loaded config.")

if __name__ == "__main__":
    get_config()
    print("I am alive!")
    