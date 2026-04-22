# ex4/decorator_mastery.py
from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            if len(args) > 2:
                power = args[2]
            elif 'power' in kwargs:
                power = kwargs['power']
            else:
                return "Insufficient power for this spell"

            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                    else:
                        print(f"Spell failed, retrying... "
                              f"(attempt {attempt}/{max_attempts})")
                        return "Spell casting failed after 3 attempts"
            return "Spell casting failed after 3 attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")
    print()

    print("Testing retrying spell...")

    class AttemptCounter:
        count = 0

    @retry_spell(3)
    def unreliable_spell():
        AttemptCounter.count += 1
        if AttemptCounter.count < 3:
            raise Exception("Spell failed")
        return "Waaaaaaagh spelled !"

    result = unreliable_spell()
    print(result)
    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(guild.validate_mage_name("Gandalf"))
    print(guild.validate_mage_name("A"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 5))
