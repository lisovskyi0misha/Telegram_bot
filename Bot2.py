import telebot
from telebot import types
from dict import dict
bot = telebot.TeleBot('5271216065:AAGqV9ZMPdpavJ44yi4Q1VMcboYnq4FUDbg')
@bot.message_handler(commands=['start'])
def start(message):
    doc =  open('Start.txt', 'rb').read()
    bot.send_message(message.chat.id, doc)

    #Кнопки

@bot.message_handler(commands=['ready'])
def corners(message):
    markup = types.ReplyKeyboardMarkup()
    two_corners = types.KeyboardButton('2 угла')
    three_corners = types.KeyboardButton('3 угла')
    four_corners = types.KeyboardButton('4 угла')
    markup.add(two_corners, three_corners, four_corners)
    bot.send_message(message.chat.id, 'Сколько углов надо перевернуть?', reply_markup=markup)

                                  # Продолжение двух углов

@bot.message_handler()
def two_corners_continue(message):
    if message.text == '2 угла':
        markup = types.ReplyKeyboardMarkup()
        #Все по русски
        case1 = types.KeyboardButton('Случай 1')
        case2 = types.KeyboardButton('Случай 2')
        case3 = types.KeyboardButton('Случай 3')
        markup.add(case1, case2, case3)
        bot.send_photo(message.chat.id, open('Рисунки/2corners.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Выбери случай', reply_markup=markup)


 # Продолжение трех углов
    elif message.text == '3 угла':
        markup = types.ReplyKeyboardMarkup()
        # английская у
        case1 = types.KeyboardButton('Слyчай 1')
        case2 = types.KeyboardButton('Слyчай 2')
        markup.add(case1, case2)
        bot.send_photo(message.chat.id, open('Рисунки/Fish.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Выбери случай', reply_markup=markup)
# Продолжение четырех углов
    elif message.text == '4 угла':
        # английская с
        markup = types.ReplyKeyboardMarkup()
        case1 = types.KeyboardButton('Cлучай 1')
        case2 = types.KeyboardButton('Cлучай 2')
        markup.add(case1, case2)
        bot.send_photo(message.chat.id, open('Рисунки/Cross.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Выбери случай', reply_markup=markup)
# 2 corners
    elif message.text == 'Случай 1':
        bot.send_message(message.chat.id, 'r U R\' U\' r\' F R F\'')
    elif message.text == 'Случай 2':
        bot.send_message(message.chat.id, 'R2 D R\' U2 R D\' R\' U2 R\'')
    elif message.text == 'Случай 3':
        bot.send_message(message.chat.id, 'F\' r U R\' U\' r\' F R')
# 3 corners
    elif message.text == 'Слyчай 1':
        bot.send_message(message.chat.id, 'R U R\' U R U2 R\'')
    elif message.text == 'Слyчай 2':
        bot.send_message(message.chat.id,'R U2 R\' U\' R U\' R\'')

        #4 corners
    elif message.text == 'Cлучай 1':
        bot.send_message(message.chat.id, 'R U2 R\' U\' R U R\' U\' R U\' R\'')
    elif message.text == 'Cлучай 2':
        bot.send_message(message.chat.id, 'R U2 R2 U\' R2 U\' R2 U2 R')
#Информация по сторонам

    elif message.text == 'R':
        bot.send_photo(message.chat.id, open(dict['R'], 'rb'))
    elif message.text == "R\'":
        bot.send_photo(message.chat.id, open(dict['R\''], 'rb'))
    elif message.text == 'L':
        bot.send_photo(message.chat.id, open(dict['L'], 'rb'))
    elif message.text == 'L\'':
        bot.send_photo(message.chat.id, open(dict['L\''], 'rb'))
    elif message.text == 'U':
        bot.send_photo(message.chat.id, open(dict['U'], 'rb'))
    elif message.text == 'U\'':
        bot.send_photo(message.chat.id, open(dict['U\''], 'rb'))
    elif message.text == 'F':
        bot.send_photo(message.chat.id, open(dict['F'], 'rb'))
    elif message.text == 'F\'':
        bot.send_photo(message.chat.id, open(dict['F\''], 'rb'))
    elif message.text == 'D':
        bot.send_photo(message.chat.id, open(dict['D'], 'rb'))
    elif message.text == 'D\'':
        bot.send_photo(message.chat.id, open(dict['D\''], 'rb'))
    elif message.text == 'r':
        bot.send_photo(message.chat.id, open(dict['r'], 'rb'))
    elif message.text == 'r\'':
        bot.send_photo(message.chat.id, open(dict['r\''], 'rb'))
    else:
        bot.send_message(message.chat.id, 'Не знаю такой стороны.')

#
bot.polling(non_stop=True)
