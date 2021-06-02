import pygame, math
from settings import *


class Wall(pygame.sprite.Sprite):


    def __init__(self, position, wall_img):
        super().__init__()

        self.image = pygame.image.load(get_texture(wall_img))
        
        self.rect = self.image.get_rect(topleft = position)


class Source(pygame.sprite.Sprite):


    def __init__(self, position, direction):
        super().__init__()

        self.px = position[0] + 16
        self.py = position[1] + 16

        self.image = pygame.image.load(get_texture("source.png"))
    
        self.rect = self.image.get_rect(center = (self.px, self.py))

        self.id = direction
        self.laser_direction = None
        
        if self.id == 1:

            self.image = pygame.transform.rotate(self.image, -90)
            self.laser_direction = (2,0)

        elif self.id == 2:

            self.image = self.image
            self.laser_direction = (0,-2)

        elif self.id == 3:

            self.image = pygame.transform.rotate(self.image, 90)
            self.laser_direction = (-2,0)

        elif self.id == 4:

            self.image = pygame.transform.rotate(self.image, 180)
            self.laser_direction = (0,2)


class Mirror(pygame.sprite.Sprite):


    def __init__(self, position):
        super().__init__()
        
        self.image = pygame.image.load(get_texture("mirror-0.png"))
 
        self.rect = self.image.get_rect(topleft = position)

        self.vector_set = [
                        (0,1), (-1, math.sqrt(6)), 
                        (-1, 1), ( - math.sqrt(6), 1), 
                        (1,0), (math.sqrt(6), 1), 
                        (1, 1), (1, math.sqrt(6))
                        ]

        self.normal_vector = pygame.Vector2(self.vector_set[0])

        self.out_vector = pygame.Vector2(0,0)

        self.is_selected = False


    def update(self, where):

        if self.is_selected:
            
            pygame.draw.rect(where, YELLOW, self.rect, 1)

        if self.normal_vector == pygame.Vector2(self.vector_set[0]):
            self.image = pygame.image.load(get_texture("mirror-0.png"))
            

        if self.normal_vector == pygame.Vector2(self.vector_set[1]):
            self.image = pygame.image.load(get_texture("mirror-1.png"))
            

        if self.normal_vector == pygame.Vector2(self.vector_set[2]):
            self.image = pygame.image.load(get_texture("mirror-2.png"))
            

        if self.normal_vector == pygame.Vector2(self.vector_set[3]):
            self.image = pygame.image.load(get_texture("mirror-3.png"))
            

        if self.normal_vector == pygame.Vector2(self.vector_set[4]):
            self.image = pygame.image.load(get_texture("mirror-4.png"))
            

        if self.normal_vector == pygame.Vector2(self.vector_set[5]):
            self.image = pygame.image.load(get_texture("mirror-5.png"))
            

        if self.normal_vector == pygame.Vector2(self.vector_set[6]):
            self.image = pygame.image.load(get_texture("mirror-6.png"))
            
            
        if self.normal_vector == pygame.Vector2(self.vector_set[7]):
            self.image = pygame.image.load(get_texture("mirror-7.png"))
            

    def rotate_cw(self):

        if self.is_selected:

            curr = self.vector_set.index(self.normal_vector)

            if curr < 7:

                self.normal_vector = self.vector_set[curr + 1]
            
            else:

                self.normal_vector = self.vector_set[0]


    def rotate_ccw(self):

        if self.is_selected:

            curr = self.vector_set.index(self.normal_vector)

            self.normal_vector = self.vector_set[curr - 1]


    def rotate_out_cw(self):

        self.out_vector = self.out_vector.rotate(45)

    def rotate_out_ccw(self):

        self.out_vector = self.out_vector.rotate(-45)


class Tracer(pygame.sprite.Sprite):


    def __init__(self, position, vector):
        super().__init__()

        self.p_x = position[0]
        self.p_y = position[1]

        self.image = pygame.Surface((1,1))
        self.rect = self.image.get_rect(center = (self.p_x, self.p_y))

        self.vector = vector


    def update(self):

        self.rect = self.rect.move(self.vector)


class Target(pygame.sprite.Sprite):


    def __init__(self, position):
        super().__init__()

        self.p_x = position[0]
        self.p_y = position[1]

        self.image = pygame.image.load(get_texture("target-0.png"))
        
        self.rect = self.image.get_rect(topleft = (self.p_x, self.p_y))


class Template:

    def __init__(self, width, height):

        self.image = pygame.Surface((200, 120))
        self.rect = self.image.get_rect(center = (width / 2, height / 2))



       






