import os

username = os.getlogin()
CHROME_PROFILE_PATH = "user-data-dir=C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Massend".format(username)
