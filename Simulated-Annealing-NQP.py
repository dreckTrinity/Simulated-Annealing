import random
import numpy as np
import scipy.misc as smp
from PIL import Image

def simAnnealing(initialState: int,
                 startTemp: int=30, 
                 steps: int=100, 
                 tempFunc = lambda x: .98*x, 
                 cutoff:float = .001):
    
    temp = startTemp
    currSol = initialState
    currSolEnergy = energyFunc(currSol)

    while temp > cutoff:
        for x in range(0,steps):
            newSol = tweakSol(currSol)
            newSolEnergy = energyFunc(newSol)
            tempPhase = False

            if(newSolEnergy < currSolEnergy):
                currSol = newSol
                currSolEnergy = newSolEnergy
                tempPhase = True
            else:
                acceptProb = np.exp(-(abs(currSolEnergy - newSolEnergy)/temp))
                #print(f"Change of success: {acceptProb}")
                if acceptProb > random.random():

                    currSol = newSol
                    currSolEnergy = newSolEnergy
                    tempPhase = True

            
            if tempPhase:
                temp = tempFunc(temp)
                break
        
        if not tempPhase:
            temp = tempFunc(temp)

    return currSol


def randSol(n:int=8):
    problem = [x for x in range(0,n)]

    #Random swapping from paper
    for i, x in enumerate(problem):
        swapVal = random.randint(0,n-1)
        tmp = problem[swapVal]
        problem[swapVal] = problem[i]
        problem[i] = tmp

    return problem

def tweakSol(problem):

    idxA = random.randrange(0, len(problem))
    idxB = random.randrange(0,len(problem))

    tmp = problem[idxA]
    problem[idxA] = problem[idxB]
    problem[idxB] = tmp
    return problem

def energyFunc(problem):
    energy = 0
    for i, _ in enumerate(problem):

        # Logic for calculating energy, the encoding method gives horizontal and vertical for free.
        if i == 0:
            if problem[i+1] == problem[i] + 1 or problem[i+1] == problem[i] - 1 :
                energy += 1
        elif i == len(problem) -1:
            if problem[i-1] == problem[i] + 1 or problem[i-1] == problem[i] - 1 :
                energy += 1
        else:
            if problem[i+1] == problem[i] + 1 or problem[i+1] == problem[i] - 1 :
                energy += 1
        if problem[i-1] == problem[i] + 1 or problem[i-1] == problem[i] - 1 :
                energy += 1

    return energy

def prettyItUp(res, size):
    coords = list(enumerate(res))
    #Thanks Overflow
    data = np.zeros((size,size,3), dtype=np.uint8)

    for x,y in coords:
        data[x,y] = [255,255,255]

    img = Image.fromarray(data)
    img.show("N-Queen Solution image")




size = int(input())
res = simAnnealing(randSol(size))

#This doesn't feel right... but works for larger problems without correcting params (i think?)
#Works up to 100k
#Might not solve 4X4 correctly
while energyFunc(res) != 0:
    res = simAnnealing(randSol(size))
print(res)
print(energyFunc(res))

#prettyItUp( res, size)