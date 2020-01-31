from algorithms import *

al = algorithms()

dict1 = {"elec_result": -1, "pop_weight" : 90, "rad_bias" : 60}
dict2 = {"elec_result": -1, "pop_weight" : 50, "rad_bias" : 60}
dict3 = {"elec_result": -1, "pop_weight" : 40, "rad_bias" : 60}

list = []
list.append(dict1)
list.append(dict2)
list.append(dict3)

threshold = 100
wonCount, lostCount, a, dList = al.SimulatedElection_Harsha(list, threshold)

print(wonCount)
print(lostCount)
print(a)
print(type(dList))
