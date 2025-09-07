from functions import *

def main():
    # Función principal del Sistema
    print("🚀 Iniciando Sistema de Parking Inteligente...")

    # Llenar el parqueo con algunos autos iniciales para pruebas
    print("📥 Generando datos iniciales...")
    for _ in range(random.randint(5, 15)):
        entrada_auto()

    mostrar_estado_parqueo()

    while True:
        try:
            mostrar_menu()
            opcion = validar_numero_entero("👉 Seleccione una opción: ", 1, 8)

            if opcion == 1:
                mostrar_estado_parqueo()
                limpiar_pantalla()

            elif opcion == 2:
                placa = obtener_placa_usuario()
                entrada_auto(placa)
                mostrar_estado_parqueo()
                limpiar_pantalla()

            elif opcion == 3:
                entrada_auto()
                mostrar_estado_parqueo()
                limpiar_pantalla()

            elif opcion == 4:
                if not placas_estacionadas:
                    print("❌ No hay autos estacionados para retirar")
                else:
                    mostrar_autos_estacionados()
                    placa = obtener_placa_usuario()
                    salida_auto(placa)
                    mostrar_estado_parqueo()
                limpiar_pantalla()

            elif opcion == 5:
                mostrar_autos_estacionados()
                limpiar_pantalla()

            elif opcion == 6:
                placa = obtener_placa_usuario()
                mostrar_historial_auto(placa)
                limpiar_pantalla()

            elif opcion == 7:
                max_entradas = CAPACIDAD_MAXIMA - espacios_ocupados
                max_salidas = len(placas_estacionadas)

                print(f"Máximo entradas posibles: {max_entradas}")
                print(f"Máximo salidas posibles: {max_salidas}")

                entradas = validar_numero_entero(
                    "Número de entradas a simular: ", 0, max_entradas)
                salidas = validar_numero_entero(
                    "Número de salidas a simular: ", 0, max_salidas)

                simular_movimientos(entradas, salidas)
                mostrar_estado_parqueo()
                limpiar_pantalla()

            elif opcion == 8:
                print("👋 ¡Gracias por usar el Sistema de Parking Inteligente!")
                break

        except KeyboardInterrupt:
            print("\n\n👋 Sistema cerrado por el usuario")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            print("El sistema continuará funcionando...")


if __name__ == "__main__":
    main()
