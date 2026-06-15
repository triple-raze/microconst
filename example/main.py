from aiogram import Bot, Dispatcher

from bot import main_router

dispatcher = Dispatcher()

dispatcher.include_router(main_router)

bot = Bot("TOKEN")

dispatcher.run_polling(bot)
