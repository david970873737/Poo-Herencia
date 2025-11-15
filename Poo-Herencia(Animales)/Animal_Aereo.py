from Animal import Animal

class Animal_Aereo(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, envergadura, tipo_plumas, tipo_pico):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.envergadura = envergadura
        self.tipo_plumas = tipo_plumas
        self.tipo_pico = tipo_pico

    # Métodos

    def volar(self):
        return f"{self.nombre} está volando con una envergadura de {self.envergadura} metros"
    
    def planear(self):
        return f"{self.nombre} está planeando en el aire"
    
    def cantar(self):
        return f"{self.nombre} está cantando melodiosamente"
    
    def mostrar_informacion(self):
        info_clase_padre = super().mostrar_informacion()
        info_adicional = (
            f"Envergadura: {self.envergadura} metros\n"
            f"Tipo de plumas: {self.tipo_plumas}\n"
            f"Tipo de pico: {self.tipo_pico}\n"
        )
        return info_clase_padre + info_adicional