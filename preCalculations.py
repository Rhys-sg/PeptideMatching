from globals import *
import random

def generatePeptide():
    peptide = []
    for i in range(PEPTIDELENGTH):
        peptide += [random.choice(list(AMINOACID_NAMES.values()))]

    return peptide


def generateSubPeptides(peptide):
    subPeptides = []
    # This method generates less subpeptides than NUMBEROFSUBPEPTIDES, but works
    for i in range(NUMBEROFSUBPEPTIDES):
        pos1 = random.randint(0, PEPTIDELENGTH)
        pos2 = random.randint(0, PEPTIDELENGTH)
        if pos1 != pos2:
            subPeptides += [peptide[min(pos1, pos2): max(pos1, pos2)]]

    return subPeptides


def generateSubPeptideMasses(subPeptides):
        subPeptideMasses = []
        for segment in subPeptides:
            mass = 0
            for aminoAcid in segment:
                mass += AMINOACID_MASS[aminoAcid]
            subPeptideMasses += [mass]
            tracker[mass] = segment # for debugging purposes
        
        return subPeptideMasses