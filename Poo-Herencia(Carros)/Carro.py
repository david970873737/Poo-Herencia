class Carro:
    def __init__(self, modelo, color, motor, n_puertas, capacidad_pasajeros, tipo_combustible):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.n_puertas = n_puertas
        self.capacidad_pasajeros = capacidad_pasajeros
        self.tipo_combustible = tipo_combustible

    def encender(self):
        print(f"El carro {self.modelo} está encendido.")

    def apagar(self):
        print(f"El carro {self.modelo} se ha apagado.")

    def mostrar_atributos(self):
        print(f"Modelo: {self.modelo}, Color: {self.color}, Motor: {self.motor}, "
              f"Puertas: {self.n_puertas}, Capacidad: {self.capacidad_pasajeros}, "
              f"Combustible: {self.tipo_combustible}")