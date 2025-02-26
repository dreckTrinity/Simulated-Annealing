import numpy
import random
import matplotlib.pyplot as plt

def simAnnealing(startTemp: int=20, 
                 steps: int=200, 
                 tempFunc = lambda x: .99*x, 
                 cutoff: float = .1, 
                 minTempDelta: int = .7, 
                 maxTempDelta: int  = 1.3 ):

    temp = startTemp
    currSol = random.randint(-8,40)
    currSolEnergy = funcForTesting(currSol)
    xVals = []
    yVals = []

    while temp > cutoff:
        xVals.append(currSol)
        yVals.append(currSolEnergy)
        for x in range(0,steps):
            #print(f"On Step {x} at temp {temp}")
            newSol = currSol * random.SystemRandom().random() * (maxTempDelta - minTempDelta) + minTempDelta
            #sprint(f"New Guess of: {newSol}")
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

    plt.plot(xVals,yVals)
    return currSol

def funcForTesting(x: int):
    return x**2
    #return (x+4)**5 + x**4 + x**3 + 20


print(simAnnealing())

#plt.show()