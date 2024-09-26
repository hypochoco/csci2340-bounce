
import pygame

from .component import Component

class DisplayComponent(Component):

    shape: str

    def __init__(self, shape: str=None) -> None:
        super().__init__()

        self.shape = shape

    def draw_circle(self, display, *args, **kwargs):
        RED = (255, 0, 0)
        pygame.draw.circle(display, RED, kwargs['position'], 5)

    def draw(self, display, *args, **kwargs):
        if self.shape == "circle":
            self.draw_circle(display, *args, **kwargs)
