"""
## Pe pozitia 0
print("[ X ] [ _ ] [ _ ] [ _ ] [ G ]")
## Pe pozitia 1
print("[ _ ] [ X ] [ _ ] [ _ ] [ G ]")

"""

import os

position = 0
SIZE = 5
target_position = SIZE - 1

def draw_table():
    os.system("clear") if os.name != "nt" else os.system("cls")
    for i in range(SIZE):
        if i == position:
            symbol = "X"
        elif i == target_position:
            symbol = "G"
        else:
            symbol = "_"
        print(f"[ {symbol} ]", end=" ")
    
draw_table()

while True:
    direction = input()
    if direction == "s" and position > 0:
        position -= 1
    elif direction == "d" and position < SIZE - 1:
        position += 1
    draw_table()
