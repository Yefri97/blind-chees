# ------------------------------------------------------------------------------
#
# Minimax: minimax.py
#
# ------------------------------------------------------------------------------

import math

class Minimax():

    pos_value = [
        # Rey
        [2.0, 2.0, 2.0, 1.5, 1.5, 2.0, 2.0, 2.0,
         2.0, 2.0, 1.5, 1.5, 1.5, 1.5, 2.0, 2.0,
         2.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 2.0,
         1.0, 1.0, 1.0, 0.5, 0.5, 1.0, 1.0, 1.0,
         1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,
         1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,
         1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0,
         1.0, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1.0],
        # Reina
        [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         1.0, 1.5, 2.0, 1.5, 1.5, 1.5, 1.5, 1.0,
         1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.5, 1.0,
         1.0, 1.5, 2.0, 2.0, 2.0, 2.0, 1.5, 1.0,
         1.0, 1.5, 2.0, 2.0, 2.0, 2.0, 1.5, 1.0,
         1.0, 1.5, 2.0, 2.0, 2.0, 2.0, 1.5, 1.0,
         1.0, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.0,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
        # Alfiles
        [0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         1.0, 1.5, 1.0, 1.0, 1.0, 1.0, 1.5, 1.0,
         1.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 1.0,
         1.0, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 1.0,
         1.0, 1.5, 1.5, 2.0, 2.0, 1.5, 1.5, 1.0,
         1.0, 1.0, 1.5, 2.0, 2.0, 1.5, 1.0, 1.0,
         1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5],
        # Caballos
        [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
         0.5, 0.5, 1.0, 1.5, 1.5, 1.0, 0.5, 0.5,
         0.5, 1.5, 1.5, 2.0, 2.0, 1.5, 1.5, 0.5,
         0.5, 1.0, 2.0, 2.0, 2.0, 2.0, 1.0, 0.5,
         0.5, 1.5, 2.0, 2.0, 2.0, 2.0, 1.5, 0.5,
         0.5, 1.0, 1.5, 2.0, 2.0, 1.5, 1.0, 0.5,
         0.5, 0.5, 1.0, 1.0, 1.0, 1.0, 0.5, 0.5,
         0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
        # Torres
        [1.0, 1.0, 1.0, 1.5, 1.5, 1.0, 1.0, 1.0,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.5,
         0.5, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 0.5,
         1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
        # Peones
        [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
         1.5, 1.5, 1.5, 0.5, 0.5, 1.5, 1.5, 1.5,
         1.5, 0.5, 0.5, 1.0, 1.0, 0.5, 0.5, 1.5,
         1.0, 1.0, 1.0, 2.0, 2.0, 1.0, 1.0, 1.0,
         0.5, 0.5, 1.5, 2.0, 2.0, 1.5, 0.5, 0.5,
         1.5, 1.5, 2.0, 2.0, 2.0, 2.0, 1.5, 1.5,
         2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
         0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    ]

    piece_value = [150, 90, 30, 30, 50, 10]

    def __init__(self, player):
        self.player = player

    def evaluate(self, current):
        value = 0.0
        for (pos, cell) in enumerate(current.board):
            if cell == -1:
                continue;
            piece, color = cell // 2, cell % 2
            p = pos if self.player == 0 else 56 - 8 * (pos // 8) + pos % 8
            if color == self.player:
                value += self.pos_value[piece][p] * self.piece_value[piece]
            else:
                value -= self.pos_value[piece][p] * self.piece_value[piece]
        return value

    def minimax(self, depth, board, alpha, betha, player):

        best_move = (0, 0, 0, 0)

        if depth == 0:
            return (self.evaluate(board), best_move)

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
