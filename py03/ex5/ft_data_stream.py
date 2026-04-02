import random
from typing import Generator


def generate_stream() -> Generator[tuple[str, str], None, None]:
    names = ["alice", "bob", "charlie", "dylan"]
    acts = ["run", "eat", "sleep", "grab",
            "move", "climb", "swim", "release", "use"]

    while True:
        player = random.choice(names)
        action = random.choice(acts)
        yield (player, action)


def consume_stream(data: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while len(data) > 0:
        i = random.randint(0, len(data) - 1)
        value = data.pop(i)
        yield value


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = generate_stream()

    for i in range(1000):
        ev = next(stream)
        print(f"Event {i}: Player {ev[0]} did action {ev[1]}")


    buffer = []
    for i in range(10):
        buffer.append(next(stream))

    print(f"Built list of 10 events: {buffer}")


    consumer = consume_stream(buffer)
    for ev in consumer:
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {buffer}")


if __name__ == "__main__":
    main()
