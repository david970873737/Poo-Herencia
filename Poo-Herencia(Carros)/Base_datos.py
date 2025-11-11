
class Base_datos:
    def __init__(self):
        self.lista_carros = []

    def agregar_carro(self, carro):
        self.lista_carros.append(carro)

    def extender_lista(self, carros):
        if isinstance(carros, list):
            self.lista_carros.extend(carros)
        else:
            print("Error: el parámetro debe ser una lista de carros.")

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.lista_carros):
            return self.lista_carros.pop(indice)
        else:
            print("Índice fuera de rango.")

    def copiar_lista(self):
        return self.lista_carros.copy()

    def limpiar_lista(self):
        self.lista_carros.clear()

    def invertir_lista(self):
        self.lista_carros.reverse()

    def imprimir_info(self, filtro_tipo=None, mostrar_indice=False):
        if not self.lista_carros:
            print("No hay vehículos registrados todavía.")
            return

        lista_filtrada = self.lista_carros

        if filtro_tipo:
            lista_filtrada = [ carro for carro in self.lista_carros if filtro_tipo.lower() in carro.__class__.__name__.lower()  ]

        if not lista_filtrada:
            print(f"No se encontraron vehículos del tipo '{filtro_tipo}'.")
            return


        for i, carro in enumerate(lista_filtrada, start=1):
            if mostrar_indice:
                print(f"{i}. ", end="")
            carro.mostrar_atributos()