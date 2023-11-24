from globals import *

# main function for postprocessing 
def reassemble(aminoAcidOccurences):
    if len(aminoAcidOccurences[1].keys()) == 8:
        graph = graphStructure(aminoAcidOccurences)
        solution = solve(graph)
    else:
        solution = "error: not enough amino acid pairs"
    return solution


# returns a graph based on the pairs of amino acids, if there are more than two "ends", it will try to connect them based on larger subpeptides
def graphStructure(aminoAcidOccurences):
    graph = {}
    for pair in aminoAcidOccurences[2].keys():
        connect(pair[0], pair[1], graph)

    ends = []
    for connections in graph.keys():
        if len(graph[connections]) == 1:
            ends += [connections]

    # if there are only two ends, we can return the graph
    if len(ends) == 2:
        return graph
    
    # if there are more than two ends, we need to try connect them based on larger subpeptides
    subPeptideLength = 3
    while subPeptideLength < PEPTIDELENGTH and len(ends) > 2:
        for subpeptide in aminoAcidOccurences[subPeptideLength].keys():
            toConnect = []
            for end in ends:
                if end in subpeptide:
                    toConnect += [end]
            if len(toConnect) == 2:
                connect(toConnect[0], toConnect[1], graph)
    
    if len(ends) == 2:
        return "error: not enough amino acid pairs"
        
    return graph

# connects two nodes in a graph
def connect(a, b, graph):
    if a not in graph:
        graph[a] = {b}
    else:
        graph[a].add(b)
    
    if b not in graph:
        graph[b] = {a}
    else:
        graph[b].add(a)

# returns the one directional traversal of the graph: the reassenbled peptide
def solve(graph):
    # find the first node with only one connection
    for each in graph.keys():
        if len(graph[each]) == 1:
            solution = [each]
            break
    
    # find each next node based on the previous node
    i = 0
    while i < PEPTIDELENGTH-1:
        possibleNext = list(graph[solution[i]])
        
        if possibleNext[0] == solution[i-1]:
            next = possibleNext[1]
        else:
            next = possibleNext[0]
        solution += [next]
        i += 1
    
    return solution
