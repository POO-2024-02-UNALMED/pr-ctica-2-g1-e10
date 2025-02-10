class Antena():

    _antenasTotales = []
    def __init__(self, identificador, coordenadas, sede, generacion,radio, proveedor):
        # /ATRIBUTOS
        super().__init__(generacion)
        self._identificador = identificador
        self._coordenadas = coordenadas
        self._sede = sede
        self._zonaCobertura = self._coordenadas.crearZonaCobertura(self._coordenadas.getX(),self._coordenadas.getY(),radio)
        self._proveedor = proveedor
        Antena._antenasTotales.append(self)