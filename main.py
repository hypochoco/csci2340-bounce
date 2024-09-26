import pygame
from pygame.locals import *

from entities.game_object import GameObject

from systems.display_system import DisplaySystem
from systems.physics_system import PhysicsSystem
from systems.draggable_system import DraggableSystem

from components.display_component import DisplayComponent
from components.transform_component import TransformComponent
from components.physics_component import PhysicsComponent
from components.draggable_component import DraggableComponent
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

        self.inputs = {}
        self.clock = pygame.time.Clock()

        # game objects
        go1 = GameObject(
            id=0,
            components={
                'draw': DisplayComponent('circle'),
                'transform': TransformComponent((0, 100)),
                'physics': PhysicsComponent(),
                'draggable': DraggableComponent()
            }
        )

        # system initialization
        self.display_system = DisplaySystem([go1], self.size)
        self.physics_system = PhysicsSystem([go1])
        self.draggable_system = DraggableSystem([go1], self.size)
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.inputs["MouseButtonDown"] = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.inputs["MouseButtonUp"] = True

    def on_loop(self):
        delta_time = self.clock.tick(60)
        delta_seconds = delta_time / 1000.0
        self.physics_system.loop(delta_seconds)

        self.draggable_system.loop(delta_seconds, self.inputs)

        self.inputs = {}

    def on_render(self):
        self._display_surf.fill((255, 255, 255))
        self.display_system.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    app = App()
    app.on_execute()