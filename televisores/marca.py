class Marca:
        
    def __init__(self,nombre:str) -> None:
        self._nombre = nombre
    
    def getNombre(self) -> str:
        return self.nombre
    
    def setNombre(self,newNombre:str) -> None:
        self.nombre = newNombre
               