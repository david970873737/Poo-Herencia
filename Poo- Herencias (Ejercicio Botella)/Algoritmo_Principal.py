from Botellas_plastico import Botella_Plastico
from Botellas_vidrio import Botella_Vidrio

def menu():
    print("--- MENÚ BOTELLAS ---")
    print("1. Crear botella de plástico")
    print("2. Crear botella de vidrio")
    print("3. Salir")
    opcion = input("Elige una opción: ")
    return opcion

def main():
    while True:
        opcion = menu()

        if opcion == "1":
            botella_plastico = Botella_Plastico("1L", "Cilíndrica", "Lisa", "normal")
            print("BOTELLA DE PLÁSTICO:")
            botella_plastico.contener_liquidos()
            botella_plastico.transparencia()
            botella_plastico.reutilizar()

        elif opcion == "2":
            botella_vidrio = Botella_Vidrio("750ml", "Recta", "elegante", "Corcho")
            print("BOTELLA DE VIDRIO:")
            botella_vidrio.contener_liquidos()
            botella_vidrio.bebidas_calientes()
            botella_vidrio.fragilidez()

        elif opcion == "3":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


main()