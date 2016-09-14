#Written by Daniel Tyler
#Licensed under the GNU license
#Anyone is free to replicate, copy, reuse, distribute, or share this software
#Sorry for my terrible spaghetti code

import math
import random
import time

locations = {
    "Yonkers" : (5,-3),
    "Springfield" : (-13,40),
    "Long" : (-7,11),
    "Beach" : (-43,28),
    "Salem" : (-39,14),
    "Mesquite" : (13,12),
    "Memphis" : (31,-1),
    "Norwalk" : (-4,-9),
    "Las" : (17,40),
    "Cruces" : (22,22),
    "Tyler" : (4,-26),
    "Corona" : (-13,11),
    "Tempe" : (-46,9),
    "Manchester" : (-42,13),
    "Torrance" : (27,-11),
    "Toledo" : (32,7),
    "Coral" : (10,45),
    "Springs" : (-35,42) }

indexMap = [i for i in locations.keys()]

#permutations

#breed
    #mutate

#path is a list of numbers which correspond to the order in which we visit each node
def testFitness(path):
    cost = 0
    curloc = locations[indexMap[path[0]]]
    for i in path[1:]:
        nextloc = locations[indexMap[i]]
        cost += math.hypot(abs(abs(curloc[0])-abs(nextloc[0])),abs(abs(curloc[1])-abs(nextloc[1])))
        curloc = nextloc
    return cost

#"mates" permutations one and two together producing a single offspring
def mate(one,two):
    split=random.randint(1,len(one) -1)
    child=[]
    for i in range(split):
        child.append(one[i])
            
    unused = []
    for i in range(len(one)):
        if not i in child:
            unused.append(i)
    random.shuffle(unused)
                
    for i in range(split,len(two)):
        if two[i] in unused:
            unused.pop(unused.index(two[i]))
            child.append(two[i])
        else:
            child.append(unused.pop())
                
    return child

#creating the random starting population
population = []
for i in range(100):
    population.append((0,[i for i in random.sample(range(len(indexMap)),len(indexMap))]))

#change the range here to increase number of iterations
for a in range(50):
    
    temppop=population
    #print("Mating: {}".format(len(population)**2))
    for i in range(len(population)**2):
        temppop.append((0,mate(population[i%len(population)][1],population[math.floor(i/len(population))][1])))
        time.sleep(0.001) #slow the operation down a little
    population=temppop
    
    unsortedstrs = {" ".join(["{}".format(j) for j in i[1]]) for i in population} #removing any duplicates, since we're storing every permutation as an array within a tuple we need to convert the array into a string so it can be hashed
    unsortedints = [(0,[int(j) for j in i.split(" ")]) for i in unsortedstrs] #converting back to an array of tuples, with the second element of the tuple being the permutation

    #Test every member of the population for their fitness, then get the top sqrt(len(population)) of the population
    population = sorted([(testFitness(i[1]),i[1]) for i in unsortedints],key=lambda x: x[0])[:(math.floor(len(population)**(1/2.0)))] 
    
    print("Iteration {0}. Population: {1}, Top fitness: {2}, Lowest fitness: {3}".format(a+1,len(population),population[0][0],population[len(population)-1][0]))
    
#print out the most efficient order
for i in population[0][1]:
    print(indexMap[i])
