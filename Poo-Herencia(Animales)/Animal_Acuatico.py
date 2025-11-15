from Animal import Animal

class Animal_Acuatico(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_agua, profundidad_maxima):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_agua = tipo_agua
        self.profundidad_maxima = profundidad_maxima

    # Métodos

    def nadar(self):
        return f"{self.nombre} está nadando en el agua {self.tipo_agua}"
    
    def bucear(self):
        return f"{self.nombre} está buceando a una profundidad de {self.profundidad_maxima} metros"
    
    def acechar(self):
        return f"{self.nombre} está acechando a su presa en el agua"
    
    def mostrar_informacion(self):
        info_clase_padre = super().mostrar_informacion()
        info_adicional = (
            f"tipo de agua: {self.tipo_agua}\n"
            f"Profundidad máxima: {self.profundidad_maxima} metros\n"
        )
        return info_clase_padre + info_adicional