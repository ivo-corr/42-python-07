from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature):
        ...


class TransformCapability(ABC):
    def __init__(self):
        self._transformed = 0

    @abstractmethod
    def transform(self):
        ...

    @abstractmethod
    def revert(self):
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def heal(self, target: Creature) -> str:
        return f"{self.name} healed {target.name}"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def transform(self):
        if (self._transformed):
            return f"{self.name} has already transformed"
        else:
            self._transformed = 1
            return f"{self.name} shifts into a sharper form!"

    def revert(self):
        if (self._transformed):
            self._transformed = 0
            return f"{self.name} has reverted"
        else:
            return "some text"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self):
        if (self._transformed):
            return f"{self.name} has already transformed"
        else:
            self._transformed = 1
            return f"{self.name} shifts into a sharper form!"

    def revert(self):
        if (self._transformed):
            self._transformed = 0
            return f"{self.name} has reverted"
        else:
            return "some text"


class TransformCreatureFactory(CreatureFactory):
    def create_base():
        return (Shiftling())

    def create_evolved():
        return (Morphagon())


class HealingCreatureFactory(CreatureFactory):
    def create_base():
        return (Sproutling())

    def create_evolved():
        return (Bloomelle())


def main():
    hcfac = HealingCreatureFactory()
    hc_base = hcfac.create_base()
    hc_evolved = hcfac.create_evolved()
    print("Testing Creature with healing capability")
    print("\tbase:")
    hc_base.describe()
    hc_base.attack()
    hc_base.heal()
    print("\tevolved:")
    hc_evolved.describe()
    hc_evolved.attack()
    hc_evolved.heal()
    tcfac = TransformCreatureFactory()
    tc_base = tcfac.create_base()
    tc_evolved = tcfac.create_evolved()
    print("\tbase:")
    tc_base.describe()
    tc_base.attack()
    tc_base.transform()
    tc_base.attack()
    tc_base.revert()
    print("\tevolved:")
    tc_evolved.describe()
    tc_evolved.attack()
    tc_evolved.transform()
    tc_evolved.attack()
    tc_evolved.revert()


if __name__ == "__main__":
    main()
