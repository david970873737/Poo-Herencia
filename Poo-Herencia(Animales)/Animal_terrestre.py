from Animal import Animal

class Animal_terrestre(Animal):
    def __init__(self, nombre, edad, habitat, dieta, tamaño, color, tipo_piel, numero_patas):
        super().__init__(nombre, edad, habitat, dieta, tamaño, color)
        self.tipo_piel = tipo_piel
        self.numero_patas = numero_patas

    # Métodos

    def caminar(self):
        return f"{self.nombre} está caminando sobre sus {self.numero_patas} patas"
    
    def esconderse(self):
        return f"{self.nombre} se está escondiendo en su hábitat terrestre"

    def emitir_sonido(self):
        return f"{self.nombre} está emitiendo un sonido "
    
    def mostrar_informacion(self):
        info_clase_padre = super().mostrar_informacion()
        info_adicional = (
            f"Tipo de piel: {self.tipo_piel}\n"
            f"Número de patas: {self.numero_patas}\n"
        )
        return info_clase_padre + info_adicional