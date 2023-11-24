from globals import *

def toMasses(string):
    return [AMINOACID_MASS[each] for each in string]

def toNames(string):
    return [AMINOACID_NAMES[each] for each in string]