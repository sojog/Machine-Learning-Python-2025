import os 
from pprint import pprint
import random
import time

#### VARIABILE NOI

## Adaugare miscari random(la intamplare)
epsilon = 0.2

## Learning rate (rata de invatare)
learning_rate = 0.1 # se mai numeste alpha

## Trecut vs Viitor (importanta)
gamma = 0.9


### VARIABILE
actions = ["left", "right"]
SIZE = 10
stari = list(range(SIZE))
target_position = SIZE - 1
Q = { }
current_position = 0

PENALTY = - 1
REWARD  = 10

EPOCI = 50 # PASI CARE SA FIE RULATI


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
    print("Valoare generata random:", next_random_state)
    # input()
    if next_random_state < epsilon:
        print(f"Mai mic de {epsilon}:")
        next_action = random.choice(actions)
    else:
        print(f"Alegem valoare mai mare")
        next_action = 'left' if Q[current_position]['left'] >= Q[current_position]['right'] else 'right'
        # next_action = max(Q[current_position]['left'], Q[current_position]['right'])


    old_value = Q[current_position][next_action] 

    if next_action == "right":
        next_value = min(current_position + 1, SIZE - 1)
    else:
        next_value = max(0, current_position - 1)


    if current_position ==  SIZE - 2 and next_action == "right":
        POINTS = REWARD # +5
    else:
        POINTS = PENALTY # -1

    Q[current_position][next_action] = old_value + learning_rate * ( POINTS + gamma * next_value - old_value)


    
        

    if next_action == "left" and current_position > 0:
        current_position -= 1
    elif next_action == "right" and current_position < SIZE - 1:
        current_position += 1

    draw_table(current_position)
    pprint(Q)
    print("Agentul a fost mutat la :", next_action)

    if current_position ==  SIZE - 1: 
        print("programul trebuie sa se termine")
        stop_program()


def stop_program():
    print("Cea mai buna varianta de reinformecement learning este:")
    import sys
    sys.exit("Am terminat")
    # for i in stari
    # print()


while True:
    # input()
    # time.sleep(1)
    move_agent()
    


# for e in range(EPOCI):
#     time.sleep(1)
#     move_agent()



