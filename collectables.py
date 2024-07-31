import pygame
import random
import utils

from pygame.locals import *


QTY_BOXES = 200


class Collectables(pygame.sprite.Sprite):
    def __init__(self, qty_boxes=QTY_BOXES):
        super().__init__()
        self.boxes_pos = []
        self.qty_boxes = qty_boxes

    def generate_boxes(self, maze_map) -> None:
        all_positions = [cell for cell in maze_map.keys()]
        positions = []

        for _ in range(self.qty_boxes):
            positions.append(random.choice(all_positions))

        self.boxes_pos = positions

    def get_box(self, event, flashs_list, player_position):
        if event.key == K_SPACE:
            if player_position in self.boxes_pos:

                flash_cells = []
                for flash_list in flashs_list:
                    for column, line in flash_list:
                        flash_cells.append((line + 1, column + 1))

                if player_position in flash_cells:
                    print("ITEM PEGO!")
                    self.boxes_pos.remove(player_position)

    def draw(self, screen, maze, flashs_list):
        flash_cells = []

        for flash_list in flashs_list:
            for column, line in flash_list:
                flash_cells.append((line + 1, column + 1))

        for box_pos in self.boxes_pos:
            if box_pos in flash_cells:
                box = pygame.Surface((14, 14))
                box.fill((153, 76, 0))

                pixel_xy = utils.cell_to_pixels(maze, box_pos)
                cell_rect = pygame.Rect(pixel_xy, (maze.cell_grid_width, maze.cell_grid_width))
                screen.blit(box, (cell_rect.centerx - 7, cell_rect.centery - 7))

