from karel.stanfordkarel import *
def move_safely():
    if front_is_clear():
        move()

def precisely_pick():
    if on_beeper():
        pick_beeper()
        
def travel_road():
    while front_is_clear():
        move()
        
def make_beeper_road():
    while on_beeper():
        pick_beeper()
        move_safely()
        
def xuhao():
    i=0
    while i<10:
        i=10
        move_safely()
        
def make_beeper():
    while not on_beeper():
        put_beeper()
        move_safely()
    
    
        
def main():
    """DELETE THIS COMMENT AND FILL IN YOUR CODE BELOW"""
    pass


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)