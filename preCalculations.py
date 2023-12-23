from globals import *
import convertArray
import random

def generatePeptide():
    peptide_masses = []
    amino_acid_mass_frequency = {}

    for i in range(PEPTIDELENGTH):
        toAdd = random.choice(list(AMINOACID_MASS.values()))
        if toAdd not in amino_acid_mass_frequency:
            amino_acid_mass_frequency[toAdd] = 1
        else:
            amino_acid_mass_frequency[toAdd] += 1
        peptide_masses += [toAdd]

    peptide_names = convertArray.toNames(peptide_masses)
    present_amino_acid_masses = sorted(peptide_masses)
    return peptide_names, peptide_masses, amino_acid_mass_frequency, present_amino_acid_masses


def generateSubPeptides(peptide):
    n = len(peptide)
    
    left_sums = [round(sum(peptide[:i+1]), 5) for i in range(1, n)]
    right_sums = [round(sum(peptide[i:]), 5) for i in range(1, n-1)][::-1]

    combined_sums = merge_sorted_lists(left_sums, right_sums)

    return combined_sums


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