from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from microconst import parse_entry

from bot.callbacks import Data, Navigation
from bot.keyboards import deposit_menu_markup, main_menu_markup

router = Router()


@router.message(Command("start"))
async def start(message: Message) -> None:
    await message.answer("Hello there!", reply_markup=main_menu_markup)


@router.callback_query(F.data == Navigation.MAIN_MENU)
async def main_menu(callback: CallbackQuery) -> None:
    await callback.message.answer("Hello there!", reply_markup=main_menu_markup)


@router.callback_query(F.data == Navigation.DEPOSIT_MENU)
async def deposit_menu(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "Select value to deposit", reply_markup=deposit_menu_markup
    )


@router.callback_query(F.data.startswith(Data.DEPOSIT))
async def process_deposit(callback: CallbackQuery) -> None:
    # Parsing data with Key method (no need to put type explictly)
    money_count = Data.DEPOSIT.parse_entry(callback.data)
    # Though you can do it another way
    money_count = parse_entry(callback.data, int)

    await callback.answer(
        f"Processed money! You lost {money_count}$",
        reply_markup=main_menu_markup,
    )
