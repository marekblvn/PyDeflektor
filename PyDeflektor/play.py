import pygame, sys
from settings import *
from level import Level
from game_objects import Template


class Play:

    def __init__(self, level):


        ### Properties ###
        self.state = "init"

        self.level = Level(level)

        self.title = pygame.display.set_caption("PyDeflektor")

        self.screen = pygame.display.set_mode((self.level.width, self.level.height))

        self.cursor = mouse_cursor

        self.clock = pygame.time.Clock()

        self.time_left = self.level.countdown

        pygame.mouse.set_visible(False)

        self.playing = False


        ### Mouse ###
        self.mouse_position = None

        self.mouse_click = None


        ### Laser ###
        self.laser_points = []


        ### Scenes ###
        pygame.font.init()

        self.init_screen = pygame.image.load(get_texture("init_screen.png"))

        self.game_over_screen = pygame.image.load(get_texture("game_over.png"))

        self.start_screen = pygame.image.load(get_texture("start_game.png"))

        self.end_screen = pygame.image.load(get_texture("end_screen.png"))

        self.template = Template(self.level.width, self.level.height)


    def check_events(self):


        for event in pygame.event.get():


            if event.type == pygame.QUIT:

                self.end_game()


            if event.type == pygame.KEYUP:

                if event.key == pygame.K_ESCAPE:

                    self.end_game()

                
                if self.state == "init":

                    if event.key == pygame.K_RETURN:
                    
                        self.state = "ready"


                if self.state == "ready" or self.state == "started":

                    if event.key == pygame.K_SPACE:

                        self.state = "started"

                        if self.playing == False:

                            self.get_laser(self.level.source.rect.center, pygame.Vector2((self.level.source.laser_direction)))

                            self.laser_points = [self.level.source.rect.center, self.level.tracer.rect.center]

                            self.time_left = self.level.countdown

                            self.playing = True


                if self.playing:

                    if event.key == pygame.K_r:

                        self.mirror_reset()

                        self.get_laser(self.level.source.rect.center, pygame.Vector2((self.level.source.laser_direction)))

                        self.laser_points = [self.level.source.rect.center, self.level.tracer.rect.center]

                        self.time_left = self.level.countdown


                if event.key == pygame.K_e:

                    for m in self.level.mirror_group:

                        m.rotate_cw()

                        if m.rect.center in self.laser_points and m.is_selected:

                            self.laser_points = self.laser_points[:self.laser_points.index(m.rect.center) + 1]

                            self.del_laser()

                            self.laser_points.append(m.rect.center)

                            m.rotate_out_cw()

                            self.level.load_tracer(m.rect.center, m.out_vector)


                if event.key == pygame.K_q:

                    for m in self.level.mirror_group:

                        m.rotate_ccw()

                        if m.rect.center in self.laser_points and m.is_selected:

                            self.laser_points = self.laser_points[:self.laser_points.index(m.rect.center) + 1]

                            self.del_laser()

                            self.laser_points.append(m.rect.center)

                            m.rotate_out_ccw()

                            self.level.load_tracer(m.rect.center, m.out_vector)


    def draw_frame(self):

        self.screen.fill((77, 77, 77))

        self.level.wall_group.draw(self.screen)

        self.level.texture_wall_group.draw(self.screen)

        self.level.mirror_group.draw(self.screen)

        self.level.source_group.draw(self.screen)

        self.level.tracer_group.draw(self.screen)

        self.level.target_group.draw(self.screen)

        if self.playing == False:

            if self.state == "init":

                self.screen.blit(self.init_screen, (0,0))

            elif self.state == "ready":

                self.screen.blit(self.start_screen, self.template)

            elif self.state == "started":

                self.screen.blit(self.game_over_screen, self.template)
                
            elif self.state == "end":

                self.screen.blit(self.end_screen, self.template)

        self.screen.blit(self.cursor, self.mouse_position)


    def get_laser(self, pos, vector):

        self.level.load_tracer(pos, vector)


    def del_laser(self):

        self.level.tracer_group.remove(self.level.tracer)


    def update_laser(self):

        if self.laser_points and self.playing:

            self.laser_points.pop()

            self.laser_points.append(self.level.tracer.rect.center)


    def draw_laser(self):

       if len(self.laser_points) > 1 and self.playing:

           pygame.draw.lines(self.screen, (230, 0, 0), False, self.laser_points, 2)

    
    def end_game(self):

        sys.exit()
        
        pygame.quit()


    def tracer_mirror_events(self):

        for mirror in self.level.mirror_group:

            if self.level.tracer.rect.center == mirror.rect.center:

                mirror.out_vector = (self.level.tracer.vector).reflect(mirror.normal_vector)

                self.level.tracer.vector.reflect_ip(mirror.normal_vector)

                self.laser_points.insert(-1, mirror.rect.center)


        if pygame.sprite.spritecollide(self.level.tracer, self.level.wall_group, False):

            self.laser_points.insert(-1, self.level.tracer.rect.center)

            self.level.tracer_group.remove(self.level.tracer)


    def target_update(self):

        for t in self.level.target_group:

            if t.rect.colliderect(self.level.tracer.rect):

                self.laser_points.insert(-1, t.rect.center)

                self.del_laser()

            if t.rect.center in self.laser_points:

                self.playing = False

                self.state = "level_fin"


    def mirror_update(self):

        for m in self.level.mirror_group:

            if m.rect.collidepoint(self.mouse_position) and self.mouse_click:

                for _ in self.level.mirror_group:

                    _.is_selected = False

                m.is_selected = True

            if m.rect.center not in self.laser_points:

                m.visited = False 

        
        if self.playing == False:

            for m in self.level.mirror_group:

                m.is_selected = False

    
    def mirror_reset(self):

        for m in self.level.mirror_group:

            m.normal_vector = (0,1)

    
    def blit_time_left(self):

        if self.time_left > 0:

            if self.playing:

                self.screen.blit(pygame.font.SysFont("consolas", 18, True).render(str(f"{round(self.time_left, 1)}"), True, BLACK), (5,5))

                self.time_left -= 0.03

            if not self.playing:

                self.time_left = self.level.countdown

                self.screen.blit(pygame.font.SysFont("consolas", 18, True).render(str(f"{round(self.time_left, 1)}"), True, BLACK), (5,5))
    

    def update(self):

        self.level.mirror_group.update(self.screen)

        self.level.tracer_group.update()

        self.mirror_update()

        if self.level.tracer_group:

            self.tracer_mirror_events()

            self.update_laser()

            self.target_update()

        self.draw_laser()

        if self.state == "started":

            self.blit_time_left()

        pygame.display.flip()

    
    def run(self):

        self.mouse_position = pygame.mouse.get_pos()

        self.mouse_click = pygame.mouse.get_pressed()[0]

        self.draw_frame()

        self.check_events()

        if self.time_left < 0:

            self.playing = False

            self.mirror_reset()

