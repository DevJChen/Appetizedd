import requests
from redvid import Downloader
import os
from instabot import Bot
from PIL import Image
from imgr import imager
from imgr import resizer

#im = Image.open("C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap\\orangechicken.jpg")
#print(im.width)
#print(im.height)
#resized = im.resize((12, 12))
#resized.save("C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap\\orangechicken.jpg")

auth = "deez"
resizer("C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap\\lunch.jpg")
bot = Bot()
bot.login(username="appetizedd", password="Ignukefoodpie1122$")
bot.upload_photo("C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap\\lunch.jpg", caption="deez nuts" + " | creds: @" + auth)











"""def weiner():
    title = "deeznuts"
    username = "appetizedd"
    url = "https://www.reddit.com/r/PublicFreakout/comments/mpynux/arrested_kid_telling_it_like_it_is/"
    path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap"
    video_title = title + ".mp4"
    video_path = "\\" + video_title
    new_path = path + video_path
    download = Downloader(max_q=True, path=path, url=url)
    download.download()
    os.rename(download.file_name, new_path)
    bot = Bot()
    bot.login(username=username, password="Ignukefoodpie1122$")
    bot.upload_video(new_path, caption=title)
    return new_path"""






