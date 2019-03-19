#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mod that shows an easy, consistent way to handle user input."""
import sys


def yes_no_question(question):
    """Continuing prompt the user until valid input is provided."""
    while True:
        print(question)
        print(" [y/n] ")
        text = input()
        if text.lower().startswith("y"):
            return True
        elif text.lower().startswith("n"):
            return False
        else:
            print("Sorry, I didn't understand that. Please type yes or no.")


if __name__ == "__main__":
    sys.exit(
        "Well I've got to admit this is embarassing. I thought you'd import"
        "me!")
