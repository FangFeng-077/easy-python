#!/usr/bin/env python3

"""
CS106AP PyCharm Intro Project
"""

from karel.stanfordkarel import *
import platform


def draw_side():
    """
    Draws a single side of a square.
    """
    put_beeper()
    move()
    put_beeper()
    move()
    put_beeper()
    move()
    turn_left()


def draw_square():
    """
    Draws an entire square.
    """
    i = 0
    while i < 4:
        draw_side()


def main():
    draw_square()


if __name__ == "__main__":
    execute_karel_task(main)