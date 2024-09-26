
import pygame
from typing import Tuple

from .component import Component

class PhysicsComponent(Component):

    velocity: Tuple[float]

    def __init__(self, velocity: Tuple[float]=(0,0)) -> None:
        super().__init__()

        self.velocity = velocity

    def update_velocity(self, velocity):
        self.velocity = velocity
    
    def get_velocity(self):
        return self.velocity
