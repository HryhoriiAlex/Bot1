from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton("/links"))

ikb = InlineKeyboardMarkup(row_width=2)
ikb1 = InlineKeyboardButton(text="Посилання 1",
                            url="https://chat.openai.com/chat?__cf_chl_tk=_QkIjVMRo_oRsYGyxm8yhTpT8brck0nLkO8Cd2yZUHA-1677503836-0-gaNycGzNGJA")
ikb2 = InlineKeyboardButton(text="Посилання 2",
                            url="https://cozy-fairy-098385.netlify.app/index.html")
ikb.add(ikb1, ikb2)