import numpy
import random
import matplotlib.pyplot as plt

def simAnnealing(startTemp: int=60, 
                 steps: int=30, 
                 tempFunc = lambda x: .90*x, 
                 cutoff:float = .1, 
                 minTempDelta: int = -10, 
                 maxTempDelta: int  = 10 ):

    temp = startTemp
    currSol = random.randint(-8,40)
    currSolEnergy = funcForTesting(currSol)
    solPoints = []
    solEnergyPoints = []

    while temp > cutoff:
        solPoints.append(currSol)
        solEnergyPoints.append(currSolEnergy)
        for x in range(0,steps):
            #print(f"==============\nOn Step {x}\nTemp: {temp}\nCurrent Sol: {currSol}\nCurrent Energy: {currSolEnergy}")
            newSol = currSol +( random.SystemRandom().random() * (maxTempDelta - minTempDelta) + minTempDelta)
            newSolEnergy = funcForTesting(newSol)
            tempPhase = False

            if(newSolEnergy < currSolEnergy):
                #print(f"Found better sol {newSol}")
                currSol = newSol
                currSolEnergy = newSolEnergy
                tempPhase = True
            else:
                acceptProb = numpy.exp(-(abs(currSolEnergy - newSolEnergy)/temp))
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

    plt.plot(range(0, len(solPoints)), solPoints)
    plt.show()
    return currSol

def funcForTesting(x: int):
    return x*(x+4)**5 + x**4 + x**3 + 20


print(simAnnealing())

