"""
apps
"""
from loader import bot, dp
from buttons import *
from database import *
from states import *

from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram import types


# start
@dp.message_handler(CommandStart())
async def start(message: types.Message):
    """

    :param message:
    """
    if database_user_table_retrieve_time_data(telegram_id=message.from_user.id) is not None:
        m = database_user_table_retrieve_time_data(message.from_user.id)
        await message.answer("Sana: " + m[0])
        await message.answer('Hafta kunini tanlang:', reply_markup=hafta_kunlari)
        await User.kun.set()
    else:
        await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
        await User.username.set()


# qolgan matnlar
@dp.message_handler()
async def els(message: types.Message):
    """
    :param message:
    """
    if database_user_table_retrieve_time_data(telegram_id=message.from_user.id) is not None:
        m = database_user_table_retrieve_time_data(message.from_user.id)
        await message.answer("Sana: " + m[0])
        await message.answer('Hafta kunini tanlang:', reply_markup=hafta_kunlari)
        await User.kun.set()
    else:
        await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
        await User.username.set()


@dp.message_handler(state=User.username, content_types=types.ContentType.TEXT)
async def username(message: types.Message, state: FSMContext):
    """
    :param message:
    :param state:
    """
    if message.text == '👨🏻‍💻Konsultatsiya👨🏻‍💻':
        await message.answer(f"Admin: t.me/mal_un")
        await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
        await User.username.set()
    elif message.text == '👨‍💻Dasturchi👨‍💻':
        await message.answer(f"Jamshidbek Ollanazarov: t.me/mal_un")
        await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
        await User.username.set()
    else:
        try:
            int(message.text)
            await state.update_data(studentuser=message.text)
            await message.answer('Student parolingizni kriting:')
            await User.parol.set()
        except Exception as _:
            await message.answer('Student id noto`g`ri!')
            await User.username.set()


@dp.message_handler(state=User.parol, content_types=types.ContentType.TEXT)
async def davomatga(message: types.Message, state: FSMContext):
    """
    :param message:
    :param state:
    """
    if message.text == '👨🏻‍💻Konsultatsiya👨🏻‍💻':
        await message.answer(f"Admin: t.me/mal_un")
        await message.answer('Student parolingizni kriting:')
        await User.parol.set()
    elif message.text == '👨‍💻Dasturchi👨‍💻':
        await message.answer(f"Jamshidbek Ollanazarov: t.me/mal_un")
        await message.answer('Student parolingizni kriting:')
        await User.parol.set()
    else:
        user = await state.get_data()
        user = user.get('studentuser')
        await bot.delete_message(message.from_user.id,message.message_id)
        msgid = await message.answer('Tekshirilmoqda...')
        students_schedule_r = students_schedule(password=message.text, username=user, telegram_id=message.from_user.id)
        if students_schedule_r['result']:
            database_user_add_data(
                telegram_id=message.from_user.id,
                student_id=user,
                student_password=message.text,
                student_about=students_schedule_r['reason']
            )
            await state.update_data(parol=message.text)
            await bot.delete_message(chat_id=message.from_user.id, message_id=msgid.message_id)
            await message.answer(students_schedule_r['reason'])
            await message.answer('Hafta kunini tanlang:', reply_markup=hafta_kunlari)
            await User.kun.set()
        else:
            await bot.delete_message(chat_id=message.from_user.id, message_id=msgid.message_id)
            await message.answer('Student parol yoki id xato!')
            await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
            await User.username.set()


@dp.message_handler(state=User.kun, content_types=types.ContentType.TEXT)
async def haftalar(message: types.Message):
    """
    :param message:
    """
    if message.text == '👨🏻‍💻Konsultatsiya👨🏻‍💻':
        await message.answer(f"Admin: t.me/mal_un")
        await message.answer('Hafta kunini tanlang:', reply_markup=hafta_kunlari)
        await User.kun.set()
    elif message.text == '👨‍💻Dasturchi👨‍💻':
        await message.answer(f"Jamshidbek Ollanazarov: t.me/mal_un")
        await message.answer('Hafta kunini tanlang:', reply_markup=hafta_kunlari)
        await User.kun.set()
    elif message.text == 'Boshiga qaytish':
        database_user_table_remove_data(message.from_user.id)
        database_user_remove_data(message.from_user.id)
        await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
        await User.username.set()
    elif message.text == "Yangilash":
        msgid = await message.answer("Yangilanmoqda...")
        telegram_id, student_id, student_parol, about = database_user_retrieve_data(message.from_user.id)
        database_user_table_remove_data(message.from_user.id)
        # database_user_remove_data(message.from_user.id)
        about = students_schedule(password=student_parol, username=student_id, telegram_id=telegram_id)
        await bot.delete_message(chat_id=message.from_user.id, message_id=msgid.message_id)
        await message.answer(about['reason'])
        await message.answer('Hafta kunini tanlang:', reply_markup=hafta_kunlari)
        await User.kun.set()
    elif kuntek(message.text):
        if database_user_table_retrieve_data(telegram_id=message.from_user.id, day=message.text) is not None:
            await message.answer(database_user_table_retrieve_data(telegram_id=message.from_user.id,
                                                                   day=message.text)[0],
                                 reply_markup=hafta_kunlari)
            await User.kun.set()
        else:
            await message.answer(
                text='Sizning dars jadvalingizni yangilashda xatolik yuz berdi iltimos qaytadan urinib ko`ring.')
            await message.answer('Student id (username) ingizni kiriting:', reply_markup=keyboard_menyu_admin)
            await User.username.set()
    else:
        await message.answer('Bunday kun mavjud emas!', reply_markup=hafta_kunlari)
        await User.kun.set()
