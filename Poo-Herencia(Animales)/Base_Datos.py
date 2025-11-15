class Base_Datos:
    def __init__(self):
        self.lista_animales = []

    def agregar_animal(self, animal):
        self.lista_animales.append(animal)

    def extender_lista(self, nuevos_animales):
        self.lista_animales.extend(nuevos_animales)

    def eliminar_animal_indice(self, indice):
        if  indice < len(self.lista_animales):
            return self.lista_animales.pop(indice)
        
    def copiar_lista(self):
        return self.lista_animales.copy()
    
    def invertir_lista(self):
        self.lista_animales.reverse()

    def limpiar_lista(self):
        self.lista_animales.clear()

    def mostrar_lista_animales(self, filtro_tipo =None, mostrar_indice = False):
        lista_filtrada = self.lista_animales

        if filtro_tipo:
            lista_filtrada = [ x for x  in self.lista_animales if filtro_tipo.lower() in x.__class__.__name__.lower()  ]

        if not lista_filtrada:
            print(f"No se encontraron Animales del tipo '{filtro_tipo}'.")
            return
        
        for i, animal in enumerate(lista_filtrada, start=1):
            if mostrar_indice:
                print(f"{i}")
            print(animal.mostrar_informacion())