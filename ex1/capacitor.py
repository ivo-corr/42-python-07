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
        super().__init__()

    def heal(self, target: Creature) -> str:
        return f"{self.name} healed {target.name}"

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
            return f"{}"


class Bloomelle(Creature, HealCapability):
    pass


class Shiftling(Creature, TransformCapability):
    pass


class Morphagon(Creature, TransformCapability):
    pass


class TransformCreatureFactory(CreatureFactory):
    pass

class HealingCreatureFactory(CreatureFactory):
    pass
