class Persona:
  
 def __init__(self, name, age):
  self.name = name 
  self.age = age

 def Caminar(self):
   print(f"hola soy {self.name} y estoy caminando")

 def Hablar(self):
   print(f"hola soy {self.name} y estoy hablando")
  
Persona1 = Persona("Alejandro",23)

print(Persona1.Caminar())



