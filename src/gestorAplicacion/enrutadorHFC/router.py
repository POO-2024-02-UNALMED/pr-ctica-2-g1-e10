class Router(Cobertura):

    def __init__(self,up=0,down=0,online=False,servidor=None,antena=None,coordenadas=None,generacion=3):
        
        super().__init__(generacion)
        
        octeto1 = randint(100,256)
        octeto2 = randint(100,256)
        octeto3 = randint(100,256)
        octeto4 = randint(100,256)
        
        self._IP = str(octeto1) + "." + str(octeto2) + "." + str(octeto3) + "." + str(octeto4)

        self._up=up
        self._down=down
        self._online=online
        self._ping=0 
        self._coordenadas=coordenadas
        self._servidorAsociado=servidor
        self._antenaAsociada=antena
        self._velocidad=250

        if self._antenaAsociada!=None:
            self._sede=self._antenaAsociada.getSede()
            
        if self._servidorAsociado!=None:
            self._servidorAsociado.getRouters().append(self)



    def getIP(self):
        return self._IP
    
    def getUp(self):
        return self._up

    def setUp(self, up):
        self._up = up

    def getDown(self):
        return self._down
    
    def setDown(self, down):
        self._down = down
    