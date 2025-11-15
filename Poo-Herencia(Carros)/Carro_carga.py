
from Carro import Carro

class Carro_carga(Carro):
    def __init__(self, modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible)
        self.carga_actual = 0.0  
        self.capacidad_carga = 10.0  

    def cargar_mercancia(self, toneladas):
        self.carga_actual = toneladas
        print(f"Se han cargado {toneladas} toneladas en {self.modelo}.")

    def descargar_mercancia(self):
            print(f"Descargando {self.carga_actual} toneladas de {self.modelo}")
            
    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Tipo: Carga, Carga actual: {self.carga_actual} ton, Capacidad máxima: {self.capacidad_carga} ton\n")