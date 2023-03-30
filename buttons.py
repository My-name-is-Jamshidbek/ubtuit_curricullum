"""
buttons
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# buttons
keyboard_menyu_admin = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_menyu_admin.add(
    KeyboardButton(text='👨🏻‍💻Konsultatsiya👨🏻‍💻'),
    KeyboardButton(text='👨‍💻Dasturchi👨‍💻'),
)

hafta_kunlari = ReplyKeyboardMarkup(resize_keyboard=True
                                    )
hafta_kunlari.add(
    KeyboardButton(text='Dushanba'),
    KeyboardButton(text='Seshanba')
)
hafta_kunlari.add(
    KeyboardButton(text='Chorshanba'),
    KeyboardButton(text='Payshanba')
)
hafta_kunlari.add(
    KeyboardButton(text='Juma'),
    KeyboardButton(text='Shanba')
)
hafta_kunlari.add(
    KeyboardButton(text='👨🏻‍💻Konsultatsiya👨🏻‍💻'),
    KeyboardButton(text='👨‍💻Dasturchi👨‍💻'),
)
hafta_kunlari.add(
    KeyboardButton(text='Boshiga qaytish'),
    KeyboardButton(text="Yangilash")
)
