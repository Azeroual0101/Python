from collections.abc import Callable
from typing import Tuple


def spell_combiner(
                spell1: Callable[[str, int], str],
                spell2: Callable[[str, int], str]
                   ) -> Callable[[str, int], Tuple[str, str]]:

    def combined(target: str, power: int) -> Tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:

    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Callable[[str, int], str]
                       ) -> Callable[[str, int], str]:

    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return conditional


def spell_sequence(
                spells: list[Callable[[str, int], str]]
                ) -> Callable[[str, int], list[str]]:
    def sequence(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence


if __name__ == "__main__":
    try:
        def fireball(target: str, power: int) -> str:
            return f"Fireball hits {target} for {power} damage"

        def heal(target: str, power: int) -> str:
            return f"Heal restores {target} for {power} HP"

        combined_spell = spell_combiner(fireball, heal)
        print("Combined spell:", combined_spell("Dragon", 10))

        mega_fireball = power_amplifier(fireball, 3)
        print("Amplified fireball:", mega_fireball("Dragon", 10))

        def is_strong_enough(target: str, power: int) -> bool:
            return power >= 20
        conditional_fireball = conditional_caster(is_strong_enough, fireball)
        print("Conditional (power=15):", conditional_fireball("Dragon", 15))
        print("Conditional (power=25):", conditional_fireball("Dragon", 25))

        sequence_spell = spell_sequence([fireball, heal, mega_fireball])
        print("Spell sequence:", sequence_spell("Goblin", 5))
    except Exception as e:
        print(f"errors :{e}")
