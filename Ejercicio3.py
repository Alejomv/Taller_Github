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

    # Validación de edad
    while True:
        edad = input("Ingrese la edad del estudiante: ")
        if edad.isdigit():
            edad = int(edad)
            break
        else:
            print("Error: los datos ingresados deben ser numéricos. Intente nuevamente.")

    # Validación de cédula
    while True:
        cedula = input("Ingrese el número de cédula del estudiante: ")
        if cedula.isdigit():
            cedula = int(cedula)
            break
        else:
            print("Error: los datos ingresados deben ser numéricos. Intente nuevamente.")
            
    carrera = input("Ingrese la carrera que el estudiante está cursando: ")

    estudiante = Estudiante(nombre, edad, cedula, carrera)

    accion = input("Ingrese una acción a realizar (estudiar/salir): ").lower()

    if accion == "estudiar":
        estudiante.estudiar()
    elif accion == "salir":
        print("Saliendo del programa")
        break
    else:
        print("Opción no reconocida. Intente nuevamente.")
