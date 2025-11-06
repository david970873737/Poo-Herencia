from Botella import Botella

class Botella_Vidrio(Botella):
    def __init__(self, capacidad, forma, diseño, tapa):
        super().__init__( "vidrio", capacidad, forma, diseño, tapa)

    def reutilizar(self):
        print("Puede reutilizarse muchas veces, es más resistente y ecológica.")

    def bebidas_calientes(self):
        print("Puede contener bebidas calientes o frías sin deformarse.")

    def fragilidez(self):
        print("material fragil. cuidado")
              