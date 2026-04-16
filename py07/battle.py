from ex0 import FlameFactory, AquaFactory


def test(factory):
    base = factory.create_base()
    print(base.describe())
    print(base.attack())

    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())
    print()


def main() -> None:
    print("Testing factory")
    Flame = FlameFactory()
    test(Flame)

    print("Testing factory")
    Aqua = AquaFactory()
    test(Aqua)

    print("Testing battle")
    flaming = Flame.create_base()
    aquabub = Aqua.create_base()

    print(flaming.describe())
    print("vs")
    print(aquabub.describe())
    print("fight!")
    print(flaming.attack())
    print(aquabub.attack())


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)