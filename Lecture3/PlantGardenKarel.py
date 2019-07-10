from karel.stanfordkarel import *


def turn_around():
    """
    Makes Karel rotate 180 degrees/
    """
    turn_left()
    turn_left()


def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise.
    """
    turn_left()
    turn_left()
    turn_left()


def plant_garden():
    """
    Pre-condition: Karel is at the bottom left corner of its world, facing north.
    Post-condition: Karel is at the top left corner of its world, facing north.

    Turns an entire world into a garden with every other row as a full row of
    seeds, represented by beepers.
    """
    place_row_and_return()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            place_row_and_return()


def come_back_west():
    """
    Pre-condition: Karel is at the far right edge of a row, facing east.
    Post-condition: Karel is at the far left edge of a row, facing west.

    Turns Karel around and brings it back to the start of a row.
    """
    turn_around()
    while front_is_clear():
        move()


def place_row_and_return():
    """
    Pre-condition: Karel is at the far left edge of a row, facing north.
    Post-condition: Karel is at the far left edge of the same row, facing
                    north.

    Fills an entire row with beepers, moving from left to right, and then
    returns and faces north.
    """
    turn_right()
    make_beeper_row_better()
    come_back_west()
    turn_right()


def make_beeper_row_better():
    """
    Pre-condition: Karel is at the far left edge of a row, facing east.
    Post-condition: Karel is at the far right edge of a row, facing east.

    Karel moves forward until it hits a wall,
    placing beepers on each intersection where there
    is not already a beeper.
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        move()
    if not on_beeper():
        put_beeper()


def main():
    """
    Karel plants a garden by placing seeds (beepers) in
    every other row. Some rows may already have seeds present.
    """
    plant_garden()



if __name__ == "__main__":
    execute_karel_task(main)