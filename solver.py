#!/usr/bin/python
# -*- coding: utf-8 -*-
from _ast import NotIn


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    first_line = lines[0].split()
    node_count = int(first_line[0])
    edge_count = int(first_line[1])
    
    
    edges = []
    solution = [0]*node_count
    for i in range(1, edge_count + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    print edges
    
   
    for a in range(0,node_count):
        for b in range(0,node_count):
            if (a,b) in edges:
                solution[a] = a
                solution[b] = a +1
            else:
                solution[b] = a
         
    for i,j in edges:
        if solution[i] == solution[j]:
            solution[j] = j * 10
            
            
                     
            
    
         
    # build a trivial solution
    # every node has its own color
    
    #solution = range(0, node_count)

    # prepare the solution in the specified output format
    output_data = str(node_count) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, solution))

    return output_data


    
    



import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

