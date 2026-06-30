from abc import ABC, abstractmethod
from ex0.creatures import Creature, CreatureFactory


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: Creature) -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self._transformed = 0

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return ("Sproutling uses Vine Whip!")

    def heal(self, target: Creature) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return ("Bloomelle uses Petal Dance!")

    def heal(self, target: Creature) -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        # self._transformed = 0

    def attack(self) -> str:
        if (not self._transformed):
            return ("Shiftling attacks normally.")
        return ("Shiftling performs a boosted strike!")

    def transform(self) -> str:
        if (self._transformed):
            return "Shiftling has already shifted."
        else:
            self._transformed = 1
            return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        if (self._transformed):
            self._transformed = 0
            return "Shiftling returns to normal."
        else:
            return "Shiftling was already normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")

    def attack(self) -> str:
        if (not self._transformed):
            return ("Morphagon attacks normally.")
        return ("Morphagon unleashes a devastating morph strike!")

    def transform(self) -> str:
        if (self._transformed):
            return "Morphagon has already morphed."
        else:
            self._transformed = 1
            return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        if (self._transformed):
            self._transformed = 0
            return "Morphagon stabilizes its form."
        else:
            return "Morphagon is already stable."


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Shiftling())

    def create_evolved(self) -> Creature:
        return (Morphagon())


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Sproutling())

    def create_evolved(self) -> Creature:
        return (Bloomelle())
