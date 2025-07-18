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
actions = ["left", "up", "right", "down"]

SIZE = 5

AGENT_POSITION = (0, 0)
GOAL_POSITION = (SIZE-1, SIZE-1)

PENALTY = - 1
REWARD  = 10

Q = {

}


for x in range(SIZE):
    for y in range(SIZE):
        inner_dict = {}
        for act in actions:
            inner_dict[act] = 0.0
        Q[(x, y)] = inner_dict

pprint(Q)

def clear_console ():
     os.system("clear") if os.name != "nt" else os.system("cls")

def draw_table(position):
    clear_console()

    for i in range(SIZE):
        for j in range(SIZE):
            if position == (i, j):
                symbol = "X"
            elif (i, j) == GOAL_POSITION:
                symbol = "G"
            else:
                symbol = "_"
            print(f"[ {symbol} ]", end=" ")
        print()
    print()

draw_table(AGENT_POSITION)



AGENT_POSITION = (0, 0)

def move(next_action, current_position):
    next_value = list(current_position)

    if next_action == "right":
        next_value[0] = min(current_position[0] + 1, SIZE - 1)
    elif next_action == "left":
        next_value[0] = max(0, current_position[0] - 1)
    elif next_action == "down":
        next_value[1] = min(current_position[1] + 1, SIZE - 1)
    elif next_action == "up":
        next_value[1] = max(0, current_position[1] - 1)
    return tuple(next_value)



step = 0 
while AGENT_POSITION != GOAL_POSITION:
    step += 1
    sanse = random.random() 
    print("Sansele generate sunt:", sanse)
    if sanse < epsilon:
        next_action = random.choice(actions)
    else:
        next_action =  max(Q[AGENT_POSITION], key=Q[AGENT_POSITION].get)

    print("A fost aleasa actiunea:", next_action)
    # input()
    old_value = Q[AGENT_POSITION][next_action] 
    next_position = move(next_action, AGENT_POSITION)


    if next_position == GOAL_POSITION:
        POINTS = REWARD # +5
    else:
        POINTS = PENALTY # -1
    next_value = max(Q[next_position].values())
    Q[AGENT_POSITION][next_action] = old_value + learning_rate * ( POINTS + gamma * next_value - old_value) 

    AGENT_POSITION = next_position

    draw_table(AGENT_POSITION)

    print("Current Position:", AGENT_POSITION)
    print("Next Position", next_position)
    input()


    

