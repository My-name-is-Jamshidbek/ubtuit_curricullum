"""
data base
"""

import time
import datetime

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

# from cryptography.fernet import Fernet

from config import *

import sqlite3
from sqlite3 import Connection

# database
if not os.path.exists("users.db"):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute(
        "CREATE TABLE users (telegram_id INTEGER PRIMARY KEY, student_id TEXT, student_password TEXT, student_about "
        "TEXT)")
    c.execute(
        "CREATE TABLE users_table (telegram_id INTEGER PRIMARY KEY, student_id TEXT, student_password TEXT, "
        "yuklangan_sana TEXT, dushanba TEXT, seshanba TEXT, chorshanba TEXT, payshanba TEXT, juma TEXT, shanba TEXT)")

    conn.commit()
    conn.close()


def database_user_table_add_data(telegram_id: str, student_id: str, student_password: str, yuklangan_sana: str,
                                 dushanba: str, seshanba: str,
                                 chorshanba: str, payshanba: str, juma: str, shanba: str) -> None:
    """
    :rtype: object
    :param telegram_id:
    :param student_id:
    :param student_password:
    :param yuklangan_sana:
    :param dushanba:
    :param seshanba:
    :param chorshanba:
    :param payshanba:
    :param juma:
    :param shanba:
    :return:
    """
    connect: Connection = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute(
        "INSERT OR IGNORE INTO users_table (telegram_id, student_id, student_password, yuklangan_sana, dushanba, "
        "seshanba, "
        "chorshanba, payshanba, juma, shanba) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (telegram_id, student_id, student_password, yuklangan_sana, dushanba, seshanba, chorshanba, payshanba, juma,
         shanba))
    connect.commit()
    connect.close()


def database_user_retrieve_data(telegram_id: str) -> object:
    """
    :param telegram_id:
    :return: None:
    """
    connect = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
    result = connect_cursor.fetchone()
    connect.close()
    telegram_id, student_id, student_parol, about = result
    #
    # cipher_suite = Fernet(KEY)
    # plain_text = cipher_suite.decrypt(student_parol)
    # student_parol = plain_text.decode()
    result = [telegram_id, student_id, student_parol, about]
    return result


def database_user_table_retrieve_time_data(telegram_id: str) -> object:
    """
    :param telegram_id:
    :return:
    """
    connect = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute(f"SELECT yuklangan_sana FROM users_table WHERE telegram_id={telegram_id}")
    result = connect_cursor.fetchone()
    connect.close()
    return result


def database_user_table_retrieve_data(telegram_id: str, day: str) -> object:
    """
    :param day:
    :param telegram_id:
    :return:
    """
    connect = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute(f"SELECT {day} FROM users_table WHERE telegram_id={telegram_id}")
    result = connect_cursor.fetchone()
    connect.close()
    return result


def database_user_add_data(telegram_id: int, student_id: int, student_password: str, student_about: str) -> None:
    """
    :param telegram_id:
    :param student_id:
    :param student_password:
    :param student_about:
    :return: None:
    """
    # cipher_suite = Fernet(KEY)
    # password = str(student_password).encode()
    # student_password = cipher_suite.encrypt(password)
    connect = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute("INSERT OR IGNORE INTO users (telegram_id, student_id, student_password, student_about) "
                           "VALUES (?,?,"
                           "?,?)",
                           (telegram_id, student_id, student_password, student_about))
    connect.commit()
    connect.close()


def database_user_table_remove_data(telegram_id: str) -> None:
    """
    :param telegram_id:
    :return:
    """
    connect = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute("DELETE FROM users_table WHERE telegram_id=?", (telegram_id,))
    connect.commit()
    connect.close()


def database_user_remove_data(telegram_id: str) -> None:
    """
    :param telegram_id:
    :return: None:
    """
    connect = sqlite3.connect("users.db")
    connect_cursor = connect.cursor()
    connect_cursor.execute("DELETE FROM users WHERE telegram_id=?", (telegram_id,))
    connect.commit()
    connect.close()


# selenium
def students_schedule(password: str, username: str, telegram_id: str) -> dict:
    """
    class schedule
    :param telegram_id:
    :param username:
    :param password:
    """
    browser = Chrome()
    browser.get("https://student.ubtuit.uz/education/time-table")
    if len(str(password)) > 5 and len(str(username)) > 5:
        el = browser.find_element(By.ID, 'formstudentlogin-login')
        el.send_keys(username)
        el = browser.find_element(By.ID, 'formstudentlogin-password')
        el.send_keys(password)
        el = browser.find_element(By.XPATH, '/html/body/div/div/div/form/div[2]/div/div[2]/button')
        el.click()
        time.sleep(10)
    else:
        return {'result': False, "reason": "Username yoki parol xato!"}
    t = True
    try:
        el = browser.find_element(By.CLASS_NAME, "user-name")
        user_name = el.text
        el = browser.find_element(By.CLASS_NAME, "user-role")
        user_group = el.text
    except Exception as _:
        return {'result': False, "reason": "Username yoki parol xato!"}
    el = browser.find_element(By.XPATH, '/html/body/div/div[2]/section/div/div[1]/div/div[2]/div/ul/li[5]/a')
    el.click()
    while t:
        time.sleep(1)
        el = browser.find_element(By.CLASS_NAME, "select2-selection__rendered")
        yuklangan_sana: str = el.text
        week = el.text.split()
        el = browser.find_element(By.XPATH, '/html/body/div/div[2]/section/div/div[3]')
        el = el.text
        if el == 'Ushbu davrga dars soatlari belgilanmagan':
            el = browser.find_element(By.XPATH, '/html/body/div/div[2]/section/div/div[2]/form/div[1]/a')
            el.click()
            time.sleep(1)
            t = False
        elif test_date(day=int(week[4]), month=str(week[5])):
            t = False
        else:
            el = browser.find_element(By.XPATH, '/html/body/div/div[2]/section/div/div[2]/form/div[3]/a')
            el.click()
    darsjadval = {}
    time.sleep(1)
    for i in range(1, 4):
        try:
            el = browser.find_element(By.XPATH, f"/html/body/div/div[2]/section/div/div[3]/div[{i}]/div/div[1]/h3")
            hafta_kuni = el.text.split('\n')[0]
            el = browser.find_element(By.XPATH, f"/html/body/div/div[2]/section/div/div[3]/div[{i}]/div/div[1]/h3/span")
            hafta_kuni1 = '     ' + el.text
            jadval = browser.find_element(By.XPATH, f"/html/body/div/div[2]/section/div/div[3]/div[{i}]/div/div[2]/ul")
            jadval = jadval.text
            darsjadval[hafta_kuni] = {'kun': hafta_kuni + hafta_kuni1, 'jadval': jadval}
        except Exception as _:
            pass
    for i in range(1, 4):
        try:
            el = browser.find_element(By.XPATH, f"/html/body/div/div[2]/section/div/div[4]/div[{i}]/div/div[1]/h3")
            hafta_kuni = el.text.split('\n')[0]
            el = browser.find_element(By.XPATH, f"/html/body/div/div[2]/section/div/div[4]/div[{i}]/div/div[1]/h3/span")
            hafta_kuni1 = '     ' + el.text
            jadval = browser.find_element(By.XPATH, f"/html/body/div/div[2]/section/div/div[4]/div[{i}]/div/div[2]/ul")
            jadval = jadval.text
            darsjadval[hafta_kuni] = {'kun': hafta_kuni + hafta_kuni1, 'jadval': jadval}
        except Exception as _:
            pass
    for i in ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba']:
        if not (i in darsjadval.keys()):
            darsjadval[i] = {'jadval': 'Dars mavjud emas!', 'kun': i}
    database_user_table_add_data(
        telegram_id=telegram_id,
        student_id=username,
        student_password=password,
        yuklangan_sana=yuklangan_sana,
        dushanba=f"{darsjadval['Dushanba']['kun']} \n{darsjadval['Dushanba']['jadval']}",
        seshanba=f"{darsjadval['Seshanba']['kun']} \n{darsjadval['Seshanba']['jadval']}",
        chorshanba=f"{darsjadval['Chorshanba']['kun']} \n{darsjadval['Chorshanba']['jadval']}",
        payshanba=f"{darsjadval['Payshanba']['kun']} \n{darsjadval['Payshanba']['jadval']}",
        juma=f"{darsjadval['Juma']['kun']} \n{darsjadval['Juma']['jadval']}",
        shanba=f"{darsjadval['Shanba']['kun']} \n{darsjadval['Shanba']['jadval']}"
    )
    return {'result': True, "reason": f"ism: {user_name}\nguruh: {user_group}"}


# other functions
def test_date(day: int, month: str) -> bool:
    """
    :param day:
    :param month:
    :return:
    """
    months = dict(yanvar=1, fevral=2, mart=3, aprel=4, may=5, iyun=6, iyul=7, avgust=8, sentabr=9, oktabr=10, noyabr=11,
                  dekabr=12)
    month = months[month]
    month_now = datetime.datetime.now().month
    day_now = datetime.datetime.now().day
    datetime_now = datetime.datetime.strptime(f"{month_now}/{day_now}", '%m/%d')  # datetime.now()
    datetime_ = datetime.datetime.strptime(f"{month}/{day}", '%m/%d')
    if datetime_ > datetime_now:
        return True
    else:
        return False


def kuntek(kun: str) -> bool:
    """
    :param kun:
    :return: bool:
    """
    if kun not in 'Dushanba' and kun not in 'Seshanba' and kun not in 'Chorshanba' and kun not in 'Payshanba' and kun \
            not in 'Juma' and kun not in 'Shanba':
        return False
    else:
        return True
