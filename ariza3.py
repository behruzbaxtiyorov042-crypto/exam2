from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
        ],
        [
        ],
        [
            KeyboardButton(text='/ariza'),

        ]
    ],
    resize_keyboard=True,
    # is_persistent=True,
    # one_time_keyboard=True,
    input_field_placeholder='Tugmalarni birini bosing!'
)


admin_murojaat_tasdiq = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="HA"),
            KeyboardButton(text="YO'Q")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Adminga matnnigizni yuborishni tasdiqlang!!!',
    one_time_keyboard=True

)