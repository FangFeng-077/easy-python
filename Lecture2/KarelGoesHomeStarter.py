from karel.stanfordkarel import *

def turn_right():
    turn_left()
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


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)