class Dispositivo:

  _dispositivosTotales=[]

  # CONSTRUCTOR
  def __init__(self, modem, nombre, generacion):

    # //ATRIBUTOS
    self._modem=modem
    self._nombre=nombre
    self._ipAsociada=modem.getIP()
    self._generacion=generacion
    Dispositivo._dispositivosTotales.append(self)