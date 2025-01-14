import pygame
import pyamaze


#  Classe que representa o rect do labirinto
class Maze(pygame.sprite.Sprite):
    MAZE_COLOR = (255, 255, 255)

    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)


#  Fun��o respons�vel por obter o maze_map (mapeamento das paredes)
def get_mazemap() -> dict:
    maze = pyamaze.maze(20, 20)
    maze.CreateMaze(loopPercent=50)
    return maze.maze_map


# Fun��o respons�vel por gerar o labirinto na janela
def maze_generator(win: pygame.Surface, rect_maze: pygame.Rect, maze_map: dict) -> None:
    wall_color = (255, 255, 255)
    initial_point_x, initial_point_y = rect_maze.topleft
    width_maze = rect_maze.width
    cell_grid_width = width_maze // 20

    for cell, walls in maze_map.items():
        line = cell[0]
        column = cell[1]
        x = initial_point_x + (cell_grid_width * (column - 1))
        y = initial_point_y + (cell_grid_width * (line - 1))

        index = 0
        wall_x = (cell_grid_width - 20) / 2
        for wall_found in walls.values():
            if wall_found == 0:
                directions = ["E", "W", "N", "S"]
                direction = directions[index]

                if direction in ["E", "W"]:
                    wall_surf = pygame.Surface((wall_x, cell_grid_width))
                    wall_surf.fill(wall_color)
                    if direction == "E":
                        wall_rect = wall_surf.get_rect(topright=(x + cell_grid_width, y))
                    else:
                        wall_rect = wall_surf.get_rect(bottomleft=(x, y + cell_grid_width))
                else:
                    wall_surf = pygame.Surface((cell_grid_width, wall_x))
                    wall_surf.fill(wall_color)
                    if direction == "N":
                        wall_rect = wall_surf.get_rect(topright=(x + cell_grid_width, y))
                    else:
                        wall_rect = wall_surf.get_rect(bottomleft=(x, y + cell_grid_width))

                win.blit(wall_surf, wall_rect)

            index += 1

#print(get_mazemap())

