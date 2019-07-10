from karel.stanfordkarel import *

def make_beeper_row_better():
    """
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
    make_beeper_row_better()


if __name__ == "__main__":
    execute_karel_task(main)