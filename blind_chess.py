from speech_recognition import SpeechRecognition
from chess import Chess

if __name__ == '__main__':

    print("Creating the speech recognition...")
    walker = SpeechRecognition()
    print("Speech Recognition created...\n")

    print("Creating the board game...")
    game = Chess()
    print("Board Game created...\n")

    """
    b = pygame.image.load('img/black.png')
    for p in movs:
        self.screen.blit(b, self.get_coord(p))
    pygame.display.flip()

    tmp = game.get_moves(10)
    for t in tmp:
        print(t)
    input()
    exit()
    """

    turn = 0
    while True:

        print("Play " + ("white" if turn == 0 else "black") + " pieces\n")

        piece, col, row = walker.listen()

        type_piece = 2 * piece + turn
        new_pos = 8 * row + col

        tmp = game.get_moves(6)
        print("Caballo: " + str(len(tmp)))
        movs = game.get_moves(type_piece)
        for i in range(len(movs)):
            a = movs[i]
            for pos in a:
                if pos == new_pos:
                    id_piece = i

        game.move_piece(type_piece, id_piece, new_pos)

        print("End..? y / n")
        if input() == "y":
            break

        turn = 1 - turn
