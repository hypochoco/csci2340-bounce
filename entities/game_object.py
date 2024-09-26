
from typing import Dict

import sys
sys.path.append('..')

from components.component import Component

class GameObject:
    
    id: int
    components: Dict[str, Component]

    def __init__(self, id: int=0, components: Dict[str, Component]={}) -> None:
        self.id = id
        self.components = components

    def add_component(self, name: str, component: Component):
        self.components[name] = component
