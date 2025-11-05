from aiogram.fsm.state import State, StatesGroup

class ArizaState(StatesGroup):
    ism_familya = State()
    yosh = State()
    texnologiya = State()
    tel_raqam = State()
    manzil = State()
    narx = State()
    kasb = State()
    mur_vaqt = State()
    maqsad = State()
    tasdiq = State()

class AdmingaMurojaatState(StatesGroup):
    matn = State()
    tasdiq = State()
class usergamurojaaat(StatesGroup):
    id = State()
    matn = State()
    tasdiq = State()