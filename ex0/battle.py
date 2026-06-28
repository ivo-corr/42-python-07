from creatures import CreatureFactory, FlameFactory, AquaFactory


def test_factory(fac: CreatureFactory):
    base_creature = fac.create_base()
    evolved_creature = fac.create_evolved()
    base_creature.describe()
    base_creature.attack()
    evolved_creature.describe()
    evolved_creature.attack()


def fight(fac_one: CreatureFactory, fac_two: CreatureFactory):
    pass


def main() -> None:
    print("Testing factory")
    f_fac = FlameFactory()
    test_factory(f_fac)
    print("Testing factory")
    a_fac = AquaFactory()
    test_factory(a_fac)


if __name__ == "__main__":
    main()
