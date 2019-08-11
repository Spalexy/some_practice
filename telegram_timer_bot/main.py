#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ptbot
from pytimeparse import parse


my_bot_token = os.getenv('MY_BOT_TOKEN')
chat_id = os.getenv('CHAT_ID')
initial_msg = 'На сколько запустить таймер?'
bot = ptbot.Bot(my_bot_token)


def finish_notify():
    finish_notify_msg = 'Время вышло!'
    bot.send_message(chat_id, finish_notify_msg)


def reply(user_input):
    seconds_quantity = parse(user_input)
    bot.create_timer(seconds_quantity, finish_notify)
    start_timer_msg = ('Таймер запущен на {}  секунд'.format(seconds_quantity))
    bot.send_message(chat_id, start_timer_msg)
    progress_msg = ('Осталось {} секунды'.format(seconds_quantity))
    progressbar = render_progressbar(seconds_quantity, 0)
    progress_msg_id = bot.send_message(chat_id, progress_msg)
    progressbar_id = bot.send_message(chat_id, progressbar)
    bot.create_countdown(seconds_quantity, notify_progress,
                         progress_msg_id=progress_msg_id,
                         progressbar_id=progressbar_id,
                         seconds_quantity=seconds_quantity)


def notify_progress(secs_left, progress_msg_id, progressbar_id, seconds_quantity):
    progress_msg = ('Осталось {} секунды'.format(secs_left))
    progressbar = render_progressbar(seconds_quantity, seconds_quantity - secs_left)
    bot.update_message(chat_id, progress_msg_id, progress_msg)
    bot.update_message(chat_id, progressbar_id, progressbar)


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


bot.send_message(chat_id, initial_msg)
bot.wait_for_msg(reply)
