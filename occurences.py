from globals import *
import alg

# from here out, we will only be dealing in masses, no names. This is more efficient, but harder to debug
def generateAminoAcidOccurences(subPeptideMasses):

    presentCombinations = {i+1 : {} for i in range(PEPTIDELENGTH)}
    stack = subPeptideMasses.copy()
    presentCombinations[1] = occuresAlone(stack)
    presentCombinations = occurenceInMultiples(stack, presentCombinations, 3)

    return presentCombinations

    
def occuresAlone(stack):
    occurences = {}
    # tracks how many times an amino acid occurs alone
    i = 0
    while len(stack) > 0:
        if stack[i] > 186.07931:
            break
        if stack[i] not in AMINOACID_NAMES:
            i += 1
            continue

        stack[i]
        if stack[i] not in occurences:
            occurences[stack[i]] = 1
        else:
            occurences[stack[i]] += 1
        stack.pop(i)
    
    return occurences

# tracks how many times an amino acid occurs in a subpeptide with other amino acids
def occurenceInMultiples(stack, presentCombinations, largestMinimumSubpeptideLength):    
    i = 0
    memo = {}
    while len(stack) > 0 and i < len(stack) and stack[i] < 186.07931 * largestMinimumSubpeptideLength:
        if stack[i] in memo:
            combinations = memo[stack[i]]
        else:
            combinations = alg.combination_sum_float(stack[i], list(presentCombinations[1].keys()))
            memo[stack[i]] = combinations

        # no combinations found
        if len(combinations) < 1:
            i += 1
            continue

        # more than one combination found, eliminate those that do not have a known pair present
        if len(combinations) > 1:
            combinations = removeCombinations(combinations, presentCombinations)

            # if there are still more than one combination, we cannot know which one is correct, so we skip it
            if len(combinations) > 1:
                i += 1
                continue

        # only one combination found, add it to the dictionary
        if len(combinations) == 1:
            presentCombinations = addCombination(combinations, presentCombinations)
            stack.pop(i)

    return presentCombinations

def removeCombinations(combinations, presentCombinations):
    j = 0
    while j < len(combinations):

        # if the possible combination is a pair, we cannot evaluate it, so we skip it
        if len(combinations[j]) <= 2:
            j += 1
            continue
        
        # test to see if there is a known pair in the combination, if not, remove it
        flag = False
        for length in range(2, len(combinations[j])-1):
            for each in presentCombinations[length].keys():
                count = 0 
                for aminoAcid in each:
                    if aminoAcid in combinations[j]:
                        count += 1
                    if length == count: flag = True

        # if there is no known pair in the combination, remove the combination  
        if not flag:
            combinations.pop(j)
        else:
            j += 1

    return combinations

def addCombination(combinations, presentCombinations):
    # adds the amino acids as individual occurences to the dictionary
    for each in combinations[0]:
        if each in presentCombinations[1]:
            presentCombinations[1][each] += 1
        else:
            presentCombinations[1][each] = 1

    # add the combination of amino acids to the dictionary
    toAdd = tuple(combinations[0])
    if toAdd in presentCombinations[len(toAdd)]:
        presentCombinations[len(toAdd)][toAdd] += 1
    else:
        presentCombinations[len(toAdd)][toAdd] = 1
    
    return presentCombinations