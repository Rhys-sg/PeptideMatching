from globals import *
import preCalculations
import convertArray
import solve


def main():
    counter = 0
    for i in range(NUMBEROFPEPTIDES):
        peptide = preCalculations.generatePeptide()
        presentMasses_hash = preCalculations.calculatepresentMasses_hash(peptide)
        presentMasses_arr = preCalculations.calculatepresentMasses_arr(peptide)
        subPeptides = preCalculations.generateSubPeptides(peptide)
        subPeptideMasses = sorted(preCalculations.generateSubPeptideMasses(subPeptides))

        reassembledPeptide = solve.reassemble(subPeptideMasses, presentMasses_arr, presentMasses_hash)
        if(reassembledPeptide):
            if (peptide != convertArray.toNames(reassembledPeptide) and peptide != convertArray.toNames(reassembledPeptide[::-1])):
                print(peptide)
                print(convertArray.toNames(reassembledPeptide))
                print(convertArray.toNames(reassembledPeptide)[::-1])
                counter += 1
                print()
    print(counter)
        


        
main()