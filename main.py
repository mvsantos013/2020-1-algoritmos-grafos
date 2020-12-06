from src.graph import DirectedGraph, UndirectedGraph

# Playground

g1 = DirectedGraph()
g1.add_vertex(1)
g1.add_vertex(2)
g1.add_vertex(3)
g1.add_vertex(4)
g1.add_edge(2, 1)
g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(1, 4)
g1.add_edge(3, 4)
g1.remove_vertex(3)
print(g1)

g2 = UndirectedGraph()
g2.add_vertex(1)
g2.add_vertex(2)
g2.add_vertex(3)
g2.add_edge(2, 1)
g2.add_edge(1, 2)
g2.add_edge(1, 3)
print(g2)