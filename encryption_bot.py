import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters
from encryptdata import EncryptData
from bot_markups import *

user_message: dict[int, EncryptData] = {}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Function for greeting users and telling about what they should do. Can be called either by command "/start" either by clicking a callback button
    """
    if update.callback_query:
        """
        If this function called by callback button
        """
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Введи повідомлення")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Привіт, я Бот-шифрувальник! Для початку введи повідомлення")


async def add_info_and_choose_option(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message[update.effective_user.id] = EncryptData(data=update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Обери опцію:",
                                   reply_markup=await get_bot_options())


async def port_encrypt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    encrypt = user_message[update.effective_user.id]
    await encrypt.port_encrypt()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Зашифроване повідомлення: {encrypt.data}\nОбери подальшу опцію",
                                   reply_markup=await get_bot_options_if_message_is_encrypted_by_port())


async def port_decrypt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    encrypt = user_message[update.effective_user.id]
    await encrypt.port_decrypt()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Розшифроване повідомлення: {encrypt.data}\nОбери подальшу опцію",
                                   reply_markup=await get_bot_options())


async def magic_square_encrypt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    encrypt = user_message[update.effective_user.id]
    await encrypt.magic_square_enc_dec()
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Перетворене повідомлення: {encrypt.data}\nОбери подальшу опцію",
                                   reply_markup=await get_bot_options())

if __name__ == "__main__":
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_info_and_choose_option))
    app.add_handler(CallbackQueryHandler(port_encrypt, "port_encrypt"))
    app.add_handler(CallbackQueryHandler(port_decrypt, "port_decrypt"))
    app.add_handler(CallbackQueryHandler(magic_square_encrypt, "magic_square_enc_dec"))
    app.add_handler(CallbackQueryHandler(start, lambda data: data == "change_message"))
    app.run_polling()
