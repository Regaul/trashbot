import discord
import time, datetime
import pytz
import re
from pytz import timezone
import data.constants as tt

# 		========================

p = 't!'
v = "1.14.4"

desc = 'a simple discord bot made by elisttm | t!help for commands'
presence = discord.Game(f'{tt.p}help | v{tt.v}')

cogs = (
	'cogmanager',
	'errors',
	'admin',
	'utilities',
	'moderation',
	'fun',
	'cats',
	'tags',
	'reactions',
)

owner_id = 216635587837296651
logs = 718646246482378782

admins = (
	owner_id,						# eli
	609059779805184001, # squidd
	530937484218204172, # peter
	217663207895072768, # fluffer
	376813566591762444, # regaul
	462354301025779733, # grumm

)
srv = {
	"rhc": 695967253900034048,
	"tmh": 379723217293803526,
	"test": 439187286278537226,
}

website = 'https://elisttm.space/trashbot'
github = 'https://github.com/elisttm/trashbot'
invite = 'https://discordapp.com/oauth2/authorize?client_id=439166087498825728&scope=bot&permissions=8'

cat_site = 'http://cat.elisttm.space:7777'
help_list = 'https://trashbot.elisttm.space/commands'
tags_list = 'https://trashbot.elisttm.space/tags'
rhcooc_list = 'https://trashbot.elisttm.space/rhcooc'

mcserver = 'mc.elisttm.space'

blacklist_pkl = 'data/pickles/blacklist.pkl'
prefixes_pkl = 'data/pickles/prefixes.pkl'
tags_pkl = 'data/pickles/tags.pkl'
rhcooc_pkl = 'data/pickles/rhcooc.pkl'

time0 = '%m/%d/%y %I:%M:%S %p'	# 01/31/20 12:34:56 PM
time1 = '%H:%M:%S'						  # 12:34:56
time2 = '%I:%M:%S %p'					  # 12:34:56 PM
time3 = '%m/%d/%y' 							# 01/31/20

start_time = time.time()

def uptime(): return str(datetime.timedelta(seconds=int(round(time.time() - start_time))))
def curtime(): return datetime.datetime.now(timezone('US/Eastern')).strftime(tt.time0)
def _t(): return datetime.datetime.now(timezone('US/Eastern')).strftime(tt.time2)

def sanitize(text: str): return text.replace('@here', '@\u200bhere').replace('@everyone', '@\u200beveryone')

ico = {
	'info' : 'https://i.imgur.com/3AccYL9.png',
	'cog'	 : 'https://i.imgur.com/6kiSbJl.png',
	'warn' : 'https://i.imgur.com/MXbitfx.png',
	'deny' : 'https://i.imgur.com/9g29yLh.png',
	'good' : 'https://i.imgur.com/54DgIma.png',
	'empty': 'https://i.imgur.com/TjsJ4Tv.png',
}
clr = {
	'red'		: 0xff0000,
	'green'	: 0x00ff00,
	'blue'	: 0x0000ff,
	'pink'	: 0xff78d3,
	'yellow': 0xbf993a,
}

rhc_restrictions = {
	'serious' : 705870681849594027,
	'reaction' : 747664614493519962,
	'image' : 714875237644108140,
	'vc' : 719987120441131048,
	'dino' : 746068022401302663,
	'poop' : 745008022773956609,
}

loaded = {}

load_ascii = "\n  ___/-\___    Online | v{}\n |---------|   {}#{} ({})\n  | | | | |  _                 _     _           _   \n  | | | | | | |_ _ __ __ _ ___| |__ | |__   ___ | |_ \n  | | | | | | __| '__/ _` / __| '_ \| '_ \ / _ \| __|\n  | | | | | | |_| | | (_| \__ \ | | | |_) | (_) | |_ \n  |_______|  \__|_|  \__,_|___/_| |_|_.__/ \___/ \__|\n"

msg_e = '⚠️ ⠀{}'