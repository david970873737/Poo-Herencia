from Animal import Animal

class Animal_insecto(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, numero_alas, tipo_exoesqueleto, tipo_antena):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.numero_alas = numero_alas
        self.tipo_exoesqueleto = tipo_exoesqueleto
        self.tipo_antena = tipo_antena

    # Métodos

    def volar(self):
        return f"{self.nombre} está volando con sus {self.numero_alas} alas"
    
    def trepar(self):
        return f"{self.nombre} está trepando por su hábitat"
    
    def emitir_zumbido(self):
        return f"{self.nombre} está emitiendo un zumbido característico"
    
    
    def mostrar_informacion(self):
        info_clase_padre = super().mostrar_informacion()
        info_adicional = (
            f"Número de alas: {self.numero_alas}\n"
            f"Tipo de exoesqueleto: {self.tipo_exoesqueleto}\n"
            f"Tipo de antena: {self.tipo_antena}\n"
        )
        return info_clase_padre + info_adicional    