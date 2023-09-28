class Persona:
  
 def __init__(self, name, age):
  self.name = name + "Hola"
  self.age = age

Persona1 = Persona("Alejandro",23)
Persona2 = Persona("Camilo",18)
Persona3 = Persona("Carlos",15)
Persona4 = Persona("Julian",33)

print(Persona1.age,Persona2.age,Persona3.age,Persona4.age)
print(Persona1.name,Persona2.name,Persona3.name,Persona4.name)


