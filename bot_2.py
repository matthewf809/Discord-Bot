import datetime
import random

from discord.ext.commands import Bot
from discord import Game

# Global Variables
BOT_PREFIX = ("?", "!")
client = Bot(command_prefix=BOT_PREFIX)
start_time = datetime.datetime.now()


# Command Methods
def timedelta_str(dt):
    days = dt.days
    hours, r = divmod(dt.seconds, 3600)
    minutes, sec = divmod(r, 60)

    if minutes == 1 and sec == 1:
        return '{0} days, {1} hours, {2} minute and {3} second.'.format(days, hours, minutes, sec)
    elif minutes > 1 and sec == 1:
        return '{0} days, {1} hours, {2} minutes and {3} second.'.format(days, hours, minutes, sec)
    elif minutes == 1 and sec > 1:
        return '{0} days, {1} hours, {2} minute and {3} seconds.'.format(days, hours, minutes, sec)
    else:
        return '{0} days, {1} hours, {2} minutes and {3} seconds.'.format(days, hours, minutes, sec)


# Client Commands
@client.command(name="uptime",
                description="Lets the user know how long Krab Borg has been online.",
                brief="Uptime for Krab Borg")
async def bot_uptime():
    await client.say(timedelta_str(datetime.datetime.now() - start_time))


@client.command(name="mood",
                description="Lets the user know how Krab Borg is currently feeling.",
                brief="Krab Borg's current mood")
async def bot_status():
    bot_feelings = ['Krab Borg is feeling happy.', 'Krab Borg is feeling sad.',
                    'Krab Borg if feeling annoyed.', 'Krab Borg is feeling mad.',
                    'Krab Borg if feeling excited.', 'Krab Borg if feeling sleepy.',
                    'Krab Borg if feeling hungry.', 'Krab Borg if feeling pleased.',
                    'Krab Borg if feeling thirsty.', 'Krab Borg if feeling anxious.']
    await client.say(random.choice(bot_feelings))


@client.command(name="rules",
                description="Displays server rules",
                brief="Displays server rules.")
async def server_rules():
    await client.say("```css\n"
                     "Rules:\n"
                     "  * Moderators reserve the right to delete any post.\n"
                     "  * No spamming (including advertising).\n"
                     "  * No NSFW outside of the NSFW channels.\n"
                     "  * Please communicate using English (English Server only).\n"
                     "  * No asking to be granted roles/moderator roles.\n"
                     "  * Misuse of the bot commands will lead to a ban.\n```")


@client.command(name="invite",
                description="Gives the user a permanent invite link to the server.",
                brief = "Permanent invite link.")
async def invite_link():
    await client.say("https://discord.gg/GxYVgna")


# Client Events
@client.event
async def on_ready():
    print("{0} has logged into Discord.".format(client.user.name))
    await client.change_presence(game=Game(name="with humans"))


# Bot Runner
client.run("NDU2NjY0MTU0ODg3OTQ2MjUx.Dgd-9w.Yq_QvCHxi2wNkvImjwhTyuLPq34")
