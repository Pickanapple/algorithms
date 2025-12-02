import random as r

def checkList(l): 
    sorted = True

    for i in range(len(l) - 1): 
        if l[i] > l[i + 1]:
            sorted = False
            break

    return sorted

def bogoSort(l): 
    if checkList(l): return l

    while not checkList(l): 
        r.shuffle(l)

    return l

if __name__ == "__main__": 
    l = [3, 2, 1, 4]
    print(bogoSort(l))