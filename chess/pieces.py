from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def get_valid_moves(self):
        pass
    
    @abstractmethod
    def move(self):
        self.move_piece()
        self.recalculate_moves()
    
    @abstractmethod
    def move_piece(self):
        pass

    @abstractmethod
    def recalculate_moves(self):
        pass
    

class Pawn(Piece):
    def __init__(self, color, is_first_turn, is_on_en_passant_row):
        self.color = color
        self.is_first_turn = is_first_turn
        self.is_on_en_passant_row = is_on_en_passant_row

class Knight(Piece):
    def __init__(self, color):
        self.color = color

class Bishop(Piece):
    def __init__(self, color):
        self.color = color

class Rook(Piece):
    def __init__(self, color):
        self.color = color

class Queen(Piece):
    def __init__(self, color):
        self.color = color

class King(Piece):
    def __init__(self, color):
        self.color = color
