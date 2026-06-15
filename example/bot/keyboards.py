from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.callbacks import Data, Navigation

main_menu_keyboard_builder = InlineKeyboardBuilder()
main_menu_keyboard_builder.add(
    InlineKeyboardButton(
        text="Deposit Menu",
        callback_data=Navigation.DEPOSIT_MENU,
    ),
)
main_menu_markup = main_menu_keyboard_builder.as_markup()

deposit_menu_keyboard_builder = InlineKeyboardBuilder()
deposit_menu_keyboard_builder.add(
    InlineKeyboardButton(
        text="Main Menu",
        callback_data=Navigation.MAIN_MENU,
    ),
    InlineKeyboardButton(
        text="10$",
        callback_data=Data.DEPOSIT(10),
    ),
    InlineKeyboardButton(
        text="20$",
        callback_data=Data.DEPOSIT(20),
    ),
    InlineKeyboardButton(
        text="30$",
        callback_data=Data.DEPOSIT(30),
    ),
)
deposit_menu_keyboard_builder.adjust(1, 3)
deposit_menu_markup = deposit_menu_keyboard_builder.as_markup()
