from karel.stanfordkarel import *

"""
File: TripleKarel.py
--------------------
Karel will paint the exterior of three buildings in a given
world.
"""

def main():
    for i in range(2):
        paint_building()
        move_to_next()
    paint_building()

# pre: Karel has a building on its left.
# post: Karel has a building on its left; and is now facing the next building.

def paint_building():
    for i in range(2):
        while left_is_blocked():
            paint_wall()
        turn_left()
        move()

    while left_is_blocked():
        paint_wall()

def paint_wall():
    put_beeper()
    move()

# pre: Karel just painted a building and is facing the next building.
# post: Karel has the next building on its left.

def move_to_next():
    while front_is_clear():
        move()
    turn_right()
    if front_is_blocked():
        turn_right()

def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
