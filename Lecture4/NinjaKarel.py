from karel.stanfordkarel import *


def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise
    """
    turn_left()
    turn_left()
    turn_left()


def climb_spider_wall():
    """
    Pre-condition: Karel is facing north and surrounded by two walls
    Post-condition: Karel is facing north and only has one wall next to it

    Makes Karel climb while surrounded by walls to its left and right.
    """
    while not right_is_clear() and not left_is_clear():  # Same as `not (right_is_clear() or left_is_clear())`
        move()


def jump_to_next_wall():
    """
    Pre-condition: Karel is facing north and only has one wall next to it
    Post-condition: Karel is facing north and surrounded by two walls

    Jumps Karel to the next wall on the left if there is a beeper present on
    its current location, otherwise jumps Karel to the next wall on the left
    """
    if on_beeper():     # Jumping to the left
        turn_left()
        move()
        turn_right()
        move()
    else:               # Jumping to the right
        turn_right()
        move()
        turn_left()
        move()


def activate_ninja_karel():
    """
    Pre-condition: At the bottom of the world, facing north
    Post-condition: At the top of the world, facing north

    Makes Karel climb a series of 'spider wall' obstacles, jumping
    between different walls continuously until Karel has reached
    the finish platform at the very top.
    """
    while front_is_clear():
        climb_spider_wall()
        jump_to_next_wall()


def main():
    activate_ninja_karel()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
