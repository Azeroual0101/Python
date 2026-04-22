# ex3/functools_artifacts.py
from collections.abc import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    if operation == 'add':
        return reduce(operator.add, spells)
    elif operation == 'multiply':
        return reduce(operator.mul, spells)
    elif operation == 'max':
        return reduce(max, spells)
    elif operation == 'min':
        return reduce(min, spells)
    else:
        return 0


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    elements = ['fire', 'ice', 'lightning']
    return {
        element: partial(base_enchantment, 50, element)
        for element in elements
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        return 0
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


@singledispatch
def spell_dispatcher(spell: Any) -> str:
    return "Unknown spell type"


@spell_dispatcher.register(int)
def _(spell: int) -> str:
    return f"Damage spell: {spell} damage"


@spell_dispatcher.register(str)
def _(spell: str) -> str:
    return f"Enchantment: {spell}"


@spell_dispatcher.register(list)
def _(spell: list) -> str:
    return f"Multi-cast: {len(spell)} spells"


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print()

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print()

    print("Testing spell dispatcher...")
    print(spell_dispatcher(42))
    print(spell_dispatcher("fireball"))
    print(spell_dispatcher([1, 2, 3]))
    print(spell_dispatcher(3.14))
