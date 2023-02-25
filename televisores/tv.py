# from marca import Marca
# from control import Control
class TV:
    _numTV =0
    
    def __init__(self,marca,estado:bool) -> None:
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        
        TV.setNumTV(TV.getNumTV()+1)
        
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca) -> None:
        self._marca = marca
    
    def getControl(self):
        return self._control
    
    def setControl(self, control) -> None:
        self._control = control
    
    def getPrecio(self) -> int:
        return self._precio
    
    def setPrecio(self, precio) -> None:
        self._precio = precio
    
    def getVolumen(self) -> int:
        return self._volumen
    
    def setVolumen(self, volumen) -> None:
        if (self._estado and self._volumen>=0 and self._volumen<=7):
            self._volumen = volumen
    
    def getCanal(self) -> int:
        return self._canal
    
    def setCanal(self, canal)-> None:
        if (self._estado and self._canal>=1 and self._canal<=120): 
            self._canal = canal
        
    def getEstado(self) -> bool:
        return self._estado
        
        
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    @classmethod
    def setNumTV(cls,tv):
        cls._numTV = tv
    
    
    
    def turnOff(self) -> None:
        self._estado = False
    
    def turnOn(self) -> None:
        self._estado = True


    def canalUp(self) -> None:
        if (self._estado and self._canal+1<=120):
            self._canal+=1
    
    def canalDown(self) -> None:
        if (self._estado and self._canal-1>=1):
            self._canal-=1
    
    def volumenUp(self) -> None:
        if (self._volumen and self._volumen+1<=7):
            self._volumen+=1
    
    def volumenDown(self) -> None:
        if (self._volumen and self._volumen-1>=0):
            self._volumen-=1
