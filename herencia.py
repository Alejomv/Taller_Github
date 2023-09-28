# Clase base 'Persona'
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"


# Clase 'Empleado' que hereda de 'Persona'
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.salario = salario

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Salario: {self.salario}"


# Clase 'Estudiante' que hereda de 'Persona'
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Grado: {self.grado}"


# Clase 'Pensionado' que hereda de 'Persona'
class Pensionado(Persona):
    def __init__(self, nombre, edad, pension):
        super().__init__(nombre, edad)
        self.pension = pension

    def mostrar_datos(self):
        return f"{super().mostrar_datos()}, Pensión: {self.pension}"


# Testeando las clases
empleado = Empleado("Juan", 30, 1000)
estudiante = Estudiante("Ana", 20, "Tercero de primaria")
pensionado = Pensionado("Luis", 65, 800)

print(empleado.mostrar_datos())
print(estudiante.mostrar_datos())
print(pensionado.mostrar_datos())
