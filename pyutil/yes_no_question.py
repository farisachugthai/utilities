#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mod that shows an easy, consistent way to handle user input."""
import sys


def _handle_args(possible_answer):
    global question
    try:
        question = args[0]
    except IndexError:
        sys.exit('Must provide question to ask. Exiting.')
    try:
        answer = args[1]
    except IndexError:
        return False
    else:
        return answer


def yes_no_question(question, answer):
    """Prompt the user until valid input is provided."""
    if not answer:
        while True:
            text = input(question + '\n' + ' [y/n] ' + '\n')
            if text.lower().startswith("y"):
                return True
            elif text.lower().startswith("n"):
                return False
            else:
                print(
                    "Sorry, I didn't understand that. Please type yes or no.")

    else:
        if answer is True:
            return True
        elif answer is False:
            return False
        else:
            sys.exit()


if __name__ == "__main__":
    args = sys.argv[1:]
    answer = _handle_args(args)

    yes_no_question(question, answer)
