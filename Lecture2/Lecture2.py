from karel.stanfordkarel import *


def move_safely():
    """
    Karel only moves forward if there is no wall in front of it.
    """
    if front_is_clear():
        move()


def travel_row():
    """
    Karel moves to the end of the current row or column until it hits a wall.
    """
    while front_is_clear():
        move()


def make_beeper_row():
    """
    Karel moves to the end of the current row or column and places beepers at every corner.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()    # Avoids the fencepost problem


def main():
    """
    The functions above teach Karel new commands, and this program
    is a space to test them. Uncomment and comment out the lines
    below to try them out.
    """
    # move_safely()             # Try me on SafeMove1.kwld, SafeMove2.kwld, and SafeMove3.kwld
    # travel_row()              # Try me on 1x8.kwld
    make_beeper_row()           # Try me on 1x8.kwld



####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)