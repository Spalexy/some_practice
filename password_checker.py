# -*- coding: utf-8 -*-

import urwid


def has_letters(password):
    return any(char.isalpha() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_digit(password):
    return any(char.isdigit() for char in password)


def is_long_enough(password):
    return len(password) > 12


def has_symbols(password):
    return any((not char.isdigit() and not char.isalpha()) for char in password)


def has_not_only_symbols(password):
    return has_letters(password) or has_digit(password)


def get_score(password):
    score = 0
    for callback in callbacks:
        if callback(password):
            score += 2
    return score


def on_ask_change(edit, new_edit_text):
    reply.set_text('Рейтинг этого пароля: %s' % get_score(new_edit_text))


callbacks = [
    has_letters,
    has_upper_letters,
    has_lower_letters,
    has_digit,
    is_long_enough,
    has_symbols,
    has_not_only_symbols
]

ask = urwid.Edit('Введите пароль: ', mask='*')
reply = urwid.Text('')
menu = urwid.Pile([ask, reply])
menu = urwid.Filler(menu, valign='top')

urwid.connect_signal(ask, 'change', on_ask_change)

urwid.MainLoop(menu).run()
