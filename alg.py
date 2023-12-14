from globals import *
import convertArray

def find_combinations(goal, values, tolerance=1e-5):
    result_set = set()
    _find_combinations(goal, values, [], result_set, tolerance)
    return list(result_set)

def _find_combinations(goal, remaining_values, current_combination, result_set, tolerance):
    if abs(goal) < tolerance:
        result_set.add(tuple(sorted(current_combination)))
        return
    if goal < 0 or not remaining_values:
        return

    # Include the current value in the combination
    _find_combinations(
        goal - remaining_values[0], remaining_values[1:], current_combination + [remaining_values[0]], result_set, tolerance
    )

    # Exclude the current value from the combination
    _find_combinations(goal, remaining_values[1:], current_combination, result_set, tolerance)

# # Test Case:
# goal = sum(convertArray.toMasses(['G', 'K']))
# values = convertArray.toMasses(['G', 'K', 'T', 'G', 'H', 'V', 'W', 'C'])

# combinations = find_combinations(goal, values)
# print("Combinations for goal {}: {}".format(goal, combinations))