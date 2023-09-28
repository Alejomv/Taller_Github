class Estudiante:
    def __init__(self,nombre,edad,cedula,carrera):
        self.nombre = nombre
        self.edad = edad
        self.cedula =cedula
        self.carrera = carrera
    def estudiar(self):
        
        print(f"Actualmetne el estudiante {self.nombre} esta matriculado en {self.carrera}")

while True:
    
    nombre=input("Digite el nombre del estudiante: ")
    edad=input("Digite la edad del estudiante: ")
    cedula=input("Digite la Cedula del estudiante: ")
    carrera=input("Digite la Carrera del estudiante: ")
    
    estudiante = Estudiante(nombre, edad, cedula, carrera)
    
    accion=input("Desea Estudiar o salir: ").lower()
    
    
    if accion=="estudiar":
        
        
        print("\n")
        print(f"Nombre del estudiante: {nombre}")
        print(f"Edad del estudiante: {edad}")
        print(f"Carerra del estudiante: {carrera}")
        print(f"Cedula del estudiante: {cedula}")
        print("\n")
        estudiante.estudiar()
        
        break
    elif accion=="salir":
        print("\n")
        print("saliendo del programa")
    

    
    
    
   
    
    
        
        
     
    
    
    
    
    
    



    
    


    
    