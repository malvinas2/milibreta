import os
import re

BASE_DIR2 = os.path.dirname((os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# BASE_DIR = os.path.dirname((os.path.realpath(__file__)))

SRC_DIR = os.path.join(BASE_DIR, 'src')
ICONS_DIR = os.path.join(BASE_DIR, 'icons')
PICTURES_DIR = os.path.join(BASE_DIR, 'pictures')
# DATABASE_NAME = os.path.join(SRC_DIR, 'milibreta.db')
ADD_PICTURE = os.path.join(ICONS_DIR, 'add.png')
UPDATE_PICTURE = os.path.join(ICONS_DIR, 'update.png')
DELETE_PICTURE = os.path.join(ICONS_DIR, 'delete.png')
RESET_PICTURE = os.path.join(ICONS_DIR, 'reset.png')

DATABASE_NAME = "milibreta.db"
REGEX_MAIL = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
DEFAULT_PROFILE = os.path.join(PICTURES_DIR, 'default_profile.png')
