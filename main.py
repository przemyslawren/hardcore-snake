import os
from game_objects import *
import sys


def load_best_score():
    if os.path.exists('best_score.txt'):
        with open('best_score.txt', 'r') as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0


class Game:
    def __init__(self):
        pg.init()
        self.GAME_FONT = pg.font.SysFont('Comic Sans MS', 30)
        self.WINDOW_SIZE = 1000
        self.TILE_SIZE = 50
        self.screen = pg.display.set_mode([self.WINDOW_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.best_score = load_best_score()
        self.new_game()

    def draw_score(self):
        score_surface = self.GAME_FONT.render(f'Score: {self.snake.score}', True, (255, 255, 255))
        best_score_surface = self.GAME_FONT.render(f'Best Score: {self.best_score}', True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))
        self.screen.blit(best_score_surface, (self.WINDOW_SIZE - best_score_surface.get_width() - 10, 10))

    def draw_grid(self):
        [pg.draw.line(self.screen, [50] * 3, (x, 0), (x, self.WINDOW_SIZE))
         for x in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.screen, [50] * 3, (0, y), (self.WINDOW_SIZE, y))
         for y in range(0, self.WINDOW_SIZE, self.TILE_SIZE)]

    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)
        self.obstacles = Obstacle(self)

    def update(self):
        self.snake.update()
        self.obstacles.check_collision(self.snake.rect)
        if self.snake.score > self.best_score:
            self.best_score = self.snake.score
            self.save_best_score()
        pg.display.flip()
        self.clock.tick(60)

    def draw(self):
        self.screen.fill('black')
        self.draw_score()
        self.draw_grid()
        self.food.draw()
        self.snake.draw()
        self.obstacles.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.snake.control(event)

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

    def save_best_score(self):
        with open('best_score.txt', 'w') as file:
            file.write(str(self.best_score))


if __name__ == '__main__':
    game = Game()
    game.run()
