# main.py
from botella_plastico import Botella_Plastico
from botella_vidrio import Botella_Vidrio
from Botella import Botella
from Base_Datos import Base_datos

bd = Base_datos()

def menu_principal():
    print("\n--- MENÚ BOTELLAS ---")
    print("1. Crear botella de plástico")
    print("2. Crear botella de vidrio")
    print("3. Crear botella normal")
    print("4. Ver listas")
    print("5. Eliminar una botella")
    print("6. gestion de listas")
    print("7. Salir")
    return input("Elige una opción: ")

def menu_ver_listas():
    print("\n--- VER LISTAS ---")
    print("1. Ver todas las botellas")
    print("2. Ver solo botellas de plástico")
    print("3. Ver solo botellas de vidrio")
    print("4. Ver solo botellas 'normales' (material distinto)")
    print("5. Volver al menú principal")
    return input("Elige una opción: ")

def crear_botella_plastico():
    capacidad = input("Capacidad (ej: 1L): ") 
    forma = input("Forma (ej: Cilíndrica): ") 
    diseño = input("Diseño: ") 
    tapa = input("Tapa: ") 
    botella_plastico = Botella_Plastico(capacidad, forma, diseño, tapa)
    bd.agregar_botella(botella_plastico)
    print("Botella de plástico creada y registrada.")
    botella_plastico.contener_liquidos()
    botella_plastico.transparencia()
    botella_plastico.reutilizar()



def crear_botella_vidrio():
    capacidad = input("Capacidad (ej: 750ml): ") 
    forma = input("Forma (ej: Recta): ") 
    diseño = input("Diseño: ") 
    tapa = input("Tapa: ")
    botella_vidrio = Botella_Vidrio(capacidad, forma, diseño, tapa)
    bd.agregar_botella(botella_vidrio)
    print("Botella de vidrio creada y registrada.")
    botella_vidrio.contener_liquidos()
    botella_vidrio.bebidas_calientes()
    botella_vidrio.fragilidez()


def crear_botella_normal():
    material = input("Material (ej: metal, cartón, normal): ") 
    capacidad = input("Capacidad (ej: 2L): ") 
    forma = input("Forma: ") 
    diseño = input("Diseño: ") 
    tapa = input("Tapa: ") 
    botella_normal = Botella(material, capacidad, forma, diseño, tapa)
    bd.agregar_botella(botella_normal)
    print("Botella normal creada y registrada.")
    botella_normal.contener_liquidos
    botella_normal.transportar()
    botella_normal.reutilizar()     
    botella_normal.cierre_hermetico()

def ver_listas():
    while True:
        opcion = menu_ver_listas()
        if opcion == "1":
            print("--- Todas las botellas ---")
            bd.imprimir_info()
        elif opcion == "2":
            print("\n--- Botellas de plástico ---")
            bd.imprimir_info(filtro_material="plastico")
        elif opcion == "3":
            print("\n--- Botellas de vidrio ---")
            bd.imprimir_info(filtro_material="vidrio")
        elif opcion == "4":
            print("\n--- Botellas 'normales' (no plástico ni vidrio) ---")
            lista = [b for b in bd.lista_botellas if b.material.lower() not in ("plastico", "vidrio")]
            if not lista:
                print("No hay botellas de ese tipo.")
            else:
                for i, botella in enumerate(lista, start=1):
                    print(f"{i}. ", end="")
                    botella.mostrar_atributos()
        elif opcion == "5":
            break
        else:
            print("Opción no válida en Ver listas.")

def gestion_listas():
        print("\n--- GESTIÓN DE LISTAS ---")
        print("1. Copiar lista de botellas")
        print("2. Limpiar lista de botellas")
        print("3. Invertir lista de botellas")
        print("4. Volver al menú principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            copia = bd.copiar_lista()
            print("Lista copiada. Botellas en la copia:")
            for i, botella in enumerate(copia, start=1):
                print(f"{i}. ", end="")
                botella.mostrar_atributos()
        elif opcion == "2":
            bd.limpiar_lista()
            print("Lista de botellas limpiada.")
        elif opcion == "3":
            bd.invertir_lista()
            print("Lista de botellas invertida.")
        elif opcion == "4":
            return
        else:
            print("Opción no válida en Gestión de listas.")

def eliminar_botella():
    if not bd.lista_botellas:
        print("No hay botellas para eliminar.")
        return
    print("--- Eliminar botella ---")
    for i, botella in enumerate(bd.lista_botellas, start=1):
        print(f"{i}. ")
        botella.mostrar_atributos()
    try:
        indice = int(input("Ingresa el número de la botella que deseas eliminar: "))
        if 1 <= indice <= len(bd.lista_botellas):
            eliminada = bd.eliminar_por_indice(indice - 1)
            print(f"Botella eliminada")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor ingresa un número válido.")

def main():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            crear_botella_plastico()
        elif opcion == "2":
            crear_botella_vidrio()
        elif opcion == "3":
            crear_botella_normal()
        elif opcion == "4":
            ver_listas()
        elif opcion == "5":
            eliminar_botella()
        elif opcion == "6":
            gestion_listas()      
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()