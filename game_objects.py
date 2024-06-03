import pygame as pg
from random import randrange

vec2 = pg.math.Vector2


def get_random_position(size, window_size, exclude_positions):
    while True:
        pos = [randrange(size // 2, window_size - size // 2, size), randrange(size // 2, window_size - size // 2, size)]
        if pos not in exclude_positions:
            return pos


class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.segments = []
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_position()
        self.direction = vec2(0, 0)
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = [self.rect.copy()]
        self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
        self.score = 0

    def control(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and self.directions[pg.K_w]:
                self.direction = vec2(0, -self.size)
                self.directions = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_s and self.directions[pg.K_s]:
                self.direction = vec2(0, self.size)
                self.directions = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

            if event.key == pg.K_a and self.directions[pg.K_a]:
                self.direction = vec2(-self.size, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}

            if event.key == pg.K_d and self.directions[pg.K_d]:
                self.direction = vec2(self.size, 0)
                self.directions = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}

    def delta_time(self):
        time_now = pg.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False

    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.game.food.rect.center = self.game.food.get_random_position()
            self.length += 1
            self.score += 10

    def check_self_eating(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()

    def get_random_position(self):
        exclude_positions = [segment.center for segment in self.segments]
        if hasattr(self.game, 'obstacles'):
            exclude_positions += [obstacle.center for obstacle in self.game.obstacles.rects]
        return get_random_position(self.size, self.game.WINDOW_SIZE, exclude_positions)

    def check_borders(self):
        if self.rect.left < 0 or self.rect.right > self.game.WINDOW_SIZE:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.WINDOW_SIZE:
            self.game.new_game()

    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]

    def update(self):
        self.check_self_eating()
        self.check_borders()
        self.check_food()
        self.move()

    def draw(self):
        [pg.draw.rect(self.game.screen, 'green', segment) for segment in self.segments]


class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TILE_SIZE
        self.rect = pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
        self.rect.center = self.get_random_position()

    def get_random_position(self):
        exclude_positions = [segment.center for segment in self.game.snake.segments]
        if hasattr(self.game, 'obstacles'):
            exclude_positions += [obstacle.center for obstacle in self.game.obstacles.rects]
        return get_random_position(self.size, self.game.WINDOW_SIZE, exclude_positions)

    def draw(self):
        pg.draw.rect(self.game.screen, 'red', self.rect)


class Obstacle:
    def __init__(self, game, num_obstacles=20):
        self.game = game
        self.size = game.TILE_SIZE
        self.rects = [pg.rect.Rect([0, 0, game.TILE_SIZE - 2, game.TILE_SIZE - 2])
                      for _ in range(num_obstacles)]
        self.positions = [self.get_random_position() for _ in range(num_obstacles)]
        for rect, pos in zip(self.rects, self.positions):
            rect.center = pos

    def get_random_position(self):
        exclude_positions = [segment.center for segment in self.game.snake.segments]
        if hasattr(self.game, 'food'):
            exclude_positions.append(self.game.food.rect.center)
        return get_random_position(self.size, self.game.WINDOW_SIZE, exclude_positions)

    def draw(self):
        for rect in self.rects:
            pg.draw.rect(self.game.screen, 'blue', rect)

    def check_collision(self, snake_rect):
        for rect in self.rects:
            if rect.colliderect(snake_rect):
                self.game.new_game()
