import requests
import os
import time
from imgr import imager, resizer
from redvid import Downloader
from instabot import Bot

def igbigmoney():
    start = time.time()
    time.sleep(1)
    page = requests.get("https://www.reddit.com/r/FoodPorn/top/.json", headers={'User-agent': 'yourmother'}).json()
    page_data = page["data"]["children"]
    page_dist = page["data"]["dist"]
    path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap"
    count = 0
    while count < page_dist:
        if ((page_data[count]["data"]["is_video"] == True) and (page_data[count]["data"]["media"]["reddit_video"]["duration"] <= 60)):
            title = page_data[count]["data"]["title"]
            if (len(title) > 221):
                while (len(title) > 221):
                    title_list = title.split()
                    title_list.pop()
                    title = " ".join(title_list)
                if ('\"', "/", ":", "*", "?", '"', "<", ">", "|" in title):
                    title = title.replace('\"', '')
                    title = title.replace("/", "")
                    title = title.replace(":", "")
                    title = title.replace("*", "")
                    title = title.replace("?", "")
                    title = title.replace('"', '')
                    title = title.replace("<", "")
                    title = title.replace(">", "")
                    title = title.replace("|", "")
            title = "'" + title + "'"
            url = page_data[count]["data"]["url"]
            auth = page_data[count]["data"]["author"]
            video_title = title + ".mp4"
            video_path = "\\" + video_title
            new_path = path + video_path
            download = Downloader(max_q=True, path=path, url=url)
            download.download()
            os.rename(download.file_name(), new_path)
            print("Video Status: Downloaded")
            bot = Bot()
            bot.login(username="appetizedd", password="Ignukefoodpie1122$")
            bot.upload_video(new_path, caption=title + "\n\n📸: @" + auth + "\nFollow @appetizedd if you ♥️ great food!"+ "\nTag Someone You Would Eat This With! 👇")
            break
        elif (page_data[count]["data"]["is_video"] == False):
            title = page_data[count]["data"]["title"]
            if (len(title) > 221):
                while (len(title) > 221):
                    title_list = title.split()
                    title_list.pop()
                    title = " ".join(title_list)
                if ('\"', "/", ":", "*", "?", '"', "<", ">", "|" in title):
                    title = title.replace('\"', '')
                    title = title.replace("/", "")
                    title = title.replace(":", "")
                    title = title.replace("*", "")
                    title = title.replace("?", "")
                    title = title.replace('"', '')
                    title = title.replace("<", "")
                    title = title.replace(">", "")
                    title = title.replace("|", "")
            title = "'" + title + "'"
            url = page_data[count]["data"]["url"]
            auth = page_data[count]["data"]["author"]
            new_path = imager(url=url, file_path=path, file_name=title)
            resizer(new_path)
            print(new_path)
            bot = Bot()
            bot.login(username="appetizedd", password="Ignukefoodpie1122$")
            bot.upload_photo(new_path, caption=title + "\n\n📸: @" + auth + "\nFollow @appetizedd if you ♥️ great food!"+ "\nTag Someone You Would Eat This With! 👇")
            break
        count += 1
    end = time.time()
    print(end - start)
igbigmoney()
