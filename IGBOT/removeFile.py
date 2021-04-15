import os
import shutil

def Remove():
    username = "appetizedd"
    path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\.vap"
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    cookie_path = "C:\\Users\\john\\PycharmProjects\\IGBOT\\config\\"
    os.unlink(cookie_path + username + ".checkpoint")
    os.unlink(cookie_path + username + "_uuid_and_cookie.json")
    print("Files Cleaned")
Remove()
