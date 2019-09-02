from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def move_to_wall():
    while front_is_clear():
        move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def move_to_newspaper():
    move_to_wall()
    turn_right()
    move()
    turn_left()
    move()


def turn_around():
    turn_left()
    turn_left()


def move_to_start():
    move()
    turn_right()
    move()
    turn_left()
    move_to_wall()
    turn_around()


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move_to_newspaper()
    pick_beeper()
    turn_around()
    move_to_start()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
