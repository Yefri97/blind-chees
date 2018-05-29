# ------------------------------------------------------------------------------
#
# Minimax: minimax.py
#
# ------------------------------------------------------------------------------

import math

class Minimax():

    pos_value = [
        # Rey
        [ 0.5,  0.5,  0.5,  0.0,  0.0,  0.5,  0.5,  0.5,
          0.5,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5,  0.5,
         -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,
         -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,
         -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
         -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
         -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,
         -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
        # Reina
        [-2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0,
         -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0,
         -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
          0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
         -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5,
         -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0,
         -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
         -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
        # Alfiles
        [-2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0,
         -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0,
         -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0,
         -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0,
         -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0,
         -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0,
         -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0,
         -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0
        ],
        # Caballos
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0,
         -4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0,
         -3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0,
         -3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0,
         -3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0,
         -3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0,
         -4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0,
         -5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        # Torres
        [ 0.0,  0.0,  0.0,  0.5,  0.5,  0.0,  0.0,  0.0,
          0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5,
         -0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -0.5,
          0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        # Peones
        [ 0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,
          0.5,  1.0,  1.0, -2.0, -2.0,  1.0,  1.0,  0.5,
          0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5,
          0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0,
          0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5,
          1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0,
          5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,
          0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]

    piece_value = [150, -150, 90, -90, 30, -30, 30, -30, 50, -50, 10, -10]

    def __init__(self, player):
        self.player = player

    def evaluate_board(self, board):
        value = 0.0
        for piece in range(len(board.positions)):
            for pos in board.positions[piece]:
                if pos == -1:
                    continue
                if self.player == 0:
                    p = pos
                    value += self.pos_value[piece//2][p] * self.piece_value[piece]
                else:
                    p = 56 - 8 * (pos // 8) + pos % 8
                    value += self.pos_value[piece//2][p] * -self.piece_value[piece]
        return value

    def minimax(self, depth, board, alpha, betha, player):

        best_move = (0, 0, 0, 0)

        if depth == 0:
            return (self.evaluate_board(board), best_move)

        all_moves = board.get_all_valid_moves(player)

        if player == self.player:
            max_val = -10000.0
            for move in all_moves:
                other = board.simulate(move)
                (val, bm) = self.minimax(depth - 1, other, alpha, betha, 1 - player)
                if val > max_val:
                    max_val = val
                    best_move = move
                if val > alpha:
                    alpha = val
                if alpha >= betha:
                    return (alpha, best_move)
            return (max_val, best_move)
        else:
            min_val = 10000.0
            for move in all_moves:
                other = board.simulate(move)
                (val, bm) = self.minimax(depth - 1, other, alpha, betha, 1 - player)
                if val < min_val:
                    min_val = val
                    best_move = move
                if val < betha:
                    betha = val
                if alpha >= betha:
                    return (betha, best_move)
            return (min_val, best_move)

    def get_best_move(self, board):
        depth = 4
        (value, best_move) = self.minimax(depth, board, -10000.0, 10000.0, self.player)
        print(value)
        return best_move
