from Animal import Animal
from Animal_Acuatico import Animal_Acuatico
from Animal_Aereo import Animal_Aereo
from Animal_insecto import Animal_insecto   
from Animal_reptil import Animal_reptil
from Animal_terrestre import Animal_terrestre
from Base_Datos import Base_Datos

bd = Base_Datos()

def menu_principal():
    print("\n--- Menu Animales ---")
    print("1. Crear Animal Terrestre")
    print("2. Crear Animal Acuatico")
    print("3. Crear Animal Aereo")
    print("4. Crear Animal Insecto")
    print("5. Crear Animal Reptil")
    print("6. Ver Listas")
    print("7. Eliminar Animal")
    print("8. Gestion de Listas")
    print("9. Salir del Programa")
    return input("Elige una opcion: ")

def menu_ver_listas():
    print("\n--- Menu Ver Listas ---")
    print("1. Ver Todos Los Animales")
    print("2. Ver Solo Animales Terrestre")
    print("3. Ver Solo Animales Acuaticos")
    print("4. Ver Solo Animales Aereos")
    print("5. Ver Solo Animales Insecto")
    print("6. Ver Solo Animales Reptiles")
    print("7. Volver Al Menu")
    return input("Elige una opcion: ")

def menu_gestion_listas():
    print("\n--- Gestion de Listas ---")
    print("1. Copiar lista (y mostrar copia)")
    print("2. Invertir lista")
    print("3. Limpiar lista")
    print("4. Volver al menu")
    return input("Elige una opcion: ")

def crear_animal_terrestre():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    habitat = input("Habitat: ")
    dieta = input("Dieta: ")
    tamano = input("Tamano: ")
    color = input("Color: ")
    tipo_piel = input("Tipo de Piel: ")
    numero_patas = input("Numero de Patas: ")

    a_terrestre = Animal_terrestre(nombre, edad, habitat, dieta, tamano, color, tipo_piel, numero_patas)
    bd.agregar_animal(a_terrestre)
    print("\nAnimal Terrestre Creado.")
    print(a_terrestre.caminar())
    print(a_terrestre.esconderse())
    print(a_terrestre.emitir_sonido())
    print(a_terrestre.mostrar_informacion())

def crear_animal_Acuatico():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    habitat = input("Habitat: ")
    dieta = input("Dieta: ")
    tamano = input("Tamano: ")
    color = input("Color: ")
    tipo_agua = input("Tipo de Agua: ")
    profundidad_maxima = input("Profundidad Maxima: ")

    a_acuatico= Animal_Acuatico(nombre, edad, habitat, dieta, tamano, color, tipo_agua, profundidad_maxima)
    bd.agregar_animal(a_acuatico)
    print("\nAnimal Acuatico Creado.")
    print(a_acuatico.nadar())
    print(a_acuatico.bucear())
    print(a_acuatico.acechar())
    print(a_acuatico.mostrar_informacion())

def crear_animal_aereo():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    habitat = input("Habitat: ")
    dieta = input("Dieta: ")
    tamano = input("Tamano: ")
    color = input("Color: ")
    envergadura = input("Envergadura: ")
    tipo_plumas = input("Tipo de Plumas: ")
    tipo_pico = input("Tipo de Pico: ")

    a_aereo = Animal_Aereo(nombre, edad, habitat, dieta, tamano, color, envergadura, tipo_plumas, tipo_pico)
    bd.agregar_animal(a_aereo)
    print("\nAnimal Aereo Creado.")
    print(a_aereo.volar())
    print(a_aereo.planear())
    print(a_aereo.cantar())
    print(a_aereo.mostrar_informacion())

def crear_animal_insecto():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    habitat = input("Habitat: ")
    dieta = input("Dieta: ")
    tamano = input("Tamano: ")
    color = input("Color: ")
    numero_alas = input("Numero de Alas: ")
    tipo_exoesqueleto = input("Tipo de Exoesqueleto: ")
    tipo_antena = input("Tipo de Antena: ")

    a_insecto = Animal_insecto(nombre, edad, habitat, dieta, tamano, color, numero_alas, tipo_exoesqueleto, tipo_antena)
    bd.agregar_animal(a_insecto)
    print("Animal Insecto Creado.")
    print(a_insecto.emitir_zumbido())
    print(a_insecto.volar())
    print(a_insecto.trepar())
    print(a_insecto.mostrar_informacion())

def crear_animal_reptil():
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    habitat = input("Habitat: ")
    dieta = input("Dieta: ")
    tamano = input("Tamano: ")
    color = input("Color: ")
    longitud = input("Longitud: ")
    tipo_escamas = input("Tipo de Escamas: ")
    venenoso = input("Venenoso: ")
    
    a_reptil = Animal_reptil(nombre, edad, habitat, dieta, tamano, color, longitud, tipo_escamas, venenoso)
    bd.agregar_animal(a_reptil)
    print("Animal Reptil Creado.")
    print(a_reptil.acechar())
    print(a_reptil.mudar_piel())
    print(a_reptil.sumergirse())
    print(a_reptil.mostrar_informacion())

def ver_listas():
    while True:
        opcion = menu_ver_listas()
        if opcion == "1":
            print("\n--- TODOS LOS ANIMALES ---")
            bd.mostrar_lista_animales()
        elif opcion == "2":
            print("\n--- ANIMALES TERRESTRES ---")
            bd.mostrar_lista_animales(filtro_tipo="terrestre")
        elif opcion == "3":
            print("\n--- ANIMALES ACUATICOS ---")
            bd.mostrar_lista_animales(filtro_tipo="acuatico")
        elif opcion == "4":
            print("\n--- ANIMALES AEREOS ---")
            bd.mostrar_lista_animales(filtro_tipo="aereo")
        elif opcion == "5":
            print("\n--- ANIMALES INSECTOS ---")
            bd.mostrar_lista_animales(filtro_tipo="insecto")
        elif opcion == "6":
            print("\n--- ANIMALES REPTILES ---")
            bd.mostrar_lista_animales(filtro_tipo="reptil")
        elif opcion == "7":
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

def eliminar_animal():
    if not bd.lista_animales:
        print("No hay animales para eliminar.")
    print("\n--- ELIMINAR ANIMAL ---")
    for i, animal in enumerate(bd.lista_animales, start=1):
        print(f"{i}, {animal.nombre}")
    try:
        indice = int(input("Ingresa el numero del animal que deseas eliminar: "))
        if  indice <= len(bd.lista_animales):
            eliminado = bd.eliminar_animal_indice(indice - 1)
            print(f"Animal eliminado correctamente.")
        else:
            print("Numero invalido.")
    except ValueError:
        print("Por favor ingresa un numero valido.")

def gestion_listas():
    while True:
        opcion = menu_gestion_listas()
        if opcion == "1":
            copia = bd.copiar_lista()
            if not copia:
                print("no hay lista para copiar")
            else:
                for i, animal in enumerate(copia, start=1):
                    print (f"{i}, {animal.nombre}")
                    
        elif opcion == "2":
            bd.invertir_lista()
            print("lista invertida ")
            
        elif opcion == "3":
            bd.limpiar_lista()
            print("lista limpiada")
            
        elif opcion == "4":
            break 
        else:
            print("elige una opcion valida")
                    

def ejecutar_programa():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            crear_animal_terrestre()
        elif opcion == "2":
            crear_animal_Acuatico()
        elif opcion == "3":
            crear_animal_aereo()
        elif opcion == "4":
            crear_animal_insecto()
        elif opcion == "5":
            crear_animal_reptil()
        elif opcion == "6":
            ver_listas()
        elif opcion == "7":
            eliminar_animal()
        elif opcion == "8":
            gestion_listas()
        elif opcion == "9":
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()