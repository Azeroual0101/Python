"""
Strategies module for Exercise 2 - Abstract Strategy
Contains concrete battle strategies for different creature types
"""

from typing import Union
from ex0 import Creature
from ex1.capability import HealCapability, TransformCapability
from .battle_strategy import BattleStrategy, InvalidStrategyError


TransformCreature = Union[Creature, TransformCapability]
HealCreature = Union[Creature, HealCapability]


class NormalStrategy(BattleStrategy):
    """Strategy that simply attacks - suitable for any creature."""

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    """Strategy that transforms, then attacks, then reverts."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this aggressive strategy"
            )
        print(creature.transform())  # type: ignore[attr-defined]
        print(creature.attack())
        print(creature.revert())  # type: ignore[attr-defined]


class DefensiveStrategy(BattleStrategy):
    """Strategy that attacks then heals."""

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                f"for this defensive strategy"
            )
        print(creature.attack())
        print(creature.heal())  # type: ignore[attr-defined]
