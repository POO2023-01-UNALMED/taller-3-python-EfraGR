
from tv import TV

class Control:
    
    def __init__(self) -> None:
        self._tv = None
    
    def enlazar(self,televisor:TV) -> None:
        self._tv = televisor
        televisor.setControl = self
    
    
    def turnOn(self) -> None:
        self._tv.turnOn()
    
    def turnOff(self) -> None:
        self._tv.turnOff()
        
    def canalUp(self) -> None:
        self._tv.canalUp

    def canalDown(self) -> None:
        self._tv.canalDown
        
    def volumenUp(self) -> None:
        self._tv.volumenUp
    
    def volumenDown(self) -> None:
        self._tv.volumenDown
    
    
    def setCanal(self,canal:int) -> None:
        self._tv.setCanal(canal)
    
    
    def setTv(self,tv:TV) -> None:
        self._tv = TV
    def getTv(self) -> TV:
        return self._tv
    
        