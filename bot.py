import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

balances = {}
symbols = ["🍒", "🍋", "🍊", "⭐", "💎"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def slot(ctx):
    user_id = str(ctx.author.id)

    if user_id not in balances:
        balances[user_id] = 100

    cost = 10

    if balances[user_id] < cost:
        await ctx.send("💸 Not enough coins!")
        return

    balances[user_id] -= cost

    spin = [random.choice(symbols) for _ in range(3)]
    result = " | ".join(spin)

    if spin[0] == spin[1] == spin[2]:
        winnings = 50
        balances[user_id] += winnings
        msg = f"🎰 {result}\n🔥 JACKPOT! +{winnings}"
    elif len(set(spin)) == 2:
        winnings = 20
        balances[user_id] += winnings
        msg = f"🎰 {result}\n✨ Nice! +{winnings}"
    else:
        msg = f"🎰 {result}\n😢 You lost!"

    await ctx.send(msg)

@bot.command()
async def balance(ctx):
    user_id = str(ctx.author.id)
    bal = balances.get(user_id, 100)
    await ctx.send(f"💰 Balance: {bal}")

bot.run(TOKEN)
