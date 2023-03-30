"""
states
"""
from aiogram.dispatcher.filters.state import State, StatesGroup


class User(StatesGroup):
    """
    userlar uchun asosiy holat
    """
    username = State()
    parol = State()
    kun = State()
