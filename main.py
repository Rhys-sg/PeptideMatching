import pandas as pd
import numpy as np

import convertArray
import solve

def write_to_excel(data, file_path):

    df = pd.DataFrame({'Column': data})
    df.to_excel(file_path, index=False)

def read_from_excel(file_path="Test.xlsx"):
    try:
        df = pd.read_excel(file_path)
        return list(df['Column'])

    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == "__main__":
    present_masses = [71.03711, 71.03711, 103.00919, 128.05858, 129.04259, 131.04049, 147.06841, 163.06333]
    example_data = [174.0463, 275.12699, 337.10963, 404.16958, 468.15012, 475.20669, 539.18723, 606.24718, 668.22982, 769.31051, 796.2884, 840.34762, 943.35681]


    write_to_excel(example_data, "C:/Users/rsore/Documents/GitHub/PeptideMatching/Test.xlsx")
    subpeptide_masses = read_from_excel("C:/Users/rsore/Documents/GitHub/PeptideMatching/Test.xlsx")

    
    possible_reassembled_peptide = solve.reassemble(subpeptide_masses, present_masses)
    
    print(f"{len(possible_reassembled_peptide)} Possible Peptide:")
    for each in possible_reassembled_peptide:
        print(convertArray.toNames(each[0]), " missing: ", each[1])

    
