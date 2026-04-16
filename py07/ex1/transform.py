from ex0 import Creature
from .capability import TransformCapability


class Shifting(Creature, TransformCapability):

    def __init__(self) -> None:
        super().__init__("Shifting", "Normal")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed is False:
            return "Shifting attacks normally."
        return "Shifting performs a boosted strike!"

    def transform(self) -> str:
        self._transformed = True
        return "Shifting shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shifting returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")
        self._transformed = False

    def attack(self) -> str:
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."
