from globals import *
from itertools import permutations
from collections import Counter

import preCalculations
import convertArray

# main function for processing 
def reassemble(subpeptide_masses, present_masses):
    all_permutations = list(permutations(present_masses))
    all_permutations_masses = [preCalculations.generate_subpeptide_masses(permutation) for permutation in all_permutations]
    
    if len(subpeptide_masses) == (len(present_masses)-1)*2:
        return no_missing_masses(all_permutations_masses, subpeptide_masses)
    
    return has_missing_masses(all_permutations, all_permutations_masses, subpeptide_masses)

# if there are no missing masses, find the permutation that matches the subpeptide masses
def no_missing_masses(all_permutations, all_permutations_masses, subpeptide_masses):
    for i in range(len(all_permutations_masses)):
        if list(all_permutations_masses[i]) == subpeptide_masses:
            return [[list(all_permutations[i]), []]]
    return None

# if there are missing masses, find all possible permutations that match the subpeptide masses
def has_missing_masses(all_permutations, all_permutations_masses, subpeptide_masses):
    possible_solutions = []
    for i in range(len(all_permutations_masses)):
        results, missing = is_copy_with_missing_values(all_permutations_masses[i], subpeptide_masses)
        if results and [list(all_permutations[i]), missing] not in possible_solutions and [list(all_permutations[i])[::-1], missing] not in possible_solutions:
            possible_solutions.append([list(all_permutations[i]), missing])
            
    return possible_solutions


# Check if list_a is a copy of list_b with some values missing, return True if so
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