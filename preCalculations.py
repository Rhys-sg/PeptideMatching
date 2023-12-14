from globals import *
import random

def generatePeptide():
    peptide = []
    aminoAcidCount = {}
    for i in range(PEPTIDELENGTH):
        toAdd = random.choice(list(AMINOACID_NAMES.values()))
        if toAdd not in aminoAcidCount:
            aminoAcidCount[toAdd] = 1
        else:
            aminoAcidCount[toAdd] += 1
        peptide += [toAdd]

    return peptide


def calculatepresentMasses_hash(peptide):
    presentMasses_hash = {}
    for aminoAcid in peptide:
        if AMINOACID_MASS[aminoAcid] not in presentMasses_hash:
            presentMasses_hash[AMINOACID_MASS[aminoAcid]] = 1
        else:
            presentMasses_hash[AMINOACID_MASS[aminoAcid]] += 1
    return presentMasses_hash


def calculatepresentMasses_arr(peptide):
    presentMasses_arr = []
    for aminoAcid in peptide:
        presentMasses_arr += [AMINOACID_MASS[aminoAcid]]
    return sorted(presentMasses_arr)


def generateSubPeptides(peptide):
    subPeptides = []

    # calculates subpeptides from left side for length 2 to length n
    for i in range(2, PEPTIDELENGTH+1):
        subPeptides += [peptide[:i]]
    
    # calculates subpeptides from right side for length 2 to length n-1
    for i in range(1, PEPTIDELENGTH-1):
        subPeptides += [peptide[i:]]

    return subPeptides


def generateSubPeptideMasses(subPeptides):
        subPeptideMasses = []
        for segment in subPeptides:
            mass = 0
            for aminoAcid in segment:
                mass += AMINOACID_MASS[aminoAcid]
            mass = round(mass, 5)
            subPeptideMasses += [mass]
            tracker[mass] = segment # for debugging purposes
        
        return subPeptideMasses