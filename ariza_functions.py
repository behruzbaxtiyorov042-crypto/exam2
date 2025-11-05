from aiogram import Bot
from aiogram.types import Message
from aiogram import html
from aiogram.fsm.context import FSMContext

from ariza3 import admin_murojaat_tasdiq
from ariza3 import start_button
import ariza

baza = []


async def bot_ishga_tushganda(bot: Bot):
    await bot.send_message(7874452621, "Bot ishga tushdi...", reply_markup=start_button)


async def bot_toxtaganda(bot: Bot):
    await bot.send_message(7874452621, "Bot to'xtadi")



async def start_bosganda(message: Message, state: FSMContext):
    ism = message.from_user.first_name
    username = message.from_user.username
    chat_id = message.chat.id

    if chat_id not in baza:
        baza.append(chat_id)
        if message.text == "/start":
            await message.answer(
                f"Assalomu alaykum {html.bold(message.from_user.full_name)}",
                reply_markup=start_button
            )
    else:
        await message.answer("Salom berishga beraman, lekin siz ro'yxatda borsiz!")


async def ariza_bosganda(message: Message, state: FSMContext):
    await message.answer("Ariza topshirishga xush kelibsiz!\nIsm familyangizni kiriting!\n\nMasalan: Aliqulov Ulug'bek")
    await state.set_state(ariza.ArizaState.ism_familya)


async def ariza_ism_familya(message: Message, state: FSMContext):
    await state.update_data(ism_familya=message.text)
    await message.answer("Ism familyangiz qabul qilindi.\nYoshingizni kiriting!\n\nMasalan: 22")
    await state.set_state(ariza.ArizaState.yosh)


async def ariza_yosh(message: Message, state: FSMContext):
    await state.update_data(yosh=message.text)
    await message.answer("Yoshingiz qabul qilindi.\nQaysi texnologiyalarni bilasiz?\n\nMasalan: Python, Aiogram...")
    await state.set_state(ariza.ArizaState.texnologiya)


async def ariza_texnologiya(message: Message, state: FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer("Texnik bilimlaringiz qabul qilindi.\nTelefon raqamingizni kiriting!\n\nMasalan: +998 99 999 99 99...")
    await state.set_state(ariza.ArizaState.tel_raqam)


async def ariza_tel_raqam(message: Message, state: FSMContext):
    await state.update_data(tel_raqam=message.text)
    await message.answer("Telefon raqamingiz qabul qilindi.\nManzilingizni kiriting!\n\nMasalan: Termiz shahar...")
    await state.set_state(ariza.ArizaState.manzil)


async def ariza_manzil(message: Message, state: FSMContext):
    await state.update_data(manzil=message.text)
    await message.answer("Manzilingiz qabul qilindi.\nQanchaga ishlamoqchisiz?\n\nMasalan: 100-200$")
    await state.set_state(ariza.ArizaState.narx)


async def ariza_narx(message: Message, state: FSMContext):
    await state.update_data(narx=message.text)
    await message.answer("Narx qabul qilindi.\nTalabamisiz yoki ishchimisiz?\n\nMasalan: Talaba")
    await state.set_state(ariza.ArizaState.kasb)


async def ariza_kasb(message: Message, state: FSMContext):
    await state.update_data(kasb=message.text)
    await message.answer("Kasbingiz qabul qilindi.\nVaqtingizni kiriting!\n\nMasalan: 8:00 - 20:00")
    await state.set_state(ariza.ArizaState.mur_vaqt)


async def ariza_mur_vaqt(message: Message, state: FSMContext):
    await state.update_data(mur_vaqt=message.text)
    await message.answer("Murojaat vaqti qabul qilindi.\nMaqsadingizni yozing!\n\nMasalan: Dasturchi bo'lish")
    await state.set_state(ariza.ArizaState.maqsad)


async def ariza_maqsad(message: Message, state: FSMContext):
    await state.update_data(maqsad=message.text)
    malumotlar = await state.get_data()

    elon = f"""
    Ish joyi kerak:

    👨‍💼 Xodim: {malumotlar['ism_familya']}
    🕑 Yosh: {malumotlar['yosh']}
    📚 Texnologiya: {malumotlar['texnologiya']}
    🇺🇿 Telegram: @{message.from_user.username}
    📞 Aloqa: {malumotlar['tel_raqam']}
    🌐 Hudud: {malumotlar['manzil']}
    💰 Narxi: {malumotlar['narx']}
    👨🏻‍💻 Kasbi: {malumotlar['kasb']}
    🕰 Murojaat vaqti: {malumotlar['mur_vaqt']}
    🔎 Maqsad: {malumotlar['maqsad']}
    """
    await message.answer(elon)
    await message.answer("Arizani tasdiqlaysizmi? [Ha/Yo‘q]")
    await state.set_state(ariza.ArizaState.tasdiq)


async def ariza_tasdiq(message: Message, state: FSMContext, bot: Bot):
    if message.text.lower() == 'ha':
        await message.answer("Arizangiz qabul qilindi ✅")
        malumotlar = await state.get_data()
        elon = f"""
        🆕 {message.from_user.full_name} dan yangi ariza!

        👨‍💼 {malumotlar['ism_familya']}
        🕑 Yosh: {malumotlar['yosh']}
        📚 Texnologiya: {malumotlar['texnologiya']}
        🇺🇿 Telegram: @{message.from_user.username}
        📞 Aloqa: {malumotlar['tel_raqam']}
        🌐 Hudud: {malumotlar['manzil']}
        💰 Narxi: {malumotlar['narx']}
        👨🏻‍💻 Kasbi: {malumotlar['kasb']}
        🕰 Murojaat vaqti: {malumotlar['mur_vaqt']}
        🔎 Maqsad: {malumotlar['maqsad']}
        """
        await bot.send_message(7635494509, elon)
    else:
        await message.answer("Arizangiz bekor qilindi ❌")



async def stop_bosganda(message: Message, state: FSMContext):
    if await state.get_state() is None:
        await message.answer("Sizda faol ariza yo‘q.")
    else:
        await message.answer("Ariza topshirish bekor qilindi!")
        await state.clear()


async def help_bosganda(message: Message):
    matn = """
/start - Botni ishga tushuradi
/ariza - Ariza yozadi
/stop - Arizani bekor qiladi
/help - Yordam
"""
    await message.answer(matn)



async def admiga_murojaat_funcsion(message: Message, state: FSMContext):
    await message.answer("Adminga yubormoqchi bo‘lgan fikringizni kiriting:")
    await state.set_state(ariza.AdmingaMurojaatState.matn)


async def admin_m_matn(message: Message, state: FSMContext):
    await state.update_data(matn=message.text)
    await message.answer("Shu matnni yuborishga ishonchingiz komilmi?", reply_markup=admin_murojaat_tasdiq)
    await state.set_state(ariza.AdmingaMurojaatState.tasdiq)


async def adminga_m_tasdiq(message: Message, state: FSMContext, bot: Bot):
    malumotlar = await state.get_data()
    if message.text.lower() == 'ha':
        await bot.send_message(
            7635494509,
            f"{message.from_user.full_name} dan murojaat:\n\n{malumotlar['matn']}"
        )
        await message.answer("Xabaringiz yuborildi ✅")
    else:
        await message.answer("Xabaringiz yuborilmadi ❌")
    await state.clear()
