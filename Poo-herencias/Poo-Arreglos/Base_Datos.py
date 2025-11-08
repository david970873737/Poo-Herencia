class Base_datos:
    def __init__(self):
        self.lista_botellas = []

    def agregar_botella(self, botella):
        self.lista_botellas.append(botella)

    def extender_lista(self, botellas):
        self.lista_botellas.extend(botellas)

    def eliminar_por_indice(self, indice):
        if 0 <= indice < len(self.lista_botellas):
            return self.lista_botellas.pop(indice)
        return None
    
    def copiar_lista(self):
        return self.lista_botellas.copy()

    def limpiar_lista(self):
        self.lista_botellas.clear()

    def invertir_lista(self):
        self.lista_botellas.reverse()

    def imprimir_info(self, filtro_material=None):
        lista = self.lista_botellas
        if filtro_material:
            lista = [b for b in lista if b.material.lower() == filtro_material.lower()]

        if not lista:
            print("No hay botellas para mostrar con ese filtro.")
            return

        for i, botella in enumerate(lista):
            print(f"{i}. ", end="")
            botella.mostrar_atributos()