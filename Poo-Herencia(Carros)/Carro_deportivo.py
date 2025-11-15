from Carro import Carro

class Carro_deportivo(Carro):
    def __init__(self, modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible)
        self.nitro_activo = False
        self.velocidad_maxima = 320

    def activar_nitro(self):
        self.nitro_activo = True
        print(f"Nitro activado en {self.modelo}! Velocidad máxima ahora: {self.velocidad_maxima + 50} km/h")

    def modo_deportivo(self):
        print(f"{self.modelo} está ahora en modo deportivo")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Tipo: Deportivo, Nitro: {self.nitro_activo }, Velocidad Máx: {self.velocidad_maxima} km/h\n")