class VertexNotFound(Exception):
  ''' Throws error when a vertex is not found. '''
  def __init__(self, id):
    message = f'Vertex {id} was not found in graph. '
    super().__init__(message)
  
class EdgeNotFound(Exception):
  ''' Throws error when a edge is not found. '''
  def __init__(self, id1, id2):
    message = f'Edge from vertex {id1} to vertex {id2} was not found in graph. '
    super().__init__(message)

class VertexNeighborNotFound(Exception):
  ''' Throws error when a vertex has no neighbor. '''
  def __init__(self, id1, id2):
    message = f'Vertex {id1} has no neighbor {id2}. '
    super().__init__(message)