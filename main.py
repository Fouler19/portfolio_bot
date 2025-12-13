from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import TOKEN

bot = TeleBot(TOKEN)

cancel_button = "🚫 Отмена"
hideBoard = types.ReplyKeyboardRemove()


def gen_markup(rows):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for row in rows:
        markup.add(KeyboardButton(row))
    markup.add(KeyboardButton(cancel_button))
    return markup


def gen_inline_markup(rows):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for row in rows:
        markup.add(InlineKeyboardButton(row, callback_data=row))
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "👋 Привет!\n\n"
        "🤖 Бот-портфолио\n\n"
        "ℹ️ /info — список команд"
    )


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(
        message.chat.id,
        "🤖 Бот-портфолио\n\n"
        "📁 /projects — проекты\n"
        "➕ /new_project — добавить проект\n"
        "✏️ /edit_project — редактировать\n"
        "❌ /delete_project — удалить\n"
        "ℹ️ /info — помощь",
        reply_markup=hideBoard
    )


@bot.message_handler(commands=['new_project'])
def new_project(message):
    bot.send_message(
        message.chat.id,
        "➕ Введи название проекта:",
        reply_markup=gen_markup(["Пример проекта"])
    )


@bot.message_handler(func=lambda m: m.text == cancel_button)
def cancel(message):
    bot.send_message(
        message.chat.id,
        "❌ Отменено\nℹ️ /info",
        reply_markup=hideBoard
    )
@bot.message_handler(commands=['set_status'])
def set_status(message):
    db.update_project_status(1, "Разработан")
    bot.send_message(
        message.chat.id,
        "✅ Статус проекта обновлён: Разработан"
    )
    
   
    
    


print("Bot started")
bot.polling(none_stop=True)
