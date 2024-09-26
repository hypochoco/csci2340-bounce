
import pygame

from .component import Component

class DraggableComponent(Component):

    radius: float = 20.

    def __init__(self) -> None:
        super().__init__()
