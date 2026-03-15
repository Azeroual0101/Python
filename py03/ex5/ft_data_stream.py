import time
from typing import Generator


PLAYERS: list = ["alice", "bob", "charlie", "diana", "eve",
                 "frank", "grace", "henry", "iris", "jack"]

EVENT_TYPES: list = ["killed monster", "found treasure",
                     "leveled up", "completed quest", "died"]


def pseudo_random(seed: int) -> int:
    seed = (seed * 1664525 + 1013904223) & 0xFFFFFFFF
    return seed


def game_event_stream(total: int) -> Generator:
    seed: int = 42
    for i in range(total):
        seed = pseudo_random(seed)
        player = PLAYERS[seed % len(PLAYERS)]
        seed = pseudo_random(seed)
        level = (seed % 20) + 1
        seed = pseudo_random(seed)
        event = EVENT_TYPES[seed % len(EVENT_TYPES)]
        yield (i + 1, player, level, event)


def high_level_filter(stream: Generator, min_level: int) -> Generator:
    for event in stream:
        if event[2] >= min_level:
            yield event


def event_type_filter(stream: Generator, event_type: str) -> Generator:
    for event in stream:
        if event[3] == event_type:
            yield event


def fibonacci_generator(count: int) -> Generator:
    a: int = 0
    b: int = 1
    for _ in range(count):
        yield a
        a, b = b, a + b


def prime_generator(count: int) -> Generator:
    found: int = 0
    candidate: int = 2
    while found < count:
        is_prime: bool = True
        for divisor in range(2, candidate):
            if candidate % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield candidate
            found += 1
        candidate += 1


def print_sequence(gen: Generator, label: str) -> None:
    values: list = []
    for val in gen:
        values.append(str(val))
    print(f"{label}: {', '.join(values)}")


if __name__ == "__main__":
    try:
        TOTAL_EVENTS: int = 1000

        print("=== Game Data Stream Processor ===")
        print(f"Processing {TOTAL_EVENTS} game events...")
        print()

        start: float = time.time()

        total_processed: int = 0
        high_level_count: int = 0
        treasure_count: int = 0
        levelup_count: int = 0

        stream = game_event_stream(TOTAL_EVENTS)

        for idx, event in enumerate(stream):
            number, player, level, action = event
            total_processed += 1

            if level >= 10:
                high_level_count += 1
            if action == "found treasure":
                treasure_count += 1
            if action == "leveled up":
                levelup_count += 1

            if idx < 3:
                print(
                    f"Event {number}: Player {player} "
                    f"(level {level}) {action}")

        print("...")

        elapsed: float = time.time() - start

        list_events: list = list(game_event_stream(TOTAL_EVENTS))
        list_size: int = len(list_events)
        gen_size: int = 1

        print()
        print("=== Stream Analytics ===")
        print(f"Total events processed: {total_processed}")
        print(f"High-level players (10+): {high_level_count}")
        print(f"Treasure events: {treasure_count}")
        print(f"Level-up events: {levelup_count}")
        print(f"Memory usage (list):      {list_size} events stored in RAM")
        print(
            f"Memory usage (generator): {gen_size} event in memory at a time")
        print(f"Processing time: {elapsed:.3f} seconds")

        print()
        print("=== Generator Demonstration ===")
        print_sequence(
            fibonacci_generator(10), "Fibonacci sequence (first 10)")
        print_sequence(prime_generator(5), "Prime numbers (first 5)")
    except Exception as e:
        print(e)
