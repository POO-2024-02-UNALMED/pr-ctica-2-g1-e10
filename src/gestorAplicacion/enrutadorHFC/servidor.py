class Servidor():
  
  _servidoresTotales=[]
  
  # CONSTRUCTOR
  def __init__(self, sede="", saturado=False, proveedor=None, coordenadas=None, indice=0, pe=0 ):
    
    # ATRIBUTOS
    self._sede=sede
    self._PORCENTAJE_EFICIENCIA=pe
    self._saturado=saturado
    self._proveedor=proveedor
    self._coordenadas=coordenadas
    self._routers=[]
    self._INDICE_SATURACION=indice
    self._FLUJO_RED_NETO=self._PORCENTAJE_EFICIENCIA*super().FLUJO_RED_PRELIMINAR
    
    if proveedor!=None :
      Servidor._servidoresTotales.append(self)
