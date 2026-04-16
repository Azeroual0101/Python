#!/usr/bin/env python3
"""
Test script for Exercise 1 - Capabilities
"""

from ex1 import HealingCreatureFactory, TransformCreatureFactory


def test_healing(factory):
    # Base creature
    base_heal = factory.create_base()
    print(f"base: {base_heal.describe()}")
    print(base_heal.attack())
    print(base_heal.heal())

    # Evolved creature
    evolved_heal = factory.create_evolved()
    print(f"evolved: {evolved_heal.describe()}")
    print(evolved_heal.attack())
    print(evolved_heal.heal())


def test_transform(factory):
    # Base creature
    base_transform = factory.create_base()
    print(f"base:\n {base_transform.describe()}")
    print(base_transform.attack())
    print(base_transform.transform())
    print(base_transform.attack())
    print(base_transform.revert())

    # Evolved creature
    evolved_transform = factory.create_evolved()
    print(f"evolved:\n {evolved_transform.describe()}")
    print(evolved_transform.attack())
    print(evolved_transform.transform())
    print(evolved_transform.attack())
    print(evolved_transform.revert())


def main():
    print("Testing Creature with healing capability")
    healing_factory = HealingCreatureFactory()
    test_healing(healing_factory)

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    test_transform(transform_factory)


if __name__ == "__main__":
    try:
        print()
        main()
        print()
    except Exception as e:
        print(e)
