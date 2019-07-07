from karel.stanfordkarel import *


def turn_right():
    """
    Makes Karel rotate 90 degrees clockwise.
    """
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """
    Makes Karel rotate 180 degrees.
    """
    turn_left()
    turn_left()


def main():
    """
    Pre-condition: Karel starts at the bottom left corner of the world,
                   facing east
    Post-condition: Karel has picked up the beeper representing "home"
    """
    # Climb over the wall
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()

    # Go to the bottom right corner (home)
    turn_left()
    move()
    pick_beeper()
    turn_around()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)