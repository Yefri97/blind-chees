from speech_recognition import SpeechRecognition
from chess import Chess

if __name__ == '__main__':

    tags_pieces = ['rey', 'reina', 'alfil', 'caballo', 'torre', 'peon']

    tags_col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    tags_row = ['1', '2', '3', '4', '5', '6', '7', '8']

    print("Creating the Speech Recognition...")
    print("Piece")
    recog_piece = SpeechRecognition(tags_pieces)
    print("Col")
    recog_col = SpeechRecognition(tags_col)
    print("Row")
    recog_row = SpeechRecognition(tags_row)
    print("Speech Recognition created...\n")

    print("Creating the board game...")
    game = Chess()

    # walker.listen_piece()
    piece = recog_piece.listen()
    # walker.listen_col()
    # walker.listen_row()
    col = recog_col.listen()
    row = recog_row.listen()

    id_piece = 3
    input()
    game.move_piece(2 * piece, id_piece, 8 * row + col)
    input()
