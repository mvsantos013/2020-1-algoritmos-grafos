from src.exceptions import *

class Vertex(object):
    
  def __init__(self, id):
    self.id = id
    self.neighbors = {}
  
  def get_id(self):
    ''' Get vertex id. '''
    return self.id

  def add_neighbor(self, vertex):
    ''' Add neighbor to vertex. '''
    self.neighbors[vertex.get_id()] = vertex

  def remove_neighbor(self, id):
    ''' Remove neighbor with id. '''
    if not self.has_neighbor(id):
      raise VertexNeighborNotFound(self.get_id(), id)
    del self.neighbors[id]
  
  def update_neighbor(self, vertex, new_vertex):
    ''' Update neighbor. '''
    self.neighbors[new_vertex.id] = new_vertex
    if vertex.id != new_vertex.id:
      del self.neighbors[vertex.id] # Delete old reference
      
  def get_neighbors(self):
    ''' Get all neighbors. '''
    return self.neighbors.values()

  def get_neighbors_ids(self):
    ''' Get all neighbors. '''
    return list(self.neighbors.keys())
  
  def has_neighbor(self, id):
    ''' Check if has neighbor with id. '''
    return id in self.get_neighbors_ids()

  def get_degree(self):
    ''' Get vertex degree. '''
    return len(self.neighbors)
  
  def __str__(self):
    ''' To string. '''
    return f'Vertex {{id: {self.id}}}'