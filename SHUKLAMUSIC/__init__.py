# -----------------------------------------------
# 🔸 StrangerMusic Project
# 🔹 Developed & Maintained by: Shashank Shukla (https://github.com/itzshukla)
# 📅 Copyright © 2022 – All Rights Reserved
#
# 📖 License:
# This source code is open for educational and non-commercial use ONLY.
# You are required to retain this credit in all copies or substantial portions of this file.
# Commercial use, redistribution, or removal of this notice is strictly prohibited
# without prior written permission from the author.
#
# ❤️ Made with dedication and love by ItzShukla
# -----------------------------------------------
from SHUKLAMUSIC.core.bot import SHUKLA
from SHUKLAMUSIC.core.dir import dirr
from SHUKLAMUSIC.core.git import git
from SHUKLAMUSIC.core.userbot import Userbot
from SHUKLAMUSIC.misc import dbb, heroku
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SHUKLA()
userbot = Userbot()
api = SafoneAPI()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "InflexOwnerBot"  # connect music api key "Dont change it"
from flask import Flask
from threading import Thread
import os

webapp = Flask(__name__)

@webapp.route("/")
def home():
    return "Bot Is Alive"

def run():
    webapp.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()