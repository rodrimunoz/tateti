# Mi primer Ta-Te-Ti           
def jugar ():
    ver_tablero()
    contador_vueltas = 0
    jugador = "x"
    fin_juego = False
    while fin_juego != True:
        contador_vueltas += 1
        jugada(jugador)
        ver_tablero()
        resultado = hubo_ganador (jugador)
        if resultado == True:
            print("Jugador ", jugador, " ha ganado!")
            fin_juego = True
        else:
            jugador = "x" if jugador == "o" else "o"
        if contador_vueltas == 9:
            fin_juego = True
            print("Empate!")
                
def ver_tablero ():
    for fila in range (3):
        print(f"{tablero[3*fila]} {tablero[3*fila+1]} {tablero[3*fila+2]}     {3*fila+1}, {3*fila+2}, {3*fila+3}")

def jugada (figura):
    contador = 1
    flag = False
    ingreso = "incorrecto"
    while ingreso == "incorrecto":
        try:
            casilla = 11
            while casilla < 1 or casilla > 10:
                casilla=int(input("Ingresé el número de la casilla: "))
            ingreso = "correcto"
        except ValueError:
            print("¡Valor inválido!")
    
    for posicion in range (casilla):
        if contador == casilla and tablero[posicion] == "-":
            tablero[posicion] = figura
            flag = True
        else:
            contador = contador + 1
    if flag == False:
        print("La casilla ya está ocupada, elegí otra: ")
        jugada (figura)

def hubo_ganador (figura):
    condicion_ganador = False
    for fila in range (3):      
        if tablero[3*fila] == figura and tablero[3*fila+1] == figura and tablero[3*fila+2] == figura:
            condicion_ganador = True
    for columna in range (3):
        if tablero[columna] == figura and tablero[columna+3] == figura and tablero[columna+6] == figura:
            condicion_ganador = True
    if tablero[0] == figura and tablero[4] == figura and tablero[8] == figura:
            condicion_ganador = True
    if tablero[2] == figura and tablero[4] == figura and tablero[6] == figura:
            condicion_ganador = True
    return condicion_ganador


flag=False
contador_partidas = 1
while flag == False:
    print("""
        ***********************************
        *            - TA-TE-TI -         *
        *                                 *
        *     1. Comenzar juego           *
        *     0. Salir                    *
        *                                 *
        ***********************************

        """)

    empezar = input("Opción elegida: ")
    while empezar != "1" and empezar != "0":
        print("Ingreso inválido. intente de nuevo.")
        empezar = input("Opción elegida: ")
    if empezar == "0":
        print("Hasta luego!")
        flag = True
    else:
        tablero=["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
        jugar()