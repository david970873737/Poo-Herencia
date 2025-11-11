from Carro import Carro
from Carro_deportivo import Carro_deportivo
from Carro_transporte import Carro_transporte
from Carro_carga import Carro_carga
from Base_datos import Base_datos

bd = Base_datos()

def menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Crear Carro Deportivo")
    print("2. Crear Carro de Transporte")
    print("3. Crear Carro de Carga")
    print("4. Ver Listas de Vehículos")
    print("5. Eliminar Carro")
    print("6. Gestión de Listas")
    print("7. Salir del Programa")
    return input("Elige una opción: ")

def menu_listas():
    print("\n--- MENÚ DE LISTAS ---")
    print("1. Ver Todos los Vehículos")
    print("2. Ver Solo Carros Deportivos")
    print("3. Ver Solo Carros de Transporte")
    print("4. Ver Solo Carros de Carga")
    print("5. Volver al Menú Principal")
    return input("Elige una opción: ")

def menu_gestion():
    print("\n--- GESTIÓN DE LISTAS ---")
    print("1. Copiar Lista de Vehículos")
    print("2. Limpiar Lista de Vehículos")
    print("3. Invertir Lista de Vehículos")
    print("4. Volver al Menú Principal")
    return input("Elige una opción: ")

# ---- FUNCIONES ----
def crear_carro_deportivo():
    modelo = input("Modelo: ")
    motor = input("Motor: ")
    color = input("Color: ")
    n_puertas = int(input("Número de puertas: "))
    capacidad_pasajeros = int(input("Capacidad de pasajeros: ") )
    t_combustible = input("Tipo de combustible: ")

    c_deportivo = Carro_deportivo(modelo, color, motor, n_puertas, capacidad_pasajeros, t_combustible)
    bd.agregar_carro(c_deportivo)
    print("Carro deportivo creado correctamente.")
    c_deportivo.activar_nitro()
    c_deportivo.modo_deportivo()
    c_deportivo.mostrar_atributos()

def crear_carro_transporte():
    modelo = input("Modelo: ")
    motor = input("Motor: ")
    color = input("Color: ")
    n_puertas = int(input("Número de puertas: ") )
    capacidad_pasajeros = int(input("Capacidad de pasajeros: ") )
    t_combustible = input("Tipo de combustible: ") 

    c_transporte = Carro_transporte(modelo, color, motor, n_puertas, capacidad_pasajeros, t_combustible)
    bd.agregar_carro(c_transporte)
    print("Carro de transporte creado correctamente.")
    c_transporte.asignar_ruta("Ruta por defecto")
    c_transporte.cargar_pasajeros(capacidad_pasajeros)
    c_transporte.mostrar_atributos()

def crear_carro_carga():
    modelo = input("Modelo: ")
    motor = input("Motor: ")
    color = input("Color: ")
    n_puertas = int(input("Número de puertas: "))
    capacidad_pasajeros = int(input("Capacidad de pasajeros: ") )
    t_combustible = input("Tipo de combustible: ") 

    c_carga = Carro_carga(modelo, color, motor, n_puertas, capacidad_pasajeros, t_combustible)
    bd.agregar_carro(c_carga)
    print("Carro de carga creado correctamente.")
    c_carga.cargar_mercancia(1.0)
    c_carga.descargar_mercancia()
    c_carga.mostrar_atributos()

def ver_listas():
    while True:
        opcion = menu_listas()
        if opcion == "1":
            print("--- TODOS LOS VEHÍCULOS ---")
            bd.imprimir_info()
        elif opcion == "2":
            print("--- VEHÍCULOS DEPORTIVOS ---")
            bd.imprimir_info(filtro_tipo="deportivo")
        elif opcion == "3":
            print("--- VEHÍCULOS DE TRANSPORTE ---")
            bd.imprimir_info(filtro_tipo="transporte")
        elif opcion == "4":
            print("--- VEHÍCULOS DE CARGA ---")
            bd.imprimir_info(filtro_tipo="carga")
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")

def gestion_lista():
    while True:
        opcion = menu_gestion()
        if opcion == "1":
            copia = bd.copiar_lista()
            print("Lista copiada exitosamente.")
            for i, carro in enumerate(copia, start=1):
                print(f"{i}. ", end="")
                carro.mostrar_atributos()
        elif opcion == "2":
            bd.limpiar_lista()
            print("Lista limpiada exitosamente.")
        elif opcion == "3":
            bd.invertir_lista()
            print("Lista invertida exitosamente.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def eliminar_vehiculo():
    if not bd.lista_carros:
        print("No hay vehículos para eliminar.")
        return
    print("--- ELIMINAR VEHÍCULO ---")
    for i, carro in enumerate(bd.lista_carros, start=1):
        print(f"{i}. ", end="")
        carro.mostrar_atributos()
    try:
        indice = int(input("Ingresa el número del vehículo que deseas eliminar: "))
        if 1 <= indice <= len(bd.lista_carros):
            bd.eliminar_por_indice(indice - 1)
            print("Vehículo eliminado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def ejecutar_programa():
    while True:
        opcion = menu_principal()
        if opcion == "1":
            crear_carro_deportivo()
        elif opcion == "2":
            crear_carro_transporte()
        elif opcion == "3":
            crear_carro_carga()
        elif opcion == "4":
            ver_listas()
        elif opcion == "5":
            eliminar_vehiculo()
        elif opcion == "6":
            gestion_lista()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()