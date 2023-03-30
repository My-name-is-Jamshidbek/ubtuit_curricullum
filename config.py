"""
config variables
"""
import os
from dotenv import load_dotenv


# .env faylidagi o'zgaruvchilarni yuklash
load_dotenv()

# TOKEN, ADMIN_ID, va KEY o'zgaruvchilarini .env faylidan yuklash
TOKEN = os.getenv('TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
KEY = os.getenv('KEY')

ERRORS_SEND = False
ADMIN_USER = 'https://t.me/mal_un'
WEB_SAYT = 'https://github.com/My-name-is-Jamshidbek'
