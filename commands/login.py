import json, os
from getpass import getpass
from util.fetch import fetch
from consants import COOKIE_FOLDER_PATH, STAT_PATH

def login():
    if not os.path.isdir(STAT_PATH):
        os.makedirs(STAT_PATH)
    if not os.path.isdir(COOKIE_FOLDER_PATH):
        os.makedirs(COOKIE_FOLDER_PATH)
    username = input("username: ")
    pwd = getpass("password: ")
    value = {'username': username, 'password': pwd}
    r = fetch("post", "login", value)
    status = json.loads(r.text)
    print(status["data"])
    if not status["error"]:
        f = open(os.path.join(COOKIE_FOLDER_PATH , "oj_cookies"), "w")
        f.write('{"csrftoken": "' + r.cookies["csrftoken"] + '" , "sessionid" : "' + r.cookies["sessionid"] + '"}')
        f.close