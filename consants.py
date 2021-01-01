import os
API = "https://oj.mozix.ebg.tw/api/"

FOLDER_DIR = os.path.dirname(os.path.realpath(__file__))
HOME_DIR = os.path.expanduser('~')

COOKIE_FOLDER_PATH = os.path.join(HOME_DIR, ".cookie")
STAT_PATH = os.path.join(FOLDER_DIR, "user_statement")
