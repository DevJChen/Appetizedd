from instabot import Bot


def followerBooster():
    if (len(bot.get_user_followers("appetizedd")) < 10000):
        followers = bot.get_user_followers("foodys")
        my_follower_amount = len(bot.get_user_following("appetizedd"))
        i = my_follower_amount
        for userid in followers[my_follower_amount:]:
            username = bot.get_username_from_user_id(userid)
            print("Attempting to follow user: ", username)
            if bot.follow(username):
                i += 1
                print("Followed: ", username)
            else:
                print("Not Followed: ", username)
            if i > (i + 128):
                break

bot = Bot(filter_users=True, follow_delay=12, unfollow_delay=12, max_follows_per_day=10000, max_unfollows_per_day=10000)
bot.login(username="appetizedd", password="Ignukefoodpie1122$")
followerBooster()