class Estudiante:
    def __init__(self, nombre, edad, cedula, carrera):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.carrera = carrera

    def estudiar(self):
        print(f"{self.nombre} está estudiando actualmente {self.carrera}.")

def main():
    # Solicitamos la información del estudiante al usuario.
    nombre = input("Digite el nombre del estudiante: ")
    edad = input(f"Digite la edad de {nombre}: ")
    cedula = input(f"Digite la cédula de {nombre}: ")
    carrera = input(f"Digite la carrera de {nombre}: ")

    # Instanciamos un objeto de la clase Estudiante.
    estudiante = Estudiante(nombre, edad, cedula, carrera)

    while True:
        # Preguntamos al usuario la acción que desea realizar.
        accion = input("¿Qué desea hacer? (estudiar/salir): ").lower()

        if accion == "estudiar":
            estudiante.estudiar()
        elif accion == "salir":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Acción no reconocida. Intente nuevamente.")

if __name__ == "__main__":
    main()
