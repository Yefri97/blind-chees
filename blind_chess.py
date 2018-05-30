from speech_recognition import SpeechRecognition
from chess import Chess
from game import Game
from minimax import Minimax

from gtts import gTTS
import os

WHITE = 0
BLACK = 1

if __name__ == '__main__':

    print("Creating the speech recognition...")

    tts = gTTS(text='Creating the speech recognition...', lang='en')
    tts.save("blind.mp3")
    os.system("mpg321 blind.mp3")

    rec = SpeechRecognition()
    print("Speech Recognition created...\n")

    tts = gTTS(text='Speech Recognition created...', lang='en')
    tts.save("blind.mp3")
    os.system("mpg321 blind.mp3")    

    print("Creating the board game...")

    board = Chess()
    game = Game()
    game.draw(board)
    print("Board Game created...\n")

    tts = gTTS(text='Board Game created...', lang='en')
    tts.save("blind.mp3")
    os.system("mpg321 blind.mp3")  

    rival = Minimax(BLACK)

    tts = gTTS(text='El juego ha comenzado', lang='es')
    tts.save("blind.mp3")
    os.system("mpg321 blind.mp3")    

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

        movement = rec.say(rival_move)

        tts = gTTS(text=movement, lang='es')
        tts.save("blind.mp3")
        os.system("mpg321 blind.mp3")

        # Print the game
        game.draw(board)

        print("End..? y / n")
        if input() == "y":
            break
