from karel.stanfordkarel import *


def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise
    """
    turn_left()
    turn_left()
    turn_left()


def follow_wall_on_right():
    """
    Move Karel forward so long as there
    is a wall to the right. Put a beeper on
    every intersection visited along the way.
    Leave Karel facing the same direction it started.
    """
    pass


def move_to_wall():
    """
    Move Karel forward until blocked.
    Leave a beeper on every intersection that you visit.
    Leave Karel facing in the original direction.
    """
    pass


def jump_hurdle():
    """
    Solve one hurdle, putting beepers along the way.
    Start facing north at the hurdle's west edge.
    End facing north at the start of the next hurdle.
    """
    pass


def traverse_hurdles():
    """
    Solve the sequence of hurdles.
    Start facing north at the first hurdle.
    Finish facing north at the end.
    (provided)
    """
    while front_is_clear():
        jump_hurdle()


def main():
    traverse_hurdles()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)