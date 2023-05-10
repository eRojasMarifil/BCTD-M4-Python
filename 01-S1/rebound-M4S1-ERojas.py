class Animal:
    #constructor con parametros
    def __init__ (self, nombre, raza, edad, peso) :
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
    
    def comer(self):
        print(f"E1 animal {self.nombre} esta comiendo")
    
    def caminar(self):
        print(f"El animal de raza {self.raza} esta caminando")
    
    def dormir(self):
        print(f"El animal {self .nombre} esta durmiendo")

#Definir una instancia de tipo Animal para un objeto llamado perro
perro = Animal("Brando", "San Bernardo", 3, 30)

#Definir una instancia de tipo Animal para un objeto llamado gato
gato = Animal( "Roll", "Persa",4, 3)

perro.caminar()
perro.comer()
perro.dormir()

gato.comer()
gato.caminar()
gato.dormir()