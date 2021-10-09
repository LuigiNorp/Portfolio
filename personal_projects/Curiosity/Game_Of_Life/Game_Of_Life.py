import numpy as np
import pygame
import matplotlib.pyplot as plt
import time

# CREANDO EL LIENZO DEL JUEGO
from numpy.core._multiarray_umath import ndarray

pygame.init()  # inicializando pygame
tamano = 10
ancho, alto = 1200, 600  # Estableciendo variables para ancho & alto (pantalla 1200 x 600 pixels)
pantalla = pygame.display.set_mode([ancho, alto])  # variable screen con valores: ancho=600 pixels, alto=1200 pixels
fondoPantalla = 20, 20, 20  # Estableciendo valores para color fondoPantalla
pantalla.fill(fondoPantalla)  # Fondo gris casi negro
velocidad = 0.1

nCeldasX, nCeldasY = (int(ancho/tamano), int(alto/tamano))  # Definiendo el tamaño de la retícula (X,Y), relación 2:1 para mantener la forma cuadrada

# Definiendo tamaño de celdas (Tamaño de Pantalla / No. de Celdas)
dimCelda_Ancho = int(ancho / nCeldasX)  # Definiendo el tamaño de las celdas en eje X
dimCelda_Alto = int(alto / nCeldasY)  # Definiendo el tamaño de las celdas en eje Y

estadoInicial = np.zeros((nCeldasX, nCeldasY))  # Numpy trabaja de esta manera: ( Y , X )

# Control de la ejecución del juego
pausarEjecucion = False

while True:  # Para que la pantalla se muestre de manera indefinida

    estadoActual = np.copy(estadoInicial)  # Es necesario crear una copia del estado, para que tenga en memoria
                                           # el estado anterior, y pueda usar sus datos para definir el actual

    # Limpiar la pantalla con el color de fondo
    pantalla.fill(fondoPantalla)

    # Transcurso del tiempo
    time.sleep(velocidad)

    # Registrando movimientos del teclado y del ratón

    mov = pygame.event.get()

    for event in mov:
        # Pausar el tiempo
        if pygame.key.get_pressed()[pygame.K_p] or \
        pygame.key.get_pressed()[pygame.K_0] or \
        pygame.key.get_pressed()[pygame.K_SPACE]:
            pausarEjecucion = not pausarEjecucion
        # Velocidad 1:
        elif pygame.key.get_pressed()[pygame.K_1]:
            velocidad = 0.5
        # Velocidad 2:
        elif pygame.key.get_pressed()[pygame.K_2]:
            velocidad = 0.1
        # Velocidad 3:
        elif pygame.key.get_pressed()[pygame.K_3]:
            velocidad = 0

        # Pausar ejecución al presionar cualquier tecla
        #if event.type == pygame.KEYDOWN:
            #pausarEjecucion = not pausarEjecucion

        # Se detecta si se presiona el ratón
        mouseClick = pygame.mouse.get_pressed()

                              # Matriz de mouse
        if sum(mouseClick) > 0: # (0 , 0 , 1)  si alguno da uno es porque se está haciendo clic
            posicionX, posicionY = pygame.mouse.get_pos()  # Obtener la posición en Pixels
            celX, celY = (int(np.floor(posicionX/dimCelda_Ancho))), int ((np.floor(posicionY/dimCelda_Alto)))
            estadoActual[celX, celY] = not mouseClick[2]



    # Rastreo del estado de celdas por ejes Y , X
    for y in range(0, nCeldasY):
        for x in range(0, nCeldasX):

            if not pausarEjecucion:

                # Calculando el número de vecinos
                nVecinos = estadoInicial[(x - 1) % nCeldasX, (y - 1) % nCeldasY] + \
                           estadoInicial[(x) % nCeldasX, (y - 1) % nCeldasY] + \
                           estadoInicial[(x + 1) % nCeldasX, (y - 1) % nCeldasY] + \
                           estadoInicial[(x - 1) % nCeldasX, (y) % nCeldasY] + \
                           estadoInicial[(x + 1) % nCeldasX, (y) % nCeldasY] + \
                           estadoInicial[(x - 1) % nCeldasX, (y + 1) % nCeldasY] + \
                           estadoInicial[(x) % nCeldasX, (y + 1) % nCeldasY] + \
                           estadoInicial[(x + 1) % nCeldasX, (y + 1) % nCeldasY]

                # CREANDO REGLAS BÁSICAS DEL JUEGO DE LA VIDA
                # Regla No. 1: Una célula muerta con exactamente 3 vecinas vivas, "REVIVE"
                if estadoInicial[x,y] == 0 and nVecinos == 3:
                    estadoActual[x,y] = 1

                # Regla No. 2: Una célula viva con menos de 2 (soledad) o más de 3 vecinas vivas (sobrepoblacion), "MUERE"
                elif estadoInicial[x,y] == 1 and (nVecinos < 2 or nVecinos > 3):
                    estadoActual[x,y] = 0

            # Creando poligono: se establece cada punto (rectangulo de la reticula)
            poly = [((x) * dimCelda_Ancho, y * dimCelda_Alto),
                    ((x + 1) * dimCelda_Ancho, (y) * dimCelda_Alto),
                    ((x + 1) * dimCelda_Ancho, (y + 1) * dimCelda_Alto),
                    ((x) * dimCelda_Ancho, (y + 1) * dimCelda_Alto)]

            # Crea una retícula con la función polygon, para muerta en negro y viva en blanco
            if estadoActual[x,y] == 0:
                pygame.draw.polygon(pantalla, (128, 128, 128), poly, 1)

            else:
                pygame.draw.polygon(pantalla, (255, 255, 255), poly, 0)

            # Hace lo mismo pero con rectángulo (Se ve más tosco)
            # pygame.draw.rect(screen,(255,255,255),(x*dimCell_Width,y*dimCell_Height,dimCell_Width,dimCell_Height),1)

    # Para pruebas:
    # plt.matshow(estadoActual)
    # plt.show()

    estadoInicial = np.copy(estadoActual)  # Se actualiza el estado inicial con los valores del actual,
                                           # para estar listos para una nueva iteración

    # Actualizando pantalla
    pygame.display.flip()
pass