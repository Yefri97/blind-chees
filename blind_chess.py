from speech_recognition import SpeechRecognition
from chess import Chess
from game import Game
from minimax import Minimax

WHITE = 0
BLACK = 1

if __name__ == '__main__':

    print("Creating the speech recognition...")
    rec = SpeechRecognition()
    print("Speech Recognition created...\n")

    print("Creating the board game...")
    board = Chess()
    game = Game()
    game.draw(board)
    print("Board Game created...\n")

    rival = Minimax(BLACK)

    while True:
        # Get all the valid moves for the white player
        valid_moves = board.get_all_valid_moves(WHITE)
        # The movement is chosen
        chosen_move = rec.listen(valid_moves)
        # Do the movement in the board
        board.do(chosen_move)
        # Print the game
        game.draw(board)
        # Get the best move for the black player
        rival_move = rival.get_best_move(board)
        # Do the rival movement
        board.do(rival_move)
        # Print the game
        game.draw(board)

        print("End..? y / n")
        if input() == "y":
            break
