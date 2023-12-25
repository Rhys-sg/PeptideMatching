from globals import *
import convertArray
import random

def generatePeptide():
    peptide_masses = []
    mass_frequency = {}

    for i in range(PEPTIDELENGTH):
        toAdd = random.choice(list(AMINOACID_MASS.values()))
        if toAdd not in mass_frequency:
            mass_frequency[toAdd] = 1
        else:
            mass_frequency[toAdd] += 1
        peptide_masses += [toAdd]

    peptide_names = convertArray.toNames(peptide_masses)
    present_masses = sorted(peptide_masses)
    return peptide_names, peptide_masses, mass_frequency, present_masses

# Generate a list of all subpeptide masses for a given peptide
#   considers subpeptides that start from both ends of the peptide
def generate_subpeptide_masses(peptide):
    n = len(peptide)
    
    left_sums = [round(sum(peptide[:i+1]), 5) for i in range(1, n)]
    right_sums = [round(sum(peptide[i:]), 5) for i in range(1, n-1)][::-1]

    combined_sums = merge_sorted_lists(left_sums, right_sums)

    return combined_sums

# Merge two sorted lists
def merge_sorted_lists(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Generate a random number of elements to remove (between 1 and half the length of the list)
#   Remove the selected elements from the list without replacement
def remove_random_elements(my_list):
    num_elements_to_remove = random.randint(1, len(my_list)//2)
    elements_to_remove = random.sample(my_list, num_elements_to_remove)
    my_list = [element for element in my_list if element not in elements_to_remove]

    return my_list, elements_to_remove
