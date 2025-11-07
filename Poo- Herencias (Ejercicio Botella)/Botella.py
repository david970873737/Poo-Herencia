class Botella:
    def __init__(self, material, capacidad, forma, diseño, tapa):
        self.material = material
        self.capacidad = capacidad
        self.forma = forma
        self.diseño = diseño
        self.tapa = tapa

    # metodos
    def contener_liquidos(self):
        print("Contiene liquidos.")

    def facilitar_vertido(self):
        print("Facilita el vertido del contenido.")

    def cierre_hermetico(self):
        print("Posee un cierre hermetico.")

    def transportar(self):
        print("Permite el transporte de liquidos.")

    def reutilizar(self):
        print("Puede ser reutilizada varias veces.")