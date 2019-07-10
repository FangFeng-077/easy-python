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


def main():
    """
    Write a function called make_beeper_row_better(), where Karel moves
    forward until it hits a wall, placing beepers on each intersection
    where there is not yet a beeper. Then call the function below and
    replace this comment with something more descriptive.

    We'll then use that function to plant a garden using top-down
    decomposition!
    """
    pass


if __name__ == "__main__":
    execute_karel_task(main)