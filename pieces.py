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
    

class Pawn(Piece):
    def __init__(self, color):
        self.