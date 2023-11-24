from globals import *
import itertools
from math import isclose

# Returns all combinations of numbers that add up to the target
# The same number can be used more than once,
# Does not include permutations
def combination_sum_float(target, candidates):
    def backtrack(start, remaining, path):
        if remaining < -epsilon:
            return
        if -epsilon < remaining < epsilon:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, remaining - candidates[i], path)
            path.pop()

    result = []
    candidates.sort()
    epsilon = 1e-4  # Adjust the epsilon value based on the desired precision
    backtrack(0, target, [])
    return result

# # Test usage with floats:
# target_sum = 504.16384999999997 
# input_candidates = [57.02146, 87.03203, 114.04293, 115.02694, 131.04049, 147.06841, 156.10111]
# result = combination_sum_float(target_sum, input_candidates)
# print(result)
