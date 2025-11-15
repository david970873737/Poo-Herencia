from Animal import Animal

class Animal_reptil(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, longitud, tipo_escamas, venenoso):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.longitud = longitud
        self.tipo_escamas = tipo_escamas
        self.venenoso = venenoso

    # Métodos

    def acechar(self):
        return f"{self.nombre} está acechando a su presa"
    
    def sumergirse(self):
        return f"{self.nombre} se está sumergiendo en el agua"
    
    def mudar_piel(self):
        return f"{self.nombre} está mudando su piel"
    
    def mostrar_informacion(self):
        info_clase_padre = super().mostrar_informacion()
        info_adicional = (
            f"Longitud: {self.longitud} metros\n"
            f"Tipo de escamas: {self.tipo_escamas}\n"
            f"Venenoso: {self.venenoso }\n"
        )
        return info_clase_padre + info_adicional