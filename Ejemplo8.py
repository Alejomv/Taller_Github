class Persona :
    
    def __init__(self,name,edad):
        self.name = name
        self.edad = edad
    def caminar (self):
        print(f"hola soy {self.name} y estoy caminando actualmetne tengo {self.edad} años")          
  
        
persona1 = Persona("Alejadnro",18)
print(persona1.name)
persona1.caminar()

