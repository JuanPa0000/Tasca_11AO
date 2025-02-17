import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

# Tamaño de la pantalla
ANCHO = 300
ALTO = 300
TAM_CELDA = 100

# Crear ventana
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Tres en Raya")

# Crear tablero vacío
tablero = [["" for _ in range(3)] for _ in range(3)]

# Función para dibujar el tablero
def dibujar_tablero():
    # Dibujar líneas
    for x in range(1, 3):
        pygame.draw.line(pantalla, NEGRO, (x * TAM_CELDA, 0), (x * TAM_CELDA, ALTO), 5)
        pygame.draw.line(pantalla, NEGRO, (0, x * TAM_CELDA), (ANCHO, x * TAM_CELDA), 5)

    # Dibujar símbolos en las celdas
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "X":
                pygame.draw.line(pantalla, ROJO, (j * TAM_CELDA + 20, i * TAM_CELDA + 20),
                                 (j * TAM_CELDA + TAM_CELDA - 20, i * TAM_CELDA + TAM_CELDA - 20), 5)
                pygame.draw.line(pantalla, ROJO, (j * TAM_CELDA + TAM_CELDA - 20, i * TAM_CELDA + 20),
                                 (j * TAM_CELDA + 20, i * TAM_CELDA + TAM_CELDA - 20), 5)
            elif tablero[i][j] == "O":
                pygame.draw.circle(pantalla, AZUL, (j * TAM_CELDA + TAM_CELDA // 2, i * TAM_CELDA + TAM_CELDA // 2), 40, 5)

# Función para verificar si hay un ganador
def verificar_ganador():
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] and tablero[i][0] != "":
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] and tablero[0][i] != "":
            return tablero[0][i]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != "":
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != "":
        return tablero[0][2]

    # Verificar empate
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "":
                return None
    return "Empate"

# Función para hacer un movimiento aleatorio para la máquina
def movimiento_maquina():
    celdas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ""]
    if celdas_vacias:
        i, j = random.choice(celdas_vacias)
        tablero[i][j] = "O"

# Juego principal
def juego():
    turno = "X"  # Comienza el jugador humano
    jugando = True
    while jugando:
        pantalla.fill(BLANCO)
        dibujar_tablero()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jugando = False
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if turno == "X":  # Solo el jugador humano puede hacer clic
                    x, y = pygame.mouse.get_pos()
                    fila = y // TAM_CELDA
                    col = x // TAM_CELDA
                    if tablero[fila][col] == "":
                        tablero[fila][col] = "X"
                        ganador = verificar_ganador()
                        if ganador:
                            print(f"{ganador} ha ganado!")
                            jugando = False
                        turno = "O"  # Cambiar turno

        # La máquina juega si es su turno
        if turno == "O":
            movimiento_maquina()
            ganador = verificar_ganador()
            if ganador:
                print(f"{ganador} ha ganado!")
                jugando = False
            turno = "X"  # Cambiar turno

        pygame.display.flip()
        pygame.time.Clock().tick(60)

    pygame.quit()

# Iniciar el juego
juego()
