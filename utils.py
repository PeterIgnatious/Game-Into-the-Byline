import pygame


def load_display(map_id, resolution):
    if map_id == "config":
        display = pygame.Surface((1280, 720))
        display.fill("Red")
    else:
        display = pygame.image.load(f"assets/{map_id}.png")
        display = pygame.transform.scale(display, resolution)
    return display


def set_music(map_id):
    musics = {"not_scared": "entering_the_maze"}

    music_text = musics[map_id]
    music = pygame.mixer.Sound(f'assets/sounds/{music_text}.mp3')
    music.set_volume(0.3)

    return music


def cell_to_pixels(maze, cell_position):
    pos_x = cell_position[0]
    pos_y = cell_position[1]

    pixel_x = maze.initial_point_x + ((pos_y - 1) * maze.cell_grid_width)
    pixel_y = maze.initial_point_y + ((pos_x - 1) * maze.cell_grid_width)

    new_pos = (pixel_x, pixel_y)

    return new_pos


