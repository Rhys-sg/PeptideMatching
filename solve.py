from globals import *

import alg

# main function for processing 
def reassemble(subPeptideMasses, presentMasses_arr, presentMasses_hash_l):
    presentMasses_hash_r = presentMasses_hash_l.copy()
    possibleCombinations_l = alg.find_combinations(subPeptideMasses[0], presentMasses_arr)


    if len(possibleCombinations_l) > 1:
        print("Not implemented yet")
        return 0,0
    
    presentMasses_hash_l[possibleCombinations_l[0][0]] -= 1
    presentMasses_hash_l[possibleCombinations_l[0][1]] -= 1

    l_mass = subPeptideMasses[0]
    l_arr = list(possibleCombinations_l[0])
    r_mass = 0
    r_arr = []


    for i in range(1, len(subPeptideMasses)):
        current = round(subPeptideMasses[i] - l_mass, 5)
        if current in presentMasses_hash_l and presentMasses_hash_l[current] > 0:
            presentMasses_hash_l[current] -= 1
            l_arr += [current]
            l_mass = subPeptideMasses[i]
            continue

        if r_mass == 0:
            possibleCombinations_r = alg.find_combinations(subPeptideMasses[i], presentMasses_arr)
            if len(possibleCombinations_r) > 1:
                print("Not implemented yet")
                return 0,0

            r_arr = list(possibleCombinations_r[0])
            r_mass = subPeptideMasses[i]
            presentMasses_hash_r[r_arr[0]] -= 1
            presentMasses_hash_r[r_arr[1]] -= 1
            r_subPeptideMasses = subPeptideMasses[:i][::-1]
        else:
            r_subPeptideMasses += [subPeptideMasses[i]]
            

    for each in r_subPeptideMasses + [subPeptideMasses[-1]]:
        current = round(each - r_mass, 5)
        if current in presentMasses_hash_r:
            presentMasses_hash_r[current] -= 1
            if presentMasses_hash_r[current] == 0:
                del presentMasses_hash_r[current]
            r_arr += [current]
            r_mass = each

    if len(l_arr) == len(r_arr):
        l_arr[:2] = r_arr[-2:][::-1]

    return l_arr, r_arr
