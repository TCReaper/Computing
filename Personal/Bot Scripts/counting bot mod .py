#!/usr/bin/env python
import sqlite3
import os
import operator

import discord
from discord.ext import commands

##############################
# you need to set these things, set your own id here
counting_id = '254639193479708680'
counting_log_id = None
binary_id = None
fibonacci_id = None
milestone_id = None
error_log_id = None
token = 'make a bot account and put the token here'
##############################

async def binary(message):
    b = bin(int(open("numb_bin", "r").read(), 2) + 1)[2:]
    print(b)
    if message.content != b:
        await bot.delete_message(message)
        print("wrong")
        return
    open("numb_bin", "w").write(message.content)


async def fib(message):
    l = open("numb_fib", "r").read().split(" ")
    c = int(l[0]) + int(l[1])  # a+b
    print(c)
    if message.content != str(c):
        await bot.delete_message(message)
        print("wrong")
        return
    open("numb_fib", "w").write("{} {}".format(l[1], c))


real_path = os.path.dirname(os.path.realpath(__file__)) + "/"
os.chdir(real_path)

database = sqlite3.connect("stats.db")
c = database.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS edits
             (id int, num int)''')
c.execute('''CREATE TABLE IF NOT EXISTS milestones
             (id int, num int)''')
c.execute('''CREATE TABLE IF NOT EXISTS numbers
             (num int unique primary key on conflict ignore, user int, time datetime)''')

bot = commands.Bot(command_prefix=';', description='no')


@bot.command(hidden=True)
async def get_stats():
    messages = []
    limit = c.execute('SELECT num FROM numbers ORDER BY num DESC LIMIT 1').fetchone()
    if not limit:
        limit = (0,)
    async for message in bot.logs_from(discord.Object(counting_id), limit=999999999999999):
        try:
            int_message = int(message.content)
            if int_message <= limit[0]:
                break
            messages.append((int_message, message.author.id, message.timestamp))
        except ValueError:
            pass
    if not messages: return
    c.executemany('INSERT INTO numbers VALUES (?,?,?)', messages)
    database.commit()


@bot.command(pass_context=True)
async def stats(context, user=None):
    if not user:
        user = context.message.author.id
    else:
        user = ''.join([c for c in user if c in '1234567890'])
    stats = c.execute("SELECT num FROM numbers WHERE user=? ORDER BY num ASC", (user,)).fetchall()
    max_run = last_num = cur_run = max_num = 0
    for num in stats:
        if num[0] == last_num + 1:
            cur_run += 1
            if cur_run > max_run:
                max_run = cur_run
                max_num = num[0]
        else:
            cur_run = 0
        last_num = num[0]
    mile = c.execute("SELECT num FROM milestones WHERE id=?", (user,)).fetchone()
    if not mile:
        mile = (0,)
    last_num = c.execute('SELECT num FROM numbers ORDER BY num DESC LIMIT 1').fetchone()[0]
    perc = '%.2f' % round(len(stats) / last_num * 100, 2)
    await bot.say("```\nHighest streak: {} ({}-{})\nTotal counted: {}\nTotal milestones: {}\nPercentage: {}%```".format(
        max_run + 1, max_num - max_run, max_num, len(stats), mile[0], perc))


@bot.command(pass_context=True)
async def streaks(context):
    stats = c.execute("SELECT num, user FROM numbers ORDER BY num ASC").fetchall()
    streaks = {}
    cur_usr = cur_streak = 0

    for stat in stats:
        if stat[1] == cur_usr:
            cur_streak += 1
            if streaks.get(cur_usr, 4) < cur_streak:
                streaks[cur_usr] = cur_streak
        else:
            cur_usr = stat[1]
            cur_streak = 1

    sorted_streaks = sorted(streaks.items(), key=operator.itemgetter(1), reverse=True)
    reply = '```\n'
    for x in range(10):
        user = discord.utils.get(context.message.server.members, id=str(sorted_streaks[x][0]))
        if not user:
            user = await bot.get_user_info(sorted_streaks[x][0])
        if not user:
            reply += "\n{} - {}".format(sorted_streaks[x][1], "unknown user")
            continue
        reply += "\n{} - {}".format(sorted_streaks[x][1], user.name)
    await bot.say(reply + "```")


@bot.command(pass_context=True)
async def totals(context):
    stats = c.execute("SELECT num, user FROM numbers ORDER BY num ASC").fetchall()
    totals = {}
    for stat in stats:
        totals[stat[1]] = totals.get(stat[1], 0) + 1
    sorted_streaks = sorted(totals.items(), key=operator.itemgetter(1), reverse=True)
    reply = '```\n'
    for x in range(10):
        user = discord.utils.get(context.message.server.members, id=str(sorted_streaks[x][0]))
        if not user:
            user = await bot.get_user_info(sorted_streaks[x][0])
        if not user:
            reply += "\n{} - {}".format(sorted_streaks[x][1], "unknown user")
            continue
        reply += "\n{} - {}".format(sorted_streaks[x][1], user.name)
    await bot.say(reply + "```")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="prefix is ;"))


@bot.event
async def on_message(message):
    try:
        if message.channel.id != counting_id:
            await bot.process_commands(message)
            if message.channel.id == binary_id:
                await binary(message)
            elif message.channel.id == fibonacci_id:
                await fib(message)
            return
        if message.content != str(int(open("numb", "r").read()) + 1):
            await bot.delete_message(message)
            return
        open("numb", "w").write(message.content)
        open("newstats.txt", "a").write(
            "{} {} {}\n".format(message.content, len(message.server.members), message.timestamp))

        await bot.send_message(discord.Object(counting_log_id),
                               "{} - **{}**".format(message.content, message.author.name))
        c.execute("INSERT INTO numbers VALUES (?,?,?)", (message.content, message.author.id, message.timestamp))
        database.commit()

        if int(message.content) % 500 == 0:
            x = c.execute("SELECT num FROM milestones WHERE id=?", (message.author.id,)).fetchone()
            if not x:
                c.execute("INSERT INTO milestones VALUES (?, ?)", (message.author.id, 0))
            c.execute("UPDATE milestones SET num = num + 1 WHERE id = ?", (message.author.id,))
            database.commit()
            await bot.send_message(discord.Object(milestones_id),
                                   "We've hit {} boys! Thanks to {}!".format(message.content, message.author.mention))
        await bot.process_commands(message)
    except Exception as e:
        await bot.delete_message(message)
        await bot.send_message(discord.Object(error_log_id), e)
        raise


@bot.event
async def on_message_edit(before, after):
    if after.channel.id != counting_id:
        return
    await bot.delete_message(after)
    x = c.execute("SELECT num FROM edits WHERE id=?", (before.author.id,)).fetchone()
    if not x:
        c.execute("INSERT INTO edits VALUES (?, ?)", (before.author.id, 1))
        database.commit()
        await bot.send_message(before.author,
                               "Do ***NOT*** edit your messages in counting\nYou will be muted next time\n\n<3 Number "
                               "bot")
    else:
        role = [x for x in before.server.roles if x.id == '254646567359873024'][
            0]  # ok idk how to do this one. feel free to delete this whole function
        await bot.add_roles(before.author, role)
        await bot.send_message(before.author,
                               "Do ***NOT*** edit your messages in counting\n**You have meen muted for 24 hours, "
                               "you will be kicked next time**\n\n<3 Number bot")


try:
    bot.run('PUT THE TOKEN HERE')
except FileNotFoundError:
    print("token not found\nplease create a file called \"token\" in the \"extras\" folder and put the token in that")
