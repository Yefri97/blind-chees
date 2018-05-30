import pygame

class Game():

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

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([self.width, self.height])

    def coord(self, pos):
        return (250 + (pos % 8) * 50, 450 - (pos // 8) * 50)

    def draw(self, board):
        """"""
        self.screen.fill(self.background)

        for k in range(64):
            self.screen.blit(self.tiles[((k + 1) + (k // 8)) % 2], self.coord(k))

        """for i in range(len(board.positions)):
            for p in board.positions[i]:
                if p != -1:
                    self.screen.blit(self.pieces[i], self.coord(p))"""
        for i in range(64):
            if board.board[i] != -1:
                self.screen.blit(self.pieces[board.board[i]], self.coord(i))

        x_a = 265
        y_n = 455        
        font = pygame.font.SysFont("arial", 30)
        pos_abc = ["a", "b", "c", "d", "e", "f", "g", "h"]
        pos_num = ["1", "2", "3", "4", "5", "6", "7", "8"]

        for i in range(8):
            leter = font.render(pos_abc[i], True, (0, 0, 0))
            num = font.render(pos_num[i], True, (0, 0, 0))
            self.screen.blit(leter, (x_a, 505))
            self.screen.blit(num, (220, y_n))
            x_a = x_a + 50
            y_n = y_n - 50

        pygame.display.flip()
