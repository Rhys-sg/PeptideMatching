from globals import *

import alg

# main function for processing 
def reassemble(subPeptideMasses, presentMasses_arr, presentMasses_hash):
    possibleCombinationsl = alg.find_combinations(subPeptideMasses[0], presentMasses_arr)
    if len(possibleCombinationsl) == 0:
        print("No possible combinations")
        return
    
    if len(possibleCombinationsl) > 1:
        print("Not implemented yet")
        return
    
    presentMasses_hash[possibleCombinationsl[0][0]] -= 1
    presentMasses_hash[possibleCombinationsl[0][1]] -= 1

    l_mass = sum(possibleCombinationsl[0])
    l_arr = list(possibleCombinationsl[0])
    r_mass = 0
    r_arr = []


    for i in range(1, len(subPeptideMasses)):
        current = round(subPeptideMasses[i] - l_mass, 5)
        if current in presentMasses_hash and presentMasses_hash[current] > 0:
            presentMasses_hash[current] -= 1
            l_arr += [current]
            l_mass = subPeptideMasses[i]
        else:
            r_arr += [subPeptideMasses[i] - r_mass]
            r_mass = subPeptideMasses[i]

    if l_arr[::-1] != r_arr[::-1]:
        l_arr[0], l_arr[1] = l_arr[1], l_arr[0]

    return l_arr