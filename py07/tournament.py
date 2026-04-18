#!/usr/bin/env python3
"""
Tournament script for Exercise 2 - Abstract Strategy.
"""

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
)


def battle(opponent1, opponent2):
    """
    Fait combattre deux opposants.

    Chaque opposant est un tuple (factory, strategy).
    """
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2

    creature1 = factory1.create_base()
    creature2 = factory2.create_base()

    if not strategy1.is_valid(creature1):
        raise InvalidStrategyError(
            f"Invalid creature '{creature1.name}' "
            f"for strategy {strategy1.__class__.__name__}"
        )

    if not strategy2.is_valid(creature2):
        raise InvalidStrategyError(
            f"Invalid creature '{creature2.name}' "
            f"for strategy {strategy2.__class__.__name__}"
        )

    print("* Battle *")
    print(creature1.describe())
    print("vs.")
    print(creature2.describe())
    print("now fight!")

    strategy1.act(creature1)
    strategy2.act(creature2)


def tournament(opponents):
    """
    Organise un tournoi entre plusieurs opposants.

    Chaque opposant combat tous les autres une fois.
    """
    n = len(opponents)

    print("*** Tournament ***")
    print(f"{n} opponents involved")
    print()

    for i in range(n):
        for j in range(i + 1, n):
            try:
                battle(opponents[i], opponents[j])
            except InvalidStrategyError as error:
                print(f"Battle error, aborting tournament: {error}")
                return
            print()


def main():
    """Point d'entrée principal avec différents tests."""
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")

    opponents0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    tournament(opponents0)

    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")

    opponents1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ]
    tournament(opponents1)

    print("Tournament 2 (multiple)")
    print(
        "[ (Aquabub+Normal), (Healing+Defensive), "
        "(Transform+Aggressive) ]"
    )

    opponents2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ]
    tournament(opponents2)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
