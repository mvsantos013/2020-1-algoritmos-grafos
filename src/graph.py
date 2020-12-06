from src.vertex import Vertex
from src.exceptions import *
from src.logger import Logger

class DirectedGraph(object):
  
  def __init__(self, enable_logs=False):
    self.vertices = {}
    self.directed = True
    self.logger = Logger(enabled=enable_logs)
    self.logger.log(f'{self.get_graph_type()} Graph created.')
    
  def add_vertex(self, id):
    ''' Add vertex do graph. '''
    new_vertex = Vertex(id)
    self.vertices[id] = new_vertex
    self.logger.log(f'Added vertex {id} to graph.')
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
    self.logger.log(f'Removed vertex {id} from graph.')

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
      self.logger.log(f'Graph already has edge ({id1}, {id2}).')
      return
    
    self.vertices[id1].add_neighbor(self.vertices[id2])
    self.logger.log(f'Added edge ({id1}, {id2}) to graph.')
  
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
  
  def get_graph_type(self):
    return 'Directed' if self.directed else 'Undirected'

  def get_max_degree(self):
    ''' Get max degree from graph. '''
    max_degree = 0
    for vertex in self.get_vertices():
      if vertex.get_degree() > max_degree:
        max_degree = vertex.get_degree()
    return max_degree
  
  def get_subjacent_graph(self):
    ''' Get subjacent graph '''
    graph = UndirectedGraph()
    for id in self.get_vertices_ids():
      graph.add_vertex(id)
    for edge in self.get_edges():
      graph.add_edge(edge[0], edge[1])
    return graph

  def show(self):
    ''' Show graph. '''
    vertices_ids = self.get_vertices_ids()
    vertices_ids_str = ", ".join([str(x) for x in vertices_ids])
    edges = self.get_edges()
    edges_str = ", ".join([f"({pair[0]}, {pair[1]})" for pair in edges])

    print('Showing graph info...')
    print(f'\tType: {self.get_graph_type()}')
    print(f'\tMax Degree: {self.get_max_degree()}')
    print(f'\tVertices: {vertices_ids_str}')
    print(f'\tEdges: {edges_str}')


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
      self.logger.log(f'Graph already has edge ({id1}, {id2}).')
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