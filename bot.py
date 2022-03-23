import logging
import discord
import logic
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

with open("config.json", "r", encoding='utf-8') as f:
    config = json.load(f)
    bot_token = config["token"]
    bot_prefix = config["prefix"]
    bot_description = config["description"]
print("Successfully loaded config.")
bot = commands.Bot(command_prefix=commands.when_mentioned_or(bot_prefix),
                        description=bot_description)

game = None

@bot.command(aliases=["ng"])
async def new_game(ctx):
    """
    Starts a new game.
    """
    global game
    game = logic.Board()
    print(game)
    await ctx.send("```\n" + str(game) + "```")

@bot.command()
async def guess(ctx, *args):
    """
    Guess a character, word or a sentence.
    Usage: !guess ...
    """
    output_str = "No game is running"
    if game is not None and game.status == logic.StatusType.running:
        if len(args) == 0:
            output_str = "Please guess a character or a word!"
        else:
            guess_str = ''
            for wordnr in range(len(args) - 1):
                guess_str += args[wordnr] + ' '
            guess_str += args[len(args) - 1]
            is_in_solution = logic.check_input(guess_str, game)
            if is_in_solution:
                output_str = 'Oui'
                if game.status == logic.StatusType.win:
                    output_str = "Big oui"
            else:
                output_str = 'Nö'
                if game.status == logic.StatusType.lose:
                    output_str = "Big nöö"    
    await ctx.send(output_str)


@bot.command(aliases=["sh"])
@commands.is_owner()
async def shutdown(ctx):
    """
    Shuts down the bot.
    """
    await ctx.send("Bye bye :D")
    await bot.close()
    print("Bot shutting down")
   

if __name__ == "__main__":
    print("I am alive!")
    bot.run(bot_token)
    
    