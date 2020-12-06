from src.vertex import Vertex
from src.exceptions import *

class DirectedGraph(object):
  
  def __init__(self):
    self.vertices = {}
    self.directed = True
    
  def add_vertex(self, id):
    ''' Add vertex do graph. '''
    new_vertex = Vertex(id)
    self.vertices[id] = new_vertex
    return new_vertex
    
  def get_vertex(self, id):
    ''' Get vertex from graph. '''
    if id not in self.vertices:
      raise VertexNotFound(id)
    return self.vertices[id]
  
  def remove_vertex(self, id):
    ''' Remove vertex from graph. '''
    if not self.has_vertex(id):
      raise VertexNotFound(id)
    for vertex in self.get_vertices():
      if vertex.has_neighbor(id):
        vertex.remove_neighbor(id)
    del self.vertices[id]

  def get_vertices(self):
    ''' Get all vertices from graph. '''
    return self.vertices.values()
  
  def get_vertices_ids(self):
    ''' Get all vertices ids from graph. '''
    return self.vertices.keys()

  def add_edge(self, id1, id2):
    ''' Add edge to graph. '''
    if id1 not in self.vertices:
      raise VertexNotFound(id1)
    if id2 not in self.vertices:
      raise VertexNotFound(id2)
    if self.has_edge(id1, id2):
      print(f'Graph already has edge from {id1} to {id2}.')
      return
    
    self.vertices[id1].add_neighbor(self.vertices[id2])
  
  def get_edges(self):
    ''' Get all edges from graph. '''
    edges = []
    for vertex in self.get_vertices():
      for neighbor in vertex.get_neighbors():
        edge = (vertex.get_id(), neighbor.get_id())
        edges.append(edge)
    return edges
  
  def has_vertex(self, id):
    ''' Determines if graph already has an vertex. '''
    return id in self.get_vertices_ids()

  def has_edge(self, id1, id2):
    ''' Determines if graph already has an edge. '''
    return (id1, id2) in self.get_edges()
  
  def get_max_degree(self):
    ''' Get max degree from graph. '''
    max_degree = 0
    for vertex in self.get_vertices():
      if vertex.get_degree() > max_degree:
        max_degree = vertex.get_degree()
    return max_degree

  def __str__(self):
    ''' ToString override. '''
    vertices_ids = self.get_vertices_ids()
    vertices_ids_str = ", ".join([str(x) for x in vertices_ids])
    edges = self.get_edges()
    edges_str = ", ".join([f"({pair[0]}, {pair[1]})" for pair in edges])
    g_type = 'Directed' if self.directed else 'Undirected'
    return f'Printing Graph:\nType: {g_type}\nMax Degree: {self.get_max_degree()}\nVertices: {vertices_ids_str}\nEdges: {edges_str}\n'



class UndirectedGraph(DirectedGraph):
  def __init__(self):
    super().__init__()
    self.directed = False
  
  def add_edge(self, id1, id2):
    ''' Add edge to graph. '''
    if id1 not in self.vertices:
      raise VertexNotFound(id1)
    if id2 not in self.vertices:
      raise VertexNotFound(id2)
    if self.has_edge(id1, id2) or self.has_edge(id2, id1):
      print(f'Graph already has edge from {id1} to {id2}.')
      return
    
    self.vertices[id1].add_neighbor(self.vertices[id2])
    self.vertices[id2].add_neighbor(self.vertices[id1])
  
  def get_edges(self):
    ''' Get all edges from graph. Ignores duplicated edges. '''
    edges = []
    for vertex in self.get_vertices():
      for neighbor in vertex.get_neighbors():
        edge = (vertex.get_id(), neighbor.get_id())
        if(edge not in edges and (edge[1], edge[0]) not in edges):
          edges.append(edge)
    return edges