class Estudiante:
    def __init__(self,nombre,edad,cedula,carrera):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.carrera = carrera
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta Matriculado actualmente en: {self.carrera}")
    
while True:
    nombre=input("Digite el nombre del Estudiante: ")
    #Validar la edad 
    while True:
        edad=input("Digite la edad del Estudiante: ")
        if edad.isdigit():
            edad=int(edad)
            break
        else:
            print("Escriba un valor numerico")
    #Validar la CEDULA 
    while True:
        cedula=input("Digite la cedula del estudiante: ")
        if cedula.isdigit():
            cedula=int(cedula)
            break
        else:
            print("Escriba un valor numerico")             
    
    
    carrera=input("Digite la carrera del estudiante: ")
    
    estudiante= Estudiante(nombre,edad,cedula,carrera)
    
    accion = input("Ingrese una acción a realizar (estudiar/salir): ").lower()
    
    if accion =="estudiar":
        estudiante.estudiar()
        print(f"Nombre del estudiante : {nombre}")
        print(f"cedula del estudiante : {cedula}")
        print(f"Edad del estudiante : {edad}")
        print(f"Actualmente estudia : {carrera}")
        break
        
    elif accion == "salir":
        print("Saliendo del programa")
        break
    

