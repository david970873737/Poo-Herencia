
from Carro import Carro

class Carro_carga(Carro):
    def __init__(self, modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible)
        self.carga_actual = 0.0  
        self.capacidad_carga = 10.0  

    def cargar_mercancia(self, toneladas):
        if toneladas <= self.capacidad_carga:
            self.carga_actual = toneladas
            print(f"Se han cargado {toneladas} toneladas en {self.modelo}.")
        else:
            print(f"No se puede cargar {toneladas} toneladas. Capacidad máxima: {self.capacidad_carga}.")

    def descargar_mercancia(self):
        if self.carga_actual > 0:
            print(f"Descargando {self.carga_actual} toneladas de {self.modelo}...")
            self.carga_actual = 0
        else:
            print(f"El vehículo {self.modelo} no tiene carga.")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Tipo: Carga, Carga actual: {self.carga_actual} ton, Capacidad máxima: {self.capacidad_carga} ton\n")