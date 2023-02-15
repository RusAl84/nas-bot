from webbrowser import get
import telebot
import get_data as gd
import tester as ts


bot = telebot.TeleBot('6103350951:AAHrZiXU61n0ti_3gSnBEa_5U21CZrUxNwQ')
global categories, test_data, test_num, mark, cur_cat, cur_theme
categories = gd.load_data()
test_data = ts.load_data()
cur_cat = cur_theme = test_num = 0
mark =""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global categories, test_data, test_num, mark, cur_cat, cur_theme
    help_message = "Сюда вставьте название и описание своего проекта" \
        " \n Для того чтобы получить информацию введите слово /info." \
        " \n Для того чтобы проверить свои знания введите слово /test."

    if str(message.text).lower() == "привет":
        bot.send_message(
            message.from_user.id, "Привет, чем я могу тебе помочь? Для информации введите /help.")
    elif cur_cat == -1:
        if str(message.text).isdigit():
            cur_cat = int(message.text)
            str1 = gd.get_sub_categories(categories, cur_cat)
            cur_theme = -1
            bot.send_message(
                message.from_user.id, str1)
        else:
            bot.send_message(
                message.from_user.id, "не верно введен номер раздела")
    elif cur_theme == -1:
        if str(message.text).isdigit():
            cur_theme = int(message.text)
            data = gd.get_desc(categories, cur_cat, cur_theme)
            cur_cat = 0
            cur_theme = 0
            str1 = f"{data} \n {help_message}"
            bot.send_message(
                message.from_user.id, str1)
        else:
            bot.send_message(
                message.from_user.id, "не верно введен номер темы")
    elif test_num > 0:
        cur_cat = 0
        cur_theme = 0
        result =ts.check_answer(test_data, test_num - 1, message.text)
        mark+=f"\n Вопрос {test_num-1}: {result:.2f}%\n"
        if test_num < len(test_data):
            str1 = ts.get_question(test_data, test_num)
            bot.send_message(
                message.from_user.id, str1)
            test_num += 1
        else:
            test_num = 0
            str1 = f"{mark} \n \n {help_message}"
            bot.send_message(
                message.from_user.id, str1)
    elif str(message.text).lower() == "/info":
        cur_cat = -1
        str1 = gd.get_categories(categories)
        bot.send_message(
            message.from_user.id, str1)
    elif str(message.text).lower() == "/test":
        str1 = ts.get_question(test_data, test_num)
        cur_cat = 0
        cur_theme = 0
        test_num = 1
        mark = ""
        bot.send_message(
            message.from_user.id, str1)
    elif str(message.text).lower() == "/help":
        bot.send_message(
            message.from_user.id, help_message)
    else:
        bot.send_message(message.from_user.id, "Для информации введите /help.")


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
