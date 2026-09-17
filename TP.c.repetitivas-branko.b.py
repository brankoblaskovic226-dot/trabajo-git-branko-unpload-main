
# ============================================================
# PROGRAMACIÓN 1 - EJERCICIOS 1 AL 5
# ============================================================


# ============================================================
# EJERCICIO 1 - CAJA DEL KIOSCO
# ============================================================

print("========================================")
print("       EJERCICIO 1 - KIOSCO")
print("========================================")

nombre = input("Ingrese el nombre del cliente: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero positivo.")
    cantidad = input("Ingrese la cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(1, cantidad + 1):

    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)

    total_sin_descuentos = total_sin_descuentos + precio

    descuento = input("Descuento (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("Descuento (S/N): ")

    if descuento.lower() == "s":
        precio_final = precio * 0.90
    else:
        precio_final = precio

    total_con_descuentos = total_con_descuentos + precio_final

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print()
print("----- RESUMEN -----")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


# ============================================================
# EJERCICIO 2 - ACCESO AL CAMPUS Y MENU SEGURO
# ============================================================

print()
print("========================================")
print("    EJERCICIO 2 - ACCESO AL CAMPUS")
print("========================================")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso correcto.")
    else:
        intentos = intentos + 1
        print("Usuario o clave incorrectos.")

if not acceso:

    print("Cuenta bloqueada.")

else:

    opcion = ""

    while opcion != "4":

        print()
        print("----- MENU DEL CAMPUS -----")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error: seleccione una opción del 1 al 4.")
            opcion = input("Seleccione una opción: ")

        opcion = int(opcion)

        if opcion == 1:

            print("Inscripto")

        elif opcion == 2:

            nueva_clave = input("Ingrese la nueva clave: ")

            while len(nueva_clave) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
                nueva_clave = input("Ingrese la nueva clave: ")

            confirmacion = input("Confirme la nueva clave: ")

            while confirmacion != nueva_clave:
                print("Error: las claves no coinciden.")
                confirmacion = input("Confirme la nueva clave: ")

            clave_correcta = nueva_clave

            print("Clave cambiada correctamente.")

        elif opcion == 3:

            print("¡No te rindas, cada esfuerzo te acerca a tu objetivo!")

        elif opcion == 4:

            print("Sesión finalizada.")


# ============================================================
# EJERCICIO 3 - AGENDA DE TURNOS SIN LISTAS
# ============================================================

print()
print("========================================")
print("     EJERCICIO 3 - AGENDA DE TURNOS")
print("========================================")

operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha():
    print("Error: Solo se permiten letras.")
    operador = input("Ingrese el nombre del operador: ")


# Variables de los turnos del lunes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Variables de los turnos del martes
martes1 = ""
martes2 = ""
martes3 = ""

opcion = ""

while opcion != 5:

    print()
    print("----- MENU AGENDA -----")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: seleccione una opción del 1 al 5.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)


    # --------------------------------------------------------
    # RESERVAR TURNO
    # --------------------------------------------------------

    if opcion == 1:

        dia = input("Seleccione el día (1=Lunes / 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Seleccione el día (1=Lunes / 2=Martes): ")

        dia = int(dia)

        paciente = input("Ingrese el nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: Solo se permiten letras.")
            paciente = input("Ingrese el nombre del paciente: ")


        if dia == 1:

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno ese día.")

            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado correctamente.")

            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado correctamente.")

            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado correctamente.")

            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el lunes.")


        else:

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno ese día.")

            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado correctamente.")

            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado correctamente.")

            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado correctamente.")

            else:
                print("No hay turnos disponibles para el martes.")


    # --------------------------------------------------------
    # CANCELAR TURNO
    # --------------------------------------------------------

    elif opcion == 2:

        dia = input("Seleccione el día (1=Lunes / 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Seleccione el día (1=Lunes / 2=Martes): ")

        dia = int(dia)

        paciente = input("Ingrese el nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: Solo se permiten letras.")
            paciente = input("Ingrese el nombre del paciente: ")

        encontrado = False


        if dia == 1:

            if paciente == lunes1:
                lunes1 = ""
                encontrado = True

            elif paciente == lunes2:
                lunes2 = ""
                encontrado = True

            elif paciente == lunes3:
                lunes3 = ""
                encontrado = True

            elif paciente == lunes4:
                lunes4 = ""
                encontrado = True


        else:

            if paciente == martes1:
                martes1 = ""
                encontrado = True

            elif paciente == martes2:
                martes2 = ""
                encontrado = True

            elif paciente == martes3:
                martes3 = ""
                encontrado = True


        if encontrado:
            print("Turno cancelado correctamente.")
        else:
            print("No se encontró ese paciente.")


    # --------------------------------------------------------
    # VER AGENDA
    # --------------------------------------------------------

    elif opcion == 3:

        dia = input("Seleccione el día (1=Lunes / 2=Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Seleccione el día (1=Lunes / 2=Martes): ")

        dia = int(dia)


        if dia == 1:

            print()
            print("----- AGENDA LUNES -----")

            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")

            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")

            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")

            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")


        else:

            print()
            print("----- AGENDA MARTES -----")

            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")

            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")

            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")


    # --------------------------------------------------------
    # RESUMEN GENERAL
    # --------------------------------------------------------

    elif opcion == 4:

        ocupados_lunes = 0

        if lunes1 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes2 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes3 != "":
            ocupados_lunes = ocupados_lunes + 1

        if lunes4 != "":
            ocupados_lunes = ocupados_lunes + 1


        ocupados_martes = 0

        if martes1 != "":
            ocupados_martes = ocupados_martes + 1

        if martes2 != "":
            ocupados_martes = ocupados_martes + 1

        if martes3 != "":
            ocupados_martes = ocupados_martes + 1


        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print()
        print("----- RESUMEN GENERAL -----")
        print(f"Lunes: {ocupados_lunes} ocupados / {disponibles_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados / {disponibles_martes} disponibles")


        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")

        else:
            print("Hay empate entre Lunes y Martes.")


    elif opcion == 5:

        print("Sistema cerrado.")


# ============================================================
# EJERCICIO 4 - ESCAPE ROOM: LA BOVEDA
# ============================================================

print()
print("========================================")
print("      EJERCICIO 4 - LA BÓVEDA")
print("========================================")

agente = input("Ingrese el nombre del agente: ")

while not agente.isalpha():
    print("Error: Solo se permiten letras.")
    agente = input("Ingrese el nombre del agente: ")


energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    print()
    print("================================")
    print(f"Agente: {agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print("================================")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: seleccione una opción del 1 al 3.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)


    # --------------------------------------------------------
    # FORZAR CERRADURA
    # --------------------------------------------------------

    if opcion == 1:

        racha_forzar = racha_forzar + 1

        energia = energia - 20
        tiempo = tiempo - 2

        if racha_forzar == 3:

            print("La cerradura se trabó.")
            print("¡ALARMA ACTIVADA!")

            alarma = True

        else:

            if energia < 40:

                numero = input("Riesgo de alarma. Elija un número del 1 al 3: ")

                while not numero.isdigit() or int(numero) < 1 or int(numero) > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    numero = input("Riesgo de alarma. Elija un número del 1 al 3: ")

                numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡ALARMA ACTIVADA!")

            if not alarma:

                cerraduras_abiertas = cerraduras_abiertas + 1
                print("¡Cerradura abierta!")


    # --------------------------------------------------------
    # HACKEAR PANEL
    # --------------------------------------------------------

    elif opcion == 2:

        racha_forzar = 0

        energia = energia - 10
        tiempo = tiempo - 3

        print("Iniciando hackeo...")

        for paso in range(1, 5):

            codigo_parcial = codigo_parcial + "A"
            print(f"Paso {paso}/4 - Código: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas = cerraduras_abiertas + 1
            codigo_parcial = ""

            print("¡Hackeo exitoso!")
            print("¡Se abrió una cerradura!")


    # --------------------------------------------------------
    # DESCANSAR
    # --------------------------------------------------------

    elif opcion == 3:

        racha_forzar = 0

        energia = energia + 15

        if energia > 100:
            energia = 100

        tiempo = tiempo - 1

        if alarma:
            energia = energia - 10

        print("Has descansado.")


    # --------------------------------------------------------
    # BLOQUEO POR ALARMA
    # --------------------------------------------------------

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:

        print("La alarma se activó con poco tiempo.")
        print("SISTEMA BLOQUEADO.")
        break


# ------------------------------------------------------------
# FINAL DEL EJERCICIO 4
# ------------------------------------------------------------

print()

if cerraduras_abiertas == 3:

    print("================================")
    print("¡VICTORIA!")
    print("¡Abriste las 3 cerraduras!")
    print("================================")

elif alarma and tiempo <= 3:

    print("================================")
    print("DERROTA - BLOQUEO POR ALARMA")
    print("================================")

elif energia <= 0 or tiempo <= 0:

    print("================================")
    print("DERROTA")
    print("Te quedaste sin energía o tiempo.")
    print("================================")


# ============================================================
# EJERCICIO 5 - ESCAPE ROOM: LA ARENA DEL GLADIADOR
# ============================================================

print()
print("========================================")
print("    EJERCICIO 5 - ARENA DEL GLADIADOR")
print("========================================")

gladiador = input("Ingrese el nombre del Gladiador: ")

while not gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    gladiador = input("Ingrese el nombre del Gladiador: ")


# Estadísticas iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
daño_enemigo = 12

turno_gladiador = True
juego_activo = True


# ------------------------------------------------------------
# CICLO DE COMBATE
# ------------------------------------------------------------

while vida_jugador > 0 and vida_enemigo > 0 and juego_activo:

    print()
    print("================================")
    print(f"Gladiador: {gladiador}")
    print(f"Tu vida: {vida_jugador}")
    print(f"Vida enemigo: {vida_enemigo}")
    print(f"Pociones: {pociones}")
    print("================================")


    # --------------------------------------------------------
    # TURNO DEL GLADIADOR
    # --------------------------------------------------------

    if turno_gladiador:

        print()
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Seleccione una opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: seleccione una opción del 1 al 3.")
            opcion = input("Seleccione una opción: ")

        opcion = int(opcion)


        # ----------------------------------------------------
        # ATAQUE PESADO
        # ----------------------------------------------------

        if opcion == 1:

            if vida_enemigo < 20:

                daño = ataque_pesado * 1.5

                print("¡GOLPE CRÍTICO!")

            else:

                daño = float(ataque_pesado)

            vida_enemigo = vida_enemigo - daño

            print(f"¡Atacaste al enemigo por {daño} puntos de daño!")


        # ----------------------------------------------------
        # RÁFAGA VELOZ
        # ----------------------------------------------------

        elif opcion == 2:

            for golpe in range(3):

                vida_enemigo = vida_enemigo - 5

                print("> Golpe conectado por 5 de daño")


        # ----------------------------------------------------
        # CURAR
        # ----------------------------------------------------

        elif opcion == 3:

            if pociones > 0:

                vida_jugador = vida_jugador + 30

                if vida_jugador > 100:
                    vida_jugador = 100

                pociones = pociones - 1

                print("¡Te has curado 30 puntos de vida!")

            else:

                print("¡No quedan pociones!")


        # ----------------------------------------------------
        # CAMBIO DE TURNO
        # ----------------------------------------------------

        turno_gladiador = False


    # --------------------------------------------------------
    # TURNO DEL ENEMIGO
    # --------------------------------------------------------

    if vida_enemigo > 0 and vida_jugador > 0 and not turno_gladiador:

        vida_jugador = vida_jugador - daño_enemigo

        print(f"¡El enemigo te atacó por {daño_enemigo} puntos de daño!")

        turno_gladiador = True


# ------------------------------------------------------------
# FINAL DEL EJERCICIO 5
# ------------------------------------------------------------

print()

if vida_jugador > 0:

    print("================================")
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
    print("================================")

else:

    print("================================")
    print("DERROTA. Has caído en combate.")
    print("================================")
