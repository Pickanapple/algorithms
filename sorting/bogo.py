import random as r

def checkList(l): 
    sorted = True

    for i in range(len(l) - 1): 
        if l[i] > l[i + 1]:
            sorted = False
            break

def bogoSort(l): 
    if checkList(l): return l

    while not checkList(l): 
        r.shuffle(l)

    return l

if __name__ == "__main__": 
    l = [2, 4, 1, 3, 5, 2, 5, 3, 9]
    print(bogoSort(l))