class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

estudiante1 = Estudiante("chino", "pacheco", "12345", "Ingeniería")


print("Nombre:", estudiante1.nombre)
print("Apellido:", estudiante1.apellido)
print("Carnet:", estudiante1.carnet)
print("Carrera:", estudiante1.carrera)

estudiante1.actualizar_nombre("sander")
estudiante1.actualizar_apellido("canales")
estudiante1.actualizar_carnet("67894440")
estudiante1.actualizar_carrera("Ciencias de la Computación")

print("\nAtributos actualizados:")
print("Nombre:", estudiante1.nombre)
print("Apellido:", estudiante1.apellido)
print("Carnet:", estudiante1.carnet)
print("Carrera:", estudiante1.carrera)
