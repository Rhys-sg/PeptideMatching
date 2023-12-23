from globals import *
import preCalculations
import convertArray
import solve


def main():
    counter = 0
    for i in range(NUMBEROFPEPTIDES):
        peptide_names, peptide_masses, amino_acid_mass_frequency, present_amino_acid_masses = preCalculations.generatePeptide()

        subPeptideMasses = preCalculations.generateSubPeptides(peptide_masses)

        reassembledPeptide, r_arr = solve.reassemble(subPeptideMasses, present_amino_acid_masses, amino_acid_mass_frequency)

        if(reassembledPeptide != 0):
            if (peptide_names != convertArray.toNames(reassembledPeptide) and peptide_names != convertArray.toNames(reassembledPeptide[::-1])):
                print(peptide_names)
                print(convertArray.toNames(reassembledPeptide))
                print(convertArray.toNames(r_arr))
                counter += 1
                print()
    print(counter)
    
main()