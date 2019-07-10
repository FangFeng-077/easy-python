from karel.stanfordkarel import *


def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise
    """
    turn_left()
    turn_left()
    turn_left()


def activate_ninja_karel():
    """
    Imbue Karel with its magical ninja skills here
    """
    pass


def main():
    activate_ninja_karel()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
