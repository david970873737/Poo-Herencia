class Animal:
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.dieta = dieta
        self.tamaño = tamaño
        self.color = color

#metodos
    def moverse(self):
        return f"{self.nombre} se está moviendo."
    
    def reproducirse(self):
        return f"{self.nombre} se está reproduciendo."
    
    def comer(self):
        return f"{self.nombre} está comiendo {self.dieta}."
    
    def dormir(self):   
        return f"{self.nombre} está durmiendo."
    
    def instinto(self):
        return f"{self.nombre} está siguiendo sus instintos."
    
    def mostrar_informacion(self):
        info = (
            f"Nombre: {self.nombre}\n"
            f"Edad: {self.edad} años\n"
            f"Hábitat: {self.habitat}\n"
            f"Dieta: {self.dieta}\n"
            f"Tamaño: {self.tamaño}\n"
            f"Color: {self.color}\n"
        )
        return info