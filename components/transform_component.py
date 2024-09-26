
import pygame
from typing import Tuple

from .component import Component

class TransformComponent(Component):

    position: Tuple[float]

    def __init__(self, position: Tuple[float]=(0,0)) -> None:
        super().__init__()

        self.position = position

    def update_position(self, position):
        self.position = position
    
    def get_position(self):
        return self.position
