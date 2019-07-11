from karel.stanfordkarel import *

def main():
    """
    Pre-condition: Karel starts at the bottom left corner of the world,
                   facing east
    Post-condition: Karel has picked up the beeper representing "home"
    """
    # FILL ME IN!
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    move()
    pick_beeper()
    
    pass


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)