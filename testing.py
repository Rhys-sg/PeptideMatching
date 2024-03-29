from globals import *
import preCalculations
import convertArray
import solve
import time


def main():
    start = time.time()
    counter = 0
    for i in range(NUMBEROFPEPTIDES):
        print("Peptide ", i+1, " / ", NUMBEROFPEPTIDES)
        peptide_names, peptide_masses, mass_frequency, present_masses = preCalculations.generatePeptide()

        subpeptide_masses = preCalculations.generate_subpeptide_masses(peptide_masses)
        possible_reassembled_peptide_full = solve.reassemble(subpeptide_masses, present_masses)
        reassembled_peptide_full = possible_reassembled_peptide_full[0][0]


        subpeptides_missing_masses, removed = preCalculations.remove_random_elements(subpeptide_masses)
        reassembled_peptide_missing = solve.reassemble(subpeptides_missing_masses, present_masses)

        
        print("Peptide: ", peptide_names)
        print("Reassembled Peptide: ", convertArray.toNames(reassembled_peptide_full))
        print("Passed: ", (peptide_names == convertArray.toNames(reassembled_peptide_full) or peptide_names == convertArray.toNames(reassembled_peptide_full[::-1])))
        print("Removed ", len(removed), " : ", removed)
        print("Possible Reassembled Peptides")
        passed = False
        for each in reassembled_peptide_missing:
            print(convertArray.toNames(each[0]), " with missing ", each[1])
            if peptide_names == convertArray.toNames(each[0]) or peptide_names == convertArray.toNames(each[0][::-1]):
                passed = True
        print("Passed: ", passed)
        print()
        if passed:
            counter += 1
    print("total passed ", counter, " / ", NUMBEROFPEPTIDES)
    
    end = time.time()
    print("Time Elapsed: ", end - start)

main()