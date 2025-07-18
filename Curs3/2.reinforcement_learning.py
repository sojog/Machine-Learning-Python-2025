import os 
from pprint import pprint
import random
import time

### VARIABILE
actions = ["left", "right"]
SIZE = 5
stari = list(range(SIZE))
target_position = SIZE - 1
Q = { }
current_position = 0

PENALTY = - 1
REWARD  = 5 

EPOCI = 20 # PASI CARE SA FIE RULATI


## FUNCTII
def clear_console ():
     os.system("clear") if os.name != "nt" else os.system("cls")

def draw_table(position):
    clear_console()
    for i in range(SIZE):
        if i == position:
            symbol = "X"
        elif i == target_position:
            symbol = "G"
        else:
            symbol = "_"
        print(f"[ {symbol} ]", end=" ")
    print()

draw_table(0)


for s in stari:
     inner_dict = {}
     for a in actions:
          inner_dict[a] = 0.0

     Q[s] = inner_dict

pprint(Q)



def move_agent():
    global current_position

    next_random_state = random.random()

    if next_random_state < 0.5:
        next_action = actions[0]
    else:
        next_action = actions[1]


    if current_position ==  SIZE - 2 and next_action == "right":
        Q[current_position][next_action] += REWARD
    else:
        Q[current_position][next_action] += PENALTY # sau +5 daca ajunge la final

    
    if next_action == "left" and current_position > 0:
        current_position -= 1
    elif next_action == "right" and current_position < SIZE - 1:
        current_position += 1

    draw_table(current_position)
    pprint(Q)
    print("Agentul a fost mutat la :", next_action)

# while True:
#     input()
#     move_agent()
    


for e in range(EPOCI):
    time.sleep(3)
    move_agent()



