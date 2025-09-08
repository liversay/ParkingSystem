import datetime
import random
import os

# Variables
CAPACIDAD_MAXIMA = 100
TARIFA_POR_HORA = 2.50

espacios_ocupados = 0
placas_estacionadas = []
eventos_parking = []
historial_autos = {}

# Funciones


def calcular_porcentaje_ocupacion():
    return (espacios_ocupados / CAPACIDAD_MAXIMA) * 100


def obtener_estado_parqueo():
    porcentaje = calcular_porcentaje_ocupacion()

    if porcentaje >= 90:
        return "lleno"
    elif porcentaje >= 50:
        return "medio ocupado"
    else:
        return "disponible"


def mostrar_estado_parqueo():
    espacios_libres = CAPACIDAD_MAXIMA - espacios_ocupados
    porcentaje = calcular_porcentaje_ocupacion()
    estado = obtener_estado_parqueo()

    print(f"\n--- ESTADO DEL PARKING ---")
    print(f"Espacios ocupados: {espacios_ocupados}/{CAPACIDAD_MAXIMA}")
    print(f"Espacios libres: {espacios_libres}")
    print(f"Estado: {estado.upper()}")


def generar_placa():
    letras = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
    numeros = ''.join(random.choices('1234567890', k=3))
    return f"{letras}{numeros}"


def entrada_auto(placa=None):
    global espacios_ocupados

    if espacios_ocupados >= CAPACIDAD_MAXIMA:
        print("ERROR: El parking está lleno!")
        return False

    if placa is None:
        placa = generar_placa()

    if placa in placas_estacionadas:
        print(f"ERROR: El auto {placa} ya está estacionado!")
        return False

    # procesar entrada
    hora_entrada = datetime.datetime.now()
    espacios_ocupados += 1
    placas_estacionadas.append(placa)

    # registrar evento
    evento = (placa, hora_entrada, "ENTRADA")
    eventos_parking.append(evento)

    # actualiza historial del auto
    if placa not in historial_autos:
        historial_autos[placa] = []
    historial_autos[placa].append(evento)

    print(f"✅ Auto {placa} ingresó al parking")
    return True


def salida_auto(placa):
    global espacios_ocupados

    # Verificar que el auto esté en el parqueo
    if placa not in placas_estacionadas:
        print(f"ERROR: El auto {placa} no está en el parking!")
        return False

    # Procesar salida
    hora_salida = datetime.datetime.now()
    espacios_ocupados -= 1
    placas_estacionadas.remove(placa)

    # Calcular tarifa (simulada - 1-5 horas)
    horas_estacionado = random.uniform(1, 5)
    tarifa = horas_estacionado * TARIFA_POR_HORA

    # Registrar evento
    evento = (placa, hora_salida, f"SALIDA - ${tarifa:.2f}")
    eventos_parking.append(evento)
    historial_autos[placa].append(evento)

    print(
        f"✅ Auto {placa} salió del parking - 💵 Tarifa: ${tarifa:.2f} por {horas_estacionado:.1f} horas")
    return True


def mostrar_autos_estacionados():
    if not placas_estacionadas:
        print("\n👻 No hay autos estacionados actualmente")
        return

    print(f"\n🚗 AUTOS ESTACIONADOS ({len(placas_estacionadas)}):")
    for i, placa in enumerate(placas_estacionadas, 1):
        print(f"  {i}. {placa}")


def mostrar_historial_auto(placa):
    if placa not in historial_autos:
        print(f"❌ No se encontró historial para el auto {placa}")
        return

    print(f"\n📋 HISTORIAL DEL AUTO {placa}:")
    for evento in historial_autos[placa]:
        fecha_hora = evento[1].strftime("%Y-%m-%d %H:%M:%S")
        print(f"  • {fecha_hora} - {evento[2]}")


def simular_entradas(cantidad):
    print(f"\n🔄 Simulando {cantidad} entradas...")
    entradas_realizadas = 0

    for _ in range(cantidad):
        if espacios_ocupados < CAPACIDAD_MAXIMA:
            if entrada_auto():
                entradas_realizadas += 1
        else:
            break

    print(f"✅ Entradas completadas: {entradas_realizadas}")


def simular_salidas(cantidad):
    print(f"\n🔄 Simulando {cantidad} salidas...")
    autos_disponibles = placas_estacionadas.copy()
    salidas_realizadas = 0

    for _ in range(min(cantidad, len(autos_disponibles))):
        if autos_disponibles:
            placa_salida = random.choice(autos_disponibles)
            if salida_auto(placa_salida):
                salidas_realizadas += 1
                autos_disponibles.remove(placa_salida)

    print(f"✅ Salidas completadas: {salidas_realizadas}")


def validar_numero_entero(mensaje, minimo=0, maximo=None):
    # Valida que el usuario ingrese un número entero válido
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"❌ El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"❌ El valor debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("❌ Por favor ingrese un número válido")


def validar_placa(placa):
    # Valida el formato de una placa (ABC123)
    if len(placa) != 6:
        return False
    if not placa[:3].isalpha():
        return False
    if not placa[3:].isdigit():
        return False
    return True


def obtener_placa_usuario():
    while True:
        placa = input("Ingrese la placa (formato ABC123): ").upper()
        if validar_placa(placa):
            return placa
        else:
            print("❌ Formato de placa inválido. Use el formato ABC123")


def limpiar_pantalla():
    input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_menu():
    print("\n" + "="*50)
    print("🏎️  SISTEMA DE PARKING INTELIGENTE")
    print("="*50)
    print("1. Ver estado del parking")
    print("2. Entrada de auto (placa específica)")
    print("3. Entrada de auto (placa aleatoria)")
    print("4. Salida de auto")
    print("5. Mostrar autos estacionados")
    print("6. Ver historial de un auto")
    print("7. Simular entradas aleatorias")
    print("8. Simular salidas aleatorias")
    print("9. Salir")
    print("="*50)
