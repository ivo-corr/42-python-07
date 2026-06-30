from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.creatures import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, c: Creature) -> bool:
        ...

    @abstractmethod
    def act(self, c: Creature) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, c: Creature) -> bool:
        return (True)

    def act(self, c: Creature) -> None:
        if (not isinstance(c, Creature)):
            raise Exception(f"Invalid input '{c._name}' "
                            "for this normal strategy")
        print(c.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, c: Creature) -> bool:
        if (isinstance(c, (Creature, TransformCapability))):
            return (True)
        return (False)

    def act(self, c: Creature) -> None:
        if (not isinstance(c, TransformCapability)):
            raise Exception(f"Invalid Creature '{c._name}' "
                            "for this aggressive strategy")
        print(c.transform())
        print(c.attack())
        print(c.revert())


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, c: Creature) -> bool:
        if (isinstance(c, HealCapability)):
            return (True)
        return (False)

    def act(self, c: Creature) -> None:
        if (not isinstance(c, HealCapability)):
            raise Exception(f"Invalid Creature '{c._name}' "
                            "for this defensive strategy")
        print(c.attack())
        print(c.heal(c))
