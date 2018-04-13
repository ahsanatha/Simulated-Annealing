from random import *
from math import *

def rumus (x1, x2) :
    return ((2 * (pow(x1,2)) + pow(x2,4)/3) * (pow(x1,2)))-(x1 * x2) + (4 * (pow(x2,2)) * (pow(x2,2)))
def rand () :
    return uniform(-1,1)
def key (dE, T) :
    return exp(-dE/T)

x1 = rand()
x2 = rand()

CurrentState = rumus(x1,x2)
BSF = CurrentState

Tawal = 2000000000000
Takhir = 0.000001
CoolingRate = 0.9999

while Tawal > Takhir :
    x1 = rand()
    x2 = rand()
    NewState = rumus(x1, x2)
    dE = NewState - CurrentState
    if dE < 0 :
        Bx1 = x1
        Bx2 = x2
        CurrentState = NewState
        BSF = NewState
    else:
        R = random()
        if key(dE, Tawal) > R :
            Bx1 = x1
            Bx2 = x2
            CurrentState = NewState
            BSF = NewState
    Tawal = Tawal * CoolingRate
print ("x1 = ", Bx1, "x2 = ", Bx2)
print ("BSF = ", BSF)