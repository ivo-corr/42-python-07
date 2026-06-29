from creatures import CreatureFactory, FlameFactory, AquaFactory


def test_factory(fac: CreatureFactory):
    base_creature = fac.create_base()
    evolved_creature = fac.create_evolved()
    print(base_creature.describe())
    print(base_creature.attack())
    print(evolved_creature.describe())
    print(evolved_creature.attack())


def fight(fac_one: CreatureFactory, fac_two: CreatureFactory):
    base_first = fac_one.create_base()
    base_second = fac_two.create_base()
    print(base_first.describe())
    print("\tvs.")
    print(base_second.describe())
    print("\tfight!")
    print(base_first.attack())
    print(base_second.attack())


def main() -> None:
    print("Testing factory")
    f_fac = FlameFactory()
    test_factory(f_fac)
    print()
    print("Testing factory")
    a_fac = AquaFactory()
    test_factory(a_fac)
    print("\nTesting battle")
    fight(f_fac, a_fac)


if __name__ == "__main__":
    main()
