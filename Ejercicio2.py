class Estudiante:
    def __init__(self, nombre, edad, cedula, carrera):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando actualmente {self.carrera}")

while True:
    
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = input("Ingrese la edad del estudiante: ")
    cedula = input("Ingrese el número de cédula del estudiante: ")
    carrera = input("Ingrese la carrera que el estudiante está cursando: ")

    estudiante = Estudiante(nombre, edad, cedula, carrera)

    accion = input("Ingrese una acción a realizar (estudiar/salir): ").lower()

    if accion == "estudiar":
        estudiante.estudiar()
    elif accion == "salir":
        break
