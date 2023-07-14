from telegram import InlineKeyboardMarkup, InlineKeyboardButton


async def get_bot_options() -> InlineKeyboardMarkup:
    """
    Returns an options' markup for Telegram
    :return: InlineKeyboardMarkup
    """
    keyboard = [
        [
            InlineKeyboardButton(text="Зашифрувати методом Порти", callback_data="port_encrypt"),
        ],
        [
            InlineKeyboardButton(text="Розшифрувати методом Порти", callback_data="port_decrypt"),
        ],
        [
            InlineKeyboardButton(text="Зашифрувати (розшифрувати) методом магічного квадрату",
                                 callback_data="magic_square_enc_dec")
        ],
        [
            InlineKeyboardButton(text="Змінити повідомлення", callback_data="change_message")
        ]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    return markup


async def get_bot_options_if_message_is_encrypted_by_port() -> InlineKeyboardMarkup:
    """
        Returns an options' markup for Telegram without encryption button
        :return: InlineKeyboardMarkup
        """
    keyboard = [
        [
            InlineKeyboardButton(text="Розшифрувати методом Порти", callback_data="port_decryption"),
        ],
        [
            InlineKeyboardButton(text="Змінити повідомлення", callback_data="change_message")
        ]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    return markup

