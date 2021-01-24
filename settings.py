import os, pygame

# SUPPORTING FUNCTIONS
def get_level(f):

    return os.path.dirname(os.path.realpath(__file__)) + "/levels/" + f

def get_texture(f):

    return os.path.dirname(os.path.realpath(__file__)) + "/textures/" + f

mouse_cursor = pygame.image.load(get_texture("cursor.png"))

# COLORS
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)



