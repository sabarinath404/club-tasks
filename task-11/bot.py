import os
import telebot
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater

import ast
import time
from telebot import types







BOT_TOKEN = os.environ.get('BOT_TOKEN')




bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Let's play a game!😎")
    bot.send_message(message.chat.id, "Choose one of the following: rock, paper, scissors")
    bot.send_message(message.chat.id, "RULES: \n 1. Rock beats scissors \n 2. Scissors beats paper \n 3. Paper beats rock \n 4. If both players choose the same object, it's a tie.")



@bot.message_handler(func=lambda message: True)
def start(message):
    player=message.text

    if(player == "rock" or player=="sessor" or player=="paper"):
        print("hihih")
        print("the messagg is "+player)
        choices = ['rock', 'paper', "scissors"]
        computer = random.choice(choices)
        if(player == computer):
            bot.send_message(message.chat.id, "computer: "+computer)
            bot.send_message(message.chat.id, "player: "+player)
            bot.send_message(message.chat.id, "Tie!")

        elif player == "rock":
            if computer == "paper":
                bot.send_message(message.chat.id, "computer: "+computer)
                bot.send_message(message.chat.id, "player: "+player)
                bot.send_message(message.chat.id, "You lose!")
            if computer == "scissors":
                bot.send_message(message.chat.id, "computer: "+computer)
                bot.send_message(message.chat.id, "player: "+player)
                bot.send_message(message.chat.id, "You win!")
        elif player == "scissors":
            if computer == "rock":
                bot.send_message(message.chat.id, "computer: "+computer)
                bot.send_message(message.chat.id, "player: "+player)
                bot.send_message(message.chat.id, "You lose!")
            if computer == "paper":
                bot.send_message(message.chat.id, "computer: "+computer)
                bot.send_message(message.chat.id, "player: "+player)
                bot.send_message(message.chat.id, "You win!")
        elif player == "paper":
            if computer == "scissors":
                bot.send_message(message.chat.id, "computer: "+computer)
                bot.send_message(message.chat.id, "player: "+player)
                bot.send_message(message.chat.id, "You lose!😕")
            if computer == "rock":
                bot.send_message(message.chat.id, "computer: "+computer)
                bot.send_message(message.chat.id, "player: "+player)
                bot.send_message(message.chat.id, "You win!🥳")
        
        

        bot.send_message(message.chat.id, "play again :)")





bot.infinity_polling()