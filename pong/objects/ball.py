from pgzero.actor import Actor
from ..global_variables import HALF_HEIGHT, HALF_WIDTH, game

class Ball(Actor):
    def __init__(self, dx):
        super().__init__("ball", (0,0))
        self.x, self.y = HALF_WIDTH, HALF_HEIGHT
        self.dx, self.dy = dx, 0
        self.speed = 5
    
    def update(self):
        for i in range(self.speed):
            original_x = self.x
            self.x += self.dx
            self.y = self.dy
            if abs(self.x - HALF_WIDTH) >= 344 and abs(original_x - HALF_WIDTH) < 344:
                if self.x < HALF_WIDTH:
                    new_dir_x = 1
                    bat = game.bats[0]
                else:
                    new_dir_x = -1
                    bat = game.bats[1]

            difference_y = self.y - bat.y

            if difference_y > -64 and difference_y < 64:
                self.dx = -self.dx
                self.dy += difference_y / 128
                self.dy = min(max(self.dy, -1), 1)
                self.dx, self.dy = normalized(self.dx, self.dy)
        
