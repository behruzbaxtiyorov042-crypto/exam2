import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


from ariza import ArizaState, AdmingaMurojaatState
from aiogram.filters import CommandStart, Command
from aiogram.types import BotCommand
import ariza_functions



TOKEN = "8385216008:AAEfx5fluKVX1dk4Qye1A9CsoDF_H-8PZL4"
dp = Dispatcher()

async def main():
    dp.startup.register(ariza_functions.bot_ishga_tushganda)
    dp.message.register(ariza_functions.start_bosganda, CommandStart())
    dp.message.register(ariza_functions.ariza_bosganda, Command('ariza'))
    dp.message.register(ariza_functions.stop_bosganda, Command('stop'))
    dp.message.register(ariza_functions.help_bosganda, F.text == '/help')
    dp.message.register(ariza_functions.admiga_murojaat_funcsion, F.text == "Adminga murojaat")
    dp.message.register(ariza_functions.admin_m_matn, AdmingaMurojaatState.matn)
    dp.message.register(ariza_functions.adminga_m_tasdiq, AdmingaMurojaatState.tasdiq)
    dp.message.register(ariza_functions.admiga_murojaat_funcsion, F.text == "userga murrojaat")
    dp.message.register(ariza_functions.ariza_ism_familya, ArizaState.ism_familya)
    dp.message.register(ariza_functions.ariza_yosh, ArizaState.yosh)
    dp.message.register(ariza_functions.ariza_texnologiya, ArizaState.texnologiya)
    dp.message.register(ariza_functions.ariza_tel_raqam, ArizaState.tel_raqam)
    dp.message.register(ariza_functions.ariza_manzil, ArizaState.manzil)
    dp.message.register(ariza_functions.ariza_narx, ArizaState.narx)
    dp.message.register(ariza_functions.ariza_kasb, ArizaState.kasb)
    dp.message.register(ariza_functions.ariza_mur_vaqt, ArizaState.mur_vaqt)
    dp.message.register(ariza_functions.ariza_maqsad, ArizaState.maqsad)
    dp.message.register(ariza_functions.ariza_tasdiq, ArizaState.tasdiq)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.shutdown.register(ariza_functions.bot_toxtaganda)

    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish uchun..."),
        BotCommand(command="/ariza", description="ariza topshirish uchun"),

        BotCommand(command="/stop", description="dasturni to'xtadadi")
    ])
    await dp.start_polling(bot)



asyncio.run(main())