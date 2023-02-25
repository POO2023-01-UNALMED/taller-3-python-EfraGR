class TV:
    numTV =0
    
    def __init__(self,marca:Marca,estado:bool) -> None:
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        
        TV.numTV+=1
        
    def getMarca(self) -> Marca:
        return self.marca
    
    def setMarca(self, marca) -> None:
        self.marca = marca
    
    def getControl(self) -> Control:
        return self.control
    
    def setControl(self, control) -> None:
        self.control = control
    
    def getPrecio(self) -> int:
        return self.precio
    
    def setPrecio(self, precio) -> None:
        self.precio = precio
    
    def getVolumen(self) -> int:
        return self.volumen
    
    def setVolumen(self, volumen) -> None:
        if (self._estado and self._volumen>=0 and self._volumen<=7):
            self.volumen = volumen
    
    def getCanal(self) -> int:
        return self.canal
    
    def setCanal(self, canal)-> None:
        if (self._estado and self._canal>=1 and self._canal<=120): 
            self.canal = canal
        
    def getEstado(self) -> bool:
        return self._estado
        
        
    @classmethod
    def getNumTV(cls):
        return TV.getNumTV
    
    def turnOff(self) -> None:
        self._estado = False
    
    def turnOn(self) -> None:
        self._estado = True


    def canalUp(self) -> None:
        if (self._estado and self.canal+1<=120):
            self._canal+=1
    
    def canalDown(self) -> None:
        if (self._estado and self.canal-1>=1):
            self._canal-=1
    
    def volumenUp(self) -> None:
        if (self.volumen and self.volumen+1<=7):
            self._volumen+=1
    
    def volumenDown(self) -> None:
        if (self._volumen and self.volumen-1>=0):
            self._volumen-=1
