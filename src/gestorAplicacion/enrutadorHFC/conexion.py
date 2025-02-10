
class Conexion():
  
  # CONSTRUCTOR
  def __init__(self,ip,up,down,online,generacion,cliente,servidor):

    # ATRIBUTOS
    self._cliente=cliente
    super().__init__(up,down,online,servidor)
