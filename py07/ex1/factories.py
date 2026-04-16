from ex0 import CreatureFactory, Creature
from .healing import Sprouting, Bloomelle
from .transform import Shifting, Morphagon


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sprouting()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shifting()

    def create_evolved(self) -> Creature:
        return Morphagon()
