from globals import *
from itertools import permutations
from collections import Counter

import preCalculations

# main function for processing 
def reassemble(subpeptide_masses, present_masses):
    all_permutations = list(permutations(present_masses))
    all_permutations_masses = [preCalculations.generate_subpeptide_masses(permutation) for permutation in all_permutations]
    
    if len(subpeptide_masses) == (len(present_masses)-1)*2:
        for i in range(len(all_permutations_masses)):
            if list(all_permutations_masses[i]) == subpeptide_masses:
                return [[list(all_permutations[i]), []]]
            
        print("No match found")
        return None
    
    possible_solutions = []
    for i in range(len(all_permutations_masses)):
        results, missing = is_copy_with_missing_values(all_permutations_masses[i], subpeptide_masses)
        if results:
            possible_solutions.append([list(all_permutations[i]), missing])
    return possible_solutions



def is_copy_with_missing_values(list_a, list_b):
    missing = []
    a, b = 0, 0
    while a < len(list_a) and b < len(list_b):
        if list_a[a] == list_b[b]:
            a += 1
            b += 1
        else:
            missing.append(list_a[a])
            a += 1
    
    return b == len(list_b) and a <= len(list_a), missing