# Se define una clase llamada 'Estudiante'
class Estudiante:
    # El método constructor __init__ inicializa los atributos de la clase.
    def __init__(self, nombre, edad, cedula, carrera):
        self.nombre = nombre  # Atributo para el nombre del estudiante
        self.edad = edad      # Atributo para la edad del estudiante
        self.cedula = cedula  # Atributo para la cédula del estudiante
        self.carrera = carrera  # Atributo para la carrera que estudia el estudiante

    # Método que muestra un mensaje indicando que el estudiante está estudiando una carrera.
    def estudiar(self):
        print(f"El estudiante {self.nombre} está matriculado actualmente en: {self.carrera}")

# Bucle principal del programa
while True:
    # Se solicita el nombre del estudiante al usuario
    nombre = input("Digite el nombre del Estudiante: ")

    # Bucle para validar que la edad ingresada sea numérica.
    while True:
        edad = input("Digite la edad del Estudiante: ")
        if edad.isdigit():  # Verifica si la entrada es numérica
            edad = int(edad)  # Convierte la edad a tipo int (entero)
            break
        else:
            print("Escriba un valor numérico")

    # Bucle para validar que la cédula ingresada sea numérica.
    while True:
        cedula = input("Digite la cédula del estudiante: ")
        if cedula.isdigit():
            cedula = int(cedula)
            break
        else:
            print("Escriba un valor numérico")

    # Se solicita la carrera que estudia el estudiante
    carrera = input("Digite la carrera del estudiante: ")

    # Se crea un objeto 'estudiante' de la clase 'Estudiante' con los datos proporcionados.
    estudiante = Estudiante(nombre, edad, cedula, carrera)

    # Se pregunta al usuario la acción a realizar.
    accion = input("Ingrese una acción a realizar (estudiar/salir): ").lower()

    # Si la acción es 'estudiar', se muestra información del estudiante.
    if accion == "estudiar":
        estudiante.estudiar()
        print(f"Nombre del estudiante: {nombre}")
        print(f"Cédula del estudiante: {cedula}")
        print(f"Edad del estudiante: {edad}")
        print(f"Actualmente estudia: {carrera}")
        break

    # Si la acción es 'salir', se termina el programa.
    elif accion == "salir":
        print("Saliendo del programa")
        break
