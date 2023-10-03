import matplotlib.pyplot as plt
import networkx as nx

g = nx.Graph()

g.add_node('1')
g.add_node('2')
g.add_node('3')
g.add_node('4')
g.add_node('5')
g.add_node('6')
g.add_node('7')

g.add_edge('1', '2')
g.add_edge('5', '3')
g.add_edge('2', '7')
g.add_edge('4', '5')
g.add_edge('6', '7')
g.add_edge('5', '2')
g.add_edge('7', '5')

nx.draw(g, node_color='r', with_labels=1)
plt.margins(0.2)
plt.show()
