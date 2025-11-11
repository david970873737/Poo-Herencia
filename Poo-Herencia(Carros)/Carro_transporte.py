from Carro import Carro

class Carro_transporte(Carro):
    def __init__(self, modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible):
        super().__init__(modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible)
        self.ruta_asignada = None
        self.pasajeros_actuales = 0

    def asignar_ruta(self, ruta):
        self.ruta_asignada = ruta
        print(f"Ruta '{ruta}' asignada al vehículo de transporte {self.modelo}.")

    def cargar_pasajeros(self, cantidad):
        if cantidad <= self.capacidad_pasajeros:
            self.pasajeros_actuales = cantidad
            print(f"{cantidad} pasajeros cargados en el vehículo {self.modelo}.")
        else:
            print("Demasiados pasajeros, excede la capacidad permitida.")

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"Tipo: Transporte, Ruta: {self.ruta_asignada}, Pasajeros actuales: {self.pasajeros_actuales}\n")