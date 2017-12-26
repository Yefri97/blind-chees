import pygame

class Chess():

    width = 900
    height = 600
    background = [82, 82, 82]

    tiles = (
        pygame.image.load('img/white.png'),
        pygame.image.load('img/gray.png')
    )

    pieces = [
        pygame.image.load('img/whiteKing.png'),
        pygame.image.load('img/blackKing.png'),
        pygame.image.load('img/whiteQueen.png'),
        pygame.image.load('img/blackQueen.png'),
        pygame.image.load('img/whiteBishop.png'),
        pygame.image.load('img/blackBishop.png'),
        pygame.image.load('img/whiteKnight.png'),
        pygame.image.load('img/blackKnight.png'),
        pygame.image.load('img/whiteRook.png'),
        pygame.image.load('img/blackRook.png'),
        pygame.image.load('img/whitePawn.png'),
        pygame.image.load('img/blackPawn.png')
    ]

    positions = [
        [4],                                                  # Rey blanco
        [60],                                                 # Rey negro
        [3],                                                  # Reina blanco
        [59],                                                 # Reina negro
        [2, 5],                                               # Alfiles blancos
        [58, 61],                                             # Alfiles negros
        [1, 6],                                               # Caballos blancos
        [57, 62],                                             # Caballos negros
        [0, 7],                                               # Torres blancas
        [56, 63],                                             # Torres negras
        [8, 9, 10, 11, 12, 13, 14, 15],                       # Peones blancos
        [48, 49, 50, 51, 52, 53, 54, 55]                      # Peones negros
    ]

    def __init__(self):
        pygame.init()
        self.board = pygame.display.set_mode([self.width, self.height])
        self.draw_board()

    def get_coord(self, pos):
        return (250 + (pos % 8) * 50, 450 - (pos // 8) * 50)

    def draw_board(self):
        """"""
        self.board.fill(self.background)

        for k in range(64):
            self.board.blit(self.tiles[((k + 1) + (k // 8)) % 2], self.get_coord(k))

        for i in range(12):
            for p in self.positions[i]:
                self.board.blit(self.pieces[i], self.get_coord(p))

        pygame.display.flip()

    def move_piece(self, type_piece, id_piece, new_pos):
        self.positions[type_piece][id_piece] = new_pos
        self.draw_board()

    def moves_rey(pos):
        pass

    def moves_dama(pos):
        pass

    def moves_alfil(pos):
        pass

    def moves_torre(pos):
        pass

    def moves_caballo(pos):
        pass

    def moves_peon(pos):
        pass

    def show_moves(id_piece):
        pass
