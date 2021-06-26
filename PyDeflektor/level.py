import pygame, json
from settings import get_path
from game_objects import Wall, Source, Mirror, Tracer, Target


class Level:


    def __init__(self, level_num):


        self.data = []
        self.tile_size = None
        self.grid_width = None
        self.grid_height = None
        self.width = None
        self.height = None
        self.countdown = None


        self.source = None
        self.source_id = None
        self.max_level = None

        self.all_sprites = pygame.sprite.Group()
        self.wall_group = pygame.sprite.Group()
        self.texture_wall_group = pygame.sprite.Group()
        self.source_group = pygame.sprite.Group()
        self.mirror_group = pygame.sprite.Group()
        self.tracer_group = pygame.sprite.Group()
        self.target_group = pygame.sprite.Group()


        with open(get_path("levels.json"), "r") as json_file:
            level_file = json.load(json_file)

            self.max_level = len(level_file)
            self.tile_size = level_file["Level_" + str(level_num)][0]["TileSize"]
            self.grid_width = level_file["Level_" + str(level_num)][0]["GridWidth"]
            self.grid_height = level_file["Level_" + str(level_num)][0]["GridHeight"]
            self.source_id = level_file["Level_" + str(level_num)][0]["SourceId"]
            self.countdown = level_file["Level_" + str(level_num)][0]["Countdown"]

            self.data = level_file["Level_" + str(level_num)][0]["Data"]


        self.data = [(self.data[i:i + self.grid_width]) for i in range(0, self.grid_width * self.grid_height, self.grid_width)]

        self.width = self.grid_width * self.tile_size
        self.height = self.grid_height * self.tile_size


        for y in range(self.grid_height):

            for x in range(self.grid_width):

                if self.data[y][x] == 0:
                    self.source = Source((x * self.tile_size, y * self.tile_size), self.source_id)

                elif self.data[y][x] == 1:
                    self.mirror_group.add(Mirror((x * self.tile_size, y * self.tile_size)))

                elif self.data[y][x] == 2:
                    self.target_group.add(Target((x * self.tile_size, y * self.tile_size)))

                elif self.data[y][x] == 3:
                    self.texture_wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall.png"))

                elif self.data[y][x] == 4:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-hor-top.png"))

                elif self.data[y][x] == 5:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-hor-bot.png"))

                elif self.data[y][x] == 6:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-vert-l.png"))

                elif self.data[y][x] == 7:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-vert-r.png"))

                elif self.data[y][x] == 8:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-corner-1.png"))

                elif self.data[y][x] == 9:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-corner-2.png"))

                elif self.data[y][x] == 10:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-corner-4.png"))

                elif self.data[y][x] == 11:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-corner-3.png"))

                elif self.data[y][x] == 12:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-i-corner-1.png"))
                
                elif self.data[y][x] == 13:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-i-corner-2.png"))

                elif self.data[y][x] == 14:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-i-corner-3.png"))

                elif self.data[y][x] == 15:
                    self.wall_group.add(Wall((x * self.tile_size, y * self.tile_size), "wall-i-corner-4.png"))

        
        self.source_group.add(self.source)


    def load_tracer(self, position, vector):

        self.tracer = Tracer(position, vector)

        self.tracer_group.add(self.tracer)

