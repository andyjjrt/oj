import requests
import os
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from consants import COOKIE_FOLDER_PATH, API

def csrf():
    try:
        with open(os.path.join(COOKIE_FOLDER_PATH , "oj_cookies"), "rt") as json_in:
            reader = json.load(json_in)
        return reader["csrftoken"]
    except:
        r = requests.get("https://oj.mozix.ebg.tw/api/profile", verify=False)
        f = open(os.path.join(COOKIE_FOLDER_PATH , "oj_cookies"), "w")
        f.write('{"csrftoken": "' + r.cookies["csrftoken"] + '"}')
        f.close
        return r.cookies['csrftoken']
def fetch(methods, url, data):
    csrf_ = csrf()
    headers = {"X-csrftoken" : csrf_}
    with open(os.path.join(COOKIE_FOLDER_PATH , "oj_cookies"), "rt") as json_in:
        cookies = json.load(json_in)
    #print(cookies)
    if methods == "get":
        r = requests.get(API+url, data=data, cookies=cookies, headers=headers, verify=False)
        return r
    elif methods == "post":
        r = requests.post(API+url, data=data, cookies=cookies, headers=headers, verify=False)
        return r
    else:
        return "error"