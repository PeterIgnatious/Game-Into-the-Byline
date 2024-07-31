import pygame
import utils
import maze_generator

from pygame.locals import *
from sys import exit
from player import Player
from flash import Flash
from collectables import Collectables


RESOLUTION = (1280, 720)
FPS = 60


flashs_list = [[]]
num_flashs = 7


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Into the Byline")

        self.clock = pygame.time.Clock()

        self.icon = pygame.image.load('assets/icon.png')
        pygame.display.set_icon(self.icon)

        self.map_id = "home_screen"
        self.display = utils.load_display(self.map_id, RESOLUTION)

        self.music = "None :)"

        x, y, width, height, color = 1, 1, 10, 10, (33, 179, 76)
        left, right, up, down = K_a, K_d, K_w, K_s
        width_maze, num_pixels = 600, 20
        self.player = Player(x, y, self.screen, width, height, color, left, right, up, down, width_maze, num_pixels)

        self.flash = Flash(self.screen, Color(0, 0, 255), K_LEFT, K_RIGHT, K_UP, K_DOWN, num_flashs)

        self.maze_map = maze_generator.get_mazemap()
        self.maze = maze_generator.Maze(57.5, 57.5, 600, 600, self.maze_map)

        self.collectables = Collectables()
        self.collectables.generate_boxes(self.maze_map)

    def run(self):
        global flashs_list

        while True:
            self.clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                    if self.map_id == "home_screen":
                        if event.key == pygame.K_1:
                            self.map_id = "not_scared"
                            self.display = utils.load_display(self.map_id, RESOLUTION)
                            self.music = utils.set_music(self.map_id)
                            self.music.play()
                            pygame.time.delay(4000)
                            self.player.spawn(20)
                        if event.key == pygame.K_2:
                            self.map_id = "config"
                            self.display = utils.load_display(self.map_id, RESOLUTION)
                            self.music = utils.set_music(self.map_id)
                        if event.key == pygame.K_3:
                            pygame.quit()
                            exit()

                    self.collectables.get_box(event, flashs_list, self.player.player_position)
                    x, y = self.player.control(event, self.maze_map)
                    flashs_list = self.flash.active(event, self.maze_map, x, y, flashs_list)

                    cells = []
                    for flash_list in flashs_list:
                        for column, line in flash_list:
                            cells.append((line + 1, column + 1))

                    cells.append(self.player.player_position)

            if self.map_id in ["home_screen", "config"]:
                self.screen.blit(self.display, (0, 0))
                pygame.display.update()
            else:
                self.screen.blit(self.display, (0, 0))
                self.collectables.draw(self.screen, self.maze, flashs_list)
                self.player.draw(57.5, 57.5)

                self.maze.display_maze_cells(self.screen, cells)

                pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
