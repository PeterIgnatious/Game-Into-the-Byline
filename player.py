import pygame
from pygame.locals import *
from pygame import mixer
import random

mixer.init()
step = mixer.Sound("assets/sounds/steps.mp3")


class Player:
    def __init__(self, x, y, win, width, height, color, left, right, up, down, width_maze, num_pixels):
        self.pos_x = x
        self.pos_y = y
        self.window = win
        self.width = width
        self.height = height
        self.color = color
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.speed = width_maze / num_pixels
        self.player_position = (self.pos_y + 1, self.pos_x + 1)

    def spawn(self, num_pixels):

        self.pos_x = random.randint(0, num_pixels - 1)
        if self.pos_x in [0, num_pixels - 1]:
            self.pos_y = random.randint(0, num_pixels - 1)
        else:
            self.pos_y = random.choice([0, num_pixels - 1])

    def draw(self, x_maze, y_maze):

        pos_x = self.pos_x * self.speed + x_maze + (self.speed - self.width) / 2
        pos_y = self.pos_y * self.speed + y_maze + (self.speed - self.height) / 2

        pygame.draw.rect(self.window, self.color, (pos_x, pos_y, self.width, self.height))
        # pygame.display.update((self.pos_x * self.speed + x_maze, self.pos_y * self.speed + y_maze, self.speed, self.speed))

        return self.pos_x + 1, self.pos_y + 1

    def control(self, event, maze_map):

        possible_directions = maze_map[(self.pos_y + 1, self.pos_x + 1)]

        if event.type == KEYDOWN:
            if event.key == self.left and possible_directions["W"]:
                step.play()
                self.pos_x -= 1

            elif event.key == self.right and possible_directions["E"]:
                step.play()
                self.pos_x += 1

            elif event.key == self.up and possible_directions["N"]:
                step.play()
                self.pos_y -= 1

            elif event.key == self.down and possible_directions["S"]:
                step.play()
                self.pos_y += 1

        self.player_position = (self.pos_y + 1, self.pos_x + 1)

        return self.pos_x, self.pos_y
