from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands (
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("support", "Texnik yordamga xabar yozish"),
            types.BotCommand("support_call", "Texnik yordam bilan suhbatlashing"),
            types.BotCommand("help", "Yordam"),
        ]
    )
