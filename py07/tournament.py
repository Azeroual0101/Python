#!/usr/bin/env python3
"""
Tournament script for Exercise 2 - Abstract Strategy
"""

from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError


def battle(opponent1, opponent2):
    """
    Fait combattre deux opposants.
    Chaque opposant est un tuple (factory, strategy)
    """
    # Créer les créatures
    factory1, strategy1 = opponent1
    factory2, strategy2 = opponent2
    
    creature1 = factory1.create_base()
    creature2 = factory2.create_base()
    
    # Vérifier si les stratégies sont valides
    if not strategy1.is_valid(creature1):
        raise InvalidStrategyError(f"Invalid Creature '{creature1.name}' for this aggressive strategy")
    if not strategy2.is_valid(creature2):
        raise InvalidStrategyError(f"Invalid Creature '{creature2.name}' for this defensive strategy")
    
    # Afficher le début du combat (format exact de l'exemple)
    print("* Battle *")
    print(f"{creature1.describe()}")
    print("vs.")
    print(f"{creature2.describe()}")
    print("now fight!")
    
    # Exécuter les stratégies
    strategy1.act(creature1)
    strategy2.act(creature2)


def tournament(opponents):
    """
    Organise un tournoi entre plusieurs opposants.
    Chaque opposant combat tous les autres une fois.
    """
    n = len(opponents)
    print(f"*** Tournament ***")
    print(f"{n} opponents involved")
    print()
    
    for i in range(n):
        for j in range(i + 1, n):
            try:
                battle(opponents[i], opponents[j])
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            print()


def main():
    # Test 0 : combat basique
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    opponents0 = [
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    tournament(opponents0)
    
    # Test 1 : combat avec erreur (AggressiveStrategy sur Flameling)
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents1 = [
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy())
    ]
    tournament(opponents1)
    
    # Test 2 : combat multiple
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents2 = [
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy())
    ]
    tournament(opponents2)


if __name__ == "__main__":
    main()