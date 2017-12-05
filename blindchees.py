from speech_recognition import SpeechRecognition
import pygame

ANCHO = 900
ALTO = 600

map_columnas = 8
map_filas = 8
white = 50
black = 50
color_fondo = [82, 82, 82]
ficha_anterior = "black"

        #   a  b  c  d  e  f  g  h
board = [   0, 1, 0, 1, 0, 1, 0, 1, # 8
            1, 0, 1, 0, 1, 0, 1, 0, # 7
            0, 1, 0, 1, 0, 1, 0, 1, # 6
            1, 0, 1, 0, 1, 0, 1, 0, # 5
            0, 1, 0, 1, 0, 1, 0, 1, # 4
            1, 0, 1, 0, 1, 0, 1, 0, # 3
            0, 1, 0, 1, 0, 1, 0, 1, # 2
            1, 0, 1, 0, 1, 0, 1, 0, # 1
            ]

'''
blacks pares
blackKing = 2 rey
blackQueen = 4 reina
blackRook = 6 torre
blackBishop = 8 alfil
blackKnight = 10 caballo
blackPawn = 12 peon

whites impares
whiteKing = 3 rey
whiteQueen = 5 reina
whiteRook = 7 torre
whiteBishop = 9 alfil
whiteKnight = 11 caballo
whitePawn = 13 peon

0 = white
1 = black
'''
        #   a  b  c  d  e  f  g  h
pieces = [  6, 10, 8, 4, 2, 8, 10, 6, # 8
            12, 12, 12, 12, 12, 12, 12, 12, # 7
            -1, -1, -1, -1, -1, -1, -1, -1, # 6
            -1, -1, -1, -1, -1, -1, -1, -1, # 5
            -1, -1, -1, -1, -1, -1, -1, -1, # 4
            -1, -1, -1, -1, -1, -1, -1, -1, # 3
            13, 13, 13, 13, 13, 13, 13, 13, # 2
            7, 11, 9, 5, 3, 9, 11, 7, # 1
            ]

# upload images
piece_white = pygame.image.load('img/white.png')
piece_black = pygame.image.load('img/gray.png')
blackKing = pygame.image.load('img/blackKing.png')
whiteKing = pygame.image.load('img/whiteKing.png')
blackQueen = pygame.image.load('img/blackQueen.png')
whiteQueen = pygame.image.load('img/whiteQueen.png')
blackRook = pygame.image.load('img/blackRook.png')
whiteRook = pygame.image.load('img/whiteRook.png')
blackBishop = pygame.image.load('img/blackBishop.png')
whiteBishop = pygame.image.load('img/whiteBishop.png')
blackKnight = pygame.image.load('img/blackKnight.png')
whiteKnight = pygame.image.load('img/whiteKnight.png')
blackPawn = pygame.image.load('img/blackPawn.png')
whitePawn = pygame.image.load('img/whitePawn.png')

posi = 0
posf = 0

# posiciones iniciles fichas
rey_black = [4]
rey_white = [60]

reina_black = [3]
reina_white = [59]

caballos_black = [1, 6]
caballos_white = [57, 62]

alfil_black = [2, 5]
alfil_white = [58, 61]

torres_black = [0, 7]
torres_white = [56, 63]

peones_black = [8, 9, 10, 11, 12, 13, 14, 15]
peones_white = [48, 49, 50, 51, 52, 53, 54, 55]

def Draw(nombre_mapa):
    inicio = x_i = y_j = 0
    y = 100
    fin = map_columnas
    for k in range(map_filas):
        x_i = 0
        fila = nombre_mapa[inicio:fin]
        for element in fila:
            x = 250 + (x_i * white)
            if element == 0:
                pantalla.blit(piece_white,(x,y))
            elif element == 1:
                pantalla.blit(piece_black,(x,y))
            elif element == 2:
                pantalla.blit(blackKing,(x,y))
            elif element == 3:
                pantalla.blit(whiteKing,(x,y))
            elif element == 4:
                pantalla.blit(blackQueen,(x,y))
            elif element == 5:
                pantalla.blit(whiteQueen,(x,y))
            elif element == 6:
                pantalla.blit(blackRook,(x,y))
            elif element == 7:
                pantalla.blit(whiteRook,(x,y))
            elif element == 8:
                pantalla.blit(blackBishop,(x,y))
            elif element == 9:
                pantalla.blit(whiteBishop,(x,y))
            elif element == 10:
                pantalla.blit(blackKnight,(x,y))
            elif element == 11:
                pantalla.blit(whiteKnight,(x,y))
            elif element == 12:
                pantalla.blit(blackPawn,(x,y))
            elif element == 13:
                pantalla.blit(whitePawn,(x,y))
            elif element == -1:
                pass
            x_i = x_i + 1
        y_j = y_j + 1
        y = 100 + (y_j * black)
        inicio = fin
        fin = fin + map_columnas

def row(pixel):
    if pixel <= 300:
        return 0
    elif pixel > 300 and pixel <= 350:
        return 1
    elif pixel > 350 and pixel <= 400:
        return 2
    elif pixel > 400 and pixel <= 450:
        return 3
    elif pixel > 450 and pixel <= 500:
        return 4
    elif pixel > 500 and pixel <= 550:
        return 5
    elif pixel > 550 and pixel <= 600:
        return 6
    elif pixel > 600:
        return 7

def column(pixel):
    if pixel <= 150:
        return 0
    elif pixel > 150 and pixel <= 200:
        return 1
    elif pixel > 200 and pixel <= 250:
        return 2
    elif pixel > 250 and pixel <= 300:
        return 3
    elif pixel > 300 and pixel <= 350:
        return 4
    elif pixel > 350 and pixel <= 400:
        return 5
    elif pixel > 400 and pixel <= 450:
        return 6
    elif pixel > 450:
        return 7

def mov_torre(posf, fichai, fichaf):
    if ficha_anterior == "black":
        arreglo = torres_white
    else:
        arreglo = torres_black
    index = -1
    for posicion in arreglo:
        index = index + 1
        if posicion + 8 == posf or posicion + 16 == posf or posicion + 24 == posf or posicion + 32 == posf or posicion + 40 == posf or posicion + 48 == posf or posicion + 56 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
        elif posicion - 8 == posf or posicion - 16 == posf or posicion - 24 == posf or posicion - 32 == posf or posicion - 40 == posf or posicion - 48 == posf or posicion - 56 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
        elif posicion >= 0 and posicion <= 7 and posf >= 0 and posf <= 7 or posicion >= 8 and posicion <= 15 and posf >= 8 and posf <= 15 or posicion >= 16 and posicion <= 23 and posf >= 16 and posf <= 23 or posicion >= 24 and posicion <= 31 and posf >= 24 and posf <= 31 or posicion >= 32 and posicion <= 39 and posf >= 32 and posf <= 39 or posicion >= 40 and posicion <= 47 and posf >= 40 and posf <= 47 or posicion >= 48 and posicion <= 55 and posf >= 48 and posf <= 55 or posicion >= 56 and posicion <= 63 and posf >= 56 and posf <= 63:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
    return False, -1

def mov_peon(posf, fichai, fichaf):
    if ficha_anterior == "black":
        arreglo = peones_white
    else:
        arreglo = peones_black
    index = -1
    for posicion in arreglo:
        index = index + 1
        if posicion >= 8 and posicion <= 15 or posicion >= 48 and posicion <= 55:
            if fichai == "black" and posicion + 8 == posf or fichai == "white" and posicion - 8 == posf or fichai == "black" and posicion + 16 == posf or fichai == "white" and posicion - 16 == posf:
                if fichaf == "none":
                    return True, index
                else:
                    return False, index
        elif fichai == "black" and posicion + 8 == posf or fichai == "white" and posicion - 8 == posf:
            if fichaf == "none":
                return True, index
        elif fichai == "black" and posicion + 9 == posf or posicion + 7 == posf:
            if fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
        elif fichai == "white" and posicion - 9 == posf or posicion - 7 == posf:
            if fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
    return False, index

def mov_alfil(posf, fichai, fichaf):
    if ficha_anterior == "black":
        arreglo = alfil_white
    else:
        arreglo = alfil_black
    index = -1
    for posicion in arreglo:
        index = index + 1
        if posicion + 9 == posf or posicion + 18 == posf or posicion + 27 == posf or posicion + 36 == posf or posicion + 45 == posf or posicion + 54 == posf or posicion + 63 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
        elif posicion - 9 == posf or posicion - 18 == posf or posicion - 27 == posf or posicion - 36 == posf or posicion - 45 == posf or posicion - 54 == posf or posicion - 63 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
        elif posicion + 7 == posf or posicion + 14 == posf or posicion + 21 == posf or posicion + 28 == posf or posicion + 35 == posf or posicion + 42 == posf or posicion + 49 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
        elif posicion - 7 == posf or posicion - 14 == posf or posicion - 21 == posf or posicion - 28 == posf or posicion - 35 == posf or posicion - 42 == posf or posi - 49 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
    return False, index

def mov_rey(posf, fichai, fichaf):
    if ficha_anterior == "black":
        arreglo = rey_white
    else:
        arreglo = rey_black
    index = -1
    for posicion in arreglo:
        index = index + 1
        if posicion + 1 == posf or posicion - 1 == posf or posicion + 8 == posf or posicion - 8 == posf or posicion - 7 == posf or posicion - 9 == posf or posicion + 7 == posf or posicion + 9 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
    return False, -1

def mov_reina(posf, fichai, fichaf):
    if ficha_anterior == "black":
        arreglo = reina_white
    else:
        arreglo = reina_black
    index = -1
    for posicion in arreglo:
        index = index + 1
        if posicion + 1 == posf or posicion - 1 == posf or posicion + 8 == posf or posicion - 8 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion + 9 == posf or posicion + 18 == posf or posicion + 27 == posf or posicion + 36 == posf or posicion + 45 == posf or posicion + 54 == posf or posicion + 63 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion - 9 == posf or posicion - 18 == posf or posicion - 27 == posf or posicion - 36 == posf or posicion - 45 == posf or posicion - 54 == posf or posicion - 63 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion + 7 == posf or posicion + 14 == posf or posicion + 21 == posf or posicion + 28 == posf or posicion + 35 == posf or posicion + 42 == posf or posicion + 49 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion - 7 == posf or posicion - 14 == posf or posicion - 21 == posf or posicion - 28 == posf or posicion - 35 == posf or posicion - 42 == posf or posicion - 49 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion + 8 == posf or posicion + 16 == posf or posicion + 24 == posf or posicion + 32 == posf or posicion + 40 == posf or posicion + 48 == posf or posicion + 56 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion - 8 == posf or posicion - 16 == posf or posicion - 24 == posf or posicion - 32 == posf or posicion - 40 == posf or posicion - 48 == posf or posicion - 56 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
        elif posicion >= 0 and posicion <= 7 and posf >= 0 and posf <= 7 or posicion >= 8 and posicion <= 15 and posf >= 8 and posf <= 15 or posicion >= 16 and posicion <= 23 and posf >= 16 and posf <= 23 or posicion >= 24 and posicion <= 31 and posf >= 24 and posf <= 31 or posicion >= 32 and posicion <= 39 and posf >= 32 and posf <= 39 or posicion >= 40 and posicion <= 47 and posf >= 40 and posf <= 47 or posicion >= 48 and posicion <= 55 and posf >= 48 and posf <= 55 or posicion >= 56 and posicion <= 63 and posf >= 56 and posf <= 63:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, -1
    return False, -1

def mov_caballo(posf, fichai, fichaf):
    if ficha_anterior == "black":
        arreglo = caballos_white
    else:
        arreglo = caballos_black
    index = -1
    for posicion in arreglo:
        index = index + 1
        if posicion + 15 == posf or posicion + 17 == posf or posicion - 15 == posf or posicion - 17 == posf or posicion + 10 == posf or posicion - 10 == posf or posicion - 6 == posf or posicion + 6 == posf:
            if fichaf == "none" or fichai == "black" and fichaf == "white" or fichai == "white" and fichaf == "black":
                return True, index
            else:
                return False, index
    return False, -1


if __name__ == '__main__':

    """ Create the Speech Recognition """
    walker = SpeechRecognition()

    # Inicializar pygame
    pygame.init()
    # Inicializar pantalla
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    fin = False
    pantalla.fill(color_fondo)
    # Pintar tablero
    Draw(board)
    Draw(pieces)
    pygame.display.flip()
    coord1 = 0
    coord2 = 0
    while not fin:
        # capturar eventos
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #if coord1 == 0:
        if ficha_anterior == "black":
            color_fichai = "white"
            print("Turno Blancas")
        else:
            color_fichai = "black"
            print("Turno Negras")

        print("Say the piece that you want to move...")
        fichai = walker.listen()
        print("You say " + fichai)

        print("Say the col...")
        colmove = walker.listen()
        print("You say " + colmove)

        print("Say the row...")
        rowmove = walker.listen()
        print("You say " + rowmove)

        r, c = int(rowmove) - 1, int(ord(colmove[0]) - ord('A'))
        print(r, c)
        posf = 8 * (7 - r) + c

        #print
        fichaf = pieces[posf]
        # posf = row(pos[0]) + column(pos[1]) * 8
        if fichaf == -1:
            color_fichaf = "none"
        elif fichaf % 2 == 0:
            color_fichaf = "black"
        else:
            color_fichaf = "white"

        if fichai == "rey" or fichai == "rey":
            movimiento, id_ficha = mov_rey(posf, color_fichai, color_fichaf)
            if movimiento == True:
                if ficha_anterior == "black":
                    pieces[posf] = pieces[rey_white[id_ficha]]
                    pieces[rey_white[id_ficha]] = -1
                    rey_white[id_ficha] = posf
                    ficha_anterior = color_fichai
                else:
                    pieces[posf] = pieces[rey_black[id_ficha]]
                    pieces[rey_black[id_ficha]] = -1
                    rey_black[id_ficha] = posf
                    ficha_anterior = color_fichai
            coord1 = 0
            coord2 = 0
        elif fichai == "reina" or fichai == "reina":
            movimiento, id_ficha = mov_reina(posf, color_fichai, color_fichaf)
            if movimiento == True:
                if ficha_anterior == "black":
                    pieces[posf] = pieces[reina_white[id_ficha]]
                    pieces[reina_white[id_ficha]] = -1
                    reina_white[id_ficha] = posf
                    ficha_anterior = color_fichai
                else:
                    pieces[posf] = pieces[reina_black[id_ficha]]
                    pieces[reina_black[id_ficha]] = -1
                    reina_black[id_ficha] = posf
                    ficha_anterior = color_fichai
            coord1 = 0
            coord2 = 0
        elif fichai == "torre" or fichai == "torre":
            movimiento, id_ficha = mov_torre(posf, color_fichai, color_fichaf)
            if movimiento == True:
                if ficha_anterior == "black":
                    pieces[posf] = pieces[torres_white[id_ficha]]
                    pieces[torres_white[id_ficha]] = -1
                    torres_white[id_ficha] = posf
                    ficha_anterior = color_fichai
                else:
                    pieces[posf] = pieces[torres_black[id_ficha]]
                    pieces[torres_black[id_ficha]] = -1
                    torres_black[id_ficha] = posf
                    ficha_anterior = color_fichai
            coord1 = 0
            coord2 = 0
        elif fichai == "alfil" or fichai == "alfil":
            movimiento, id_ficha = mov_alfil(posf, color_fichai, color_fichaf)
            if movimiento == True:
                if ficha_anterior == "black":
                    pieces[posf] = pieces[alfil_white[id_ficha]]
                    pieces[alfil_white[id_ficha]] = -1
                    alfil_white[id_ficha] = posf
                    ficha_anterior = color_fichai
                else:
                    pieces[posf] = pieces[alfil_black[id_ficha]]
                    pieces[alfil_black[id_ficha]] = -1
                    alfil_black[id_ficha] = posf
                    ficha_anterior = color_fichai
            coord1 = 0
            coord2 = 0
        elif fichai == "caballo" or fichai == "caballo":
            movimiento, id_ficha = mov_caballo(posf, color_fichai, color_fichaf)
            if movimiento == True:
                if ficha_anterior == "black":
                    pieces[posf] = pieces[caballos_white[id_ficha]]
                    pieces[caballos_white[id_ficha]] = -1
                    caballos_white[id_ficha] = posf
                    ficha_anterior = color_fichai
                else:
                    pieces[posf] = pieces[caballos_black[id_ficha]]
                    pieces[caballos_black[id_ficha]] = -1
                    caballos_black[id_ficha] = posf
                    ficha_anterior = color_fichai
            coord1 = 0
            coord2 = 0
        elif fichai == "peon" or fichai == "peon":
            movimiento, id_ficha = mov_peon(posf, color_fichai, color_fichaf)
            if movimiento == True:
                if ficha_anterior == "black":
                    pieces[posf] = pieces[peones_white[id_ficha]]
                    pieces[peones_white[id_ficha]] = -1
                    peones_white[id_ficha] = posf
                    ficha_anterior = color_fichai
                else:
                    pieces[posf] = pieces[peones_black[id_ficha]]
                    pieces[peones_black[id_ficha]] = -1
                    peones_black[id_ficha] = posf
                    ficha_anterior = color_fichai
            coord1 = 0
            coord2 = 0
        pantalla.fill(color_fondo)
        Draw(board)
        Draw(pieces)
        #pygame.display.update()
        pygame.display.flip()
