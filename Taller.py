class Persona():

    Nombre="Alejandro"
    Apellidos="Martinez"
    Edad="18"
    Cedula="101010"

Persona1 = Persona()
Persona2 = Persona()
Persona3 = Persona()


print(Persona1.Nombre)
print(Persona1.Nombre)
print(Persona1.Nombre)
print(Persona1.Apellidos)
print(Persona1.Edad)
print(Persona1.Cedula)

print(Persona2.Nombre)
print(Persona2.Apellidos)
print(Persona2.Edad)
print(Persona2.Cedula)


Persona1.Nombre = "Camilo"

print(Persona1.Nombre)

print(Persona2.Nombre)
print(Persona3.Nombre)