from globals import *
import preCalculations
import convertArray
import occurences
import solve


def main():
    for i in range(NUMBEROFPEPTIDES):
        # generate a random peptide, subpeptides, and subpeptide masses
        peptide = preCalculations.generatePeptide()
        subPeptides = preCalculations.generateSubPeptides(peptide)
        subPeptideMasses = sorted(preCalculations.generateSubPeptideMasses(subPeptides))

        # generate a dictionary of how many times subpeptides occur
        aminoAcidOccurences = occurences.generateAminoAcidOccurences(subPeptideMasses)

        print([convertArray.toNames(x) for x in list(aminoAcidOccurences[2].keys())])

        # reassemble the peptide
        solution = solve.reassemble(aminoAcidOccurences)

        # check if the solution is correct
        if type(solution) == str:
            print(solution)
            continue
        else:
            solution_names = convertArray.toNames(solution)
            print(peptide)
            print(solution_names)
            if peptide == solution_names or peptide == solution_names[::-1]:
                print(True)
            else:
                print(False)

main()