from ex0 import Creature
from .capability import HealCapability


class Sprouting(Creature, HealCapability):

    def __init__(self) -> None:
        super().__init__("Sprouting", "Grass")

    def attack(self) -> str:
        return "Sprouting uses Vine Whip!"

    def heal(self, target=None) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):

    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target=None):
        return "Bloomelle heals itself and others for a large amount"
