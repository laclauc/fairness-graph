import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from generate_graph import *
import sys

graph_choice = str(sys.argv[1])
print(graph_choice)

# Generate graph parameters (choose between g1--g6)
probs, sizes, nb_class, method = property_graph(graph=graph_choice)

# Generate the graph and the associated node attribute s (dictionnary)
if graph_choice == 'g6':
    g, s_all = get_graph_prot(sizes=sizes, probs=probs, number_class=nb_class,
     choice=method, nb_sens=2)

    # Compute the assortativity coefficient
    print('Assortativity coefficient wrt to the first attribute: %0.3f'%
      nx.attribute_assortativity_coefficient(g, 's'))

    # Compute the assortativity coefficient
    print('Assortativity coefficient wrt to the second attribute: %0.3f'%
      nx.attribute_assortativity_coefficient(g, 's2'))

else:
    g, s = get_graph_prot(sizes=sizes, probs=probs, number_class=nb_class,
     choice=method)
    # Compute the assortativity coefficient
    print('Assortativity coefficient: %0.3f'%
      nx.attribute_assortativity_coefficient(g, 's'))

nx.write_edgelist(g, str(sys.argv[2])+'/'+str(sys.argv[1])+'.edgelist', data=False)

print("Done!")
