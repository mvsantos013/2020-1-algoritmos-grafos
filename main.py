from src.graph import DirectedGraph, UndirectedGraph

# Playground

g1 = DirectedGraph(enable_logs=True)
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
g1.show()

# g2 = UndirectedGraph()
# g2.add_vertex(1)
# g2.add_vertex(2)
# g2.add_vertex(3)
# g2.add_edge(2, 1)
# g2.add_edge(1, 2)
# g2.add_edge(1, 3)
# g2.show()

sg1 = g1.get_subjacent_graph()
sg1.show()