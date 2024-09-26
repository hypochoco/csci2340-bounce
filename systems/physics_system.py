
from typing import Tuple, Dict

from .system import System

import sys
sys.path.append('..')

from components.transform_component import TransformComponent
from components.physics_component import PhysicsComponent

class PhysicsSystem(System):

    gravity: float = -100.

    def collide(self):
        collisions: Dict[int, bool] = {}
        for entity in self.entities:
            if "transform" in entity.components:
                transform: TransformComponent = entity.components["transform"]
                x, y = transform.get_position()
                collisions[entity.id] = y <= 0
        return collisions

    def loop(self, dt):

        collisions = self.collide()

        for entity in self.entities:

            if "transform" in entity.components and "physics" in entity.components:
                transform: TransformComponent = entity.components["transform"]
                physics: PhysicsComponent = entity.components["physics"]

                x, y = transform.get_position()
                dx, dy = physics.get_velocity()

                # gravity
                if entity.id in collisions:
                    if collisions[entity.id]:
                        physics.update_velocity((dx, -dy))
                    else:
                        physics.update_velocity((dx, dy + self.gravity * dt))

                # update position
                dx, dy = physics.get_velocity()
                transform.update_position((x + dx * dt, y + dy * dt))

                
