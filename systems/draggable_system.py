
from typing import Tuple, Dict
import pygame
import numpy as np

from .system import System

import sys
sys.path.append('..')

from components.draggable_component import DraggableComponent
from components.transform_component import TransformComponent
from components.physics_component import PhysicsComponent

class DraggableSystem(System):

    state: str="UP"
    screen_size: Tuple[int]

    def __init__(self, entities=None, screen_size: Tuple[int]=(640, 400)) -> None:
        super().__init__(entities)

        self.screen_size = screen_size

    def loop(self, dt, inputs):

        if "MouseButtonDown" in inputs and inputs["MouseButtonDown"]: self.state = "DOWN"
        if "MouseButtonUp" in inputs and inputs["MouseButtonUp"]: self.state = "UP"

        if self.state == "UP": return

        x, y = pygame.mouse.get_pos()

        for entity in self.entities:

            if "draggable" in entity.components and "transform" in entity.components and "physics" in entity.components:
                draggable: DraggableComponent = entity.components["draggable"]
                transform: TransformComponent = entity.components["transform"]
                physics: PhysicsComponent = entity.components["physics"]

                # world position
                    # 100 => x=0 # NOTE: sync with display system
                    # 350 => y=0
                world_pos = (x-100, 350-y)

                # check range
                radius = np.array(draggable.radius)
                entity_pos = np.array(transform.get_position())
                if np.linalg.norm(world_pos-entity_pos) > radius: continue

                # update position
                transform.update_position(world_pos)
                physics.update_velocity((0, 0))
