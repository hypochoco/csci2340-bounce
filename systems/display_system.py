
from typing import Tuple

from .system import System

import sys
sys.path.append('..')

from components.transform_component import TransformComponent
from components.display_component import DisplayComponent

class DisplaySystem(System):

    screen_size: Tuple[int]

    def __init__(self, entities=None, screen_size: Tuple[int]=(640, 400)) -> None:
        super().__init__(entities)

        self.screen_size = screen_size

    def draw(self, display):

        for entity in self.entities:

            if "transform" in entity.components and "draw" in entity.components:
                transform: TransformComponent = entity.components["transform"]
                draw: DisplayComponent = entity.components["draw"]

                # 100 => x=0
                # 350 => y=0

                x, y = transform.get_position()
                draw.draw(display, position=(x+100, 350-y))
