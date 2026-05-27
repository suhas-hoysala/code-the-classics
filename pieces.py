from abc import ABC, abstractmethod

class Piece(ABC):
    @abstractmethod
    def get_moves(self):
        pass
    
    @abstractmethod
    def move(self):
        pass