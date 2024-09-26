
from typing import List

import sys
sys.path.append('..')

from entities.game_object import GameObject

class System:

    entities: List[GameObject]

    def __init__(self, entities=None) -> None:
        self.entities = entities
    
    def draw(self, display):
        pass

    def loop(self, dt):
        pass

