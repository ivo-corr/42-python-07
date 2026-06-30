from ex1 import HealingCreatureFactory, TransformCreatureFactory


def main() -> None:
    hcfac = HealingCreatureFactory()
    hc_base = hcfac.create_base()
    hc_evolved = hcfac.create_evolved()
    print("Testing Creature with healing capability")
    print("\tbase:")
    print(hc_base.describe())
    print(hc_base.attack())
    print(hc_base.heal(hc_base))
    print("\tevolved:")
    print(hc_evolved.describe())
    print(hc_evolved.attack())
    print(hc_evolved.heal(hc_base))
    tcfac = TransformCreatureFactory()
    tc_base = tcfac.create_base()
    tc_evolved = tcfac.create_evolved()
    print("\tbase:")
    print(tc_base.describe())
    print(tc_base.attack())
    print(tc_base.transform())
    print(tc_base.attack())
    print(tc_base.revert())
    print("\tevolved:")
    print(tc_evolved.describe())
    print(tc_evolved.attack())
    print(tc_evolved.transform())
    print(tc_evolved.attack())
    print(tc_evolved.revert())


if __name__ == "__main__":
    main()
