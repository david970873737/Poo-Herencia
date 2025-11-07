from Botella import Botella

class Botella_Plastico(Botella):
    def __init__(self, capacidad, forma, diseño, tapa):
        super().__init__("plastico",capacidad, forma, diseño, tapa)

    def reutilizar(self):
        print("Puede reutilizarse pocas veces por seguridad sanitaria.")

    def transparencia(self):
        print("El plástico es semitransparente y permite ver el contenido.")

    
       
