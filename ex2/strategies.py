from abc import ABC, abstractmethod
from ex0.creatures import Creature
from ex1.creatures import TransformCapability, HealCapability


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, c: Creature) -> bool:
        ...

    @abstractmethod
    def act(self) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, c: Creature) -> bool:
        return (True)

    def act(self, c: Creature):
        if (type(c) is not Creature):
            raise Exception(f"Invalid input '{c}' "
                            "for this normal strategy")
        c.attack()


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, c: Creature) -> bool:
        if (type(c) is Creature & TransformCapability):
            return (True)
        return (False)

    def act(self, c: Creature | TransformCapability):
        if (type(c) is not TransformCapability):
            raise Exception(f"Invalid Creature '{c}' "
                            "for this aggressive strategy")
        c.transform()
        c.attack()
        c.revert()


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, c: Creature) -> bool:
        if (type(c) is HealCapability):
            return (True)
        return (False)

    def act(self, c: Creature | HealCapability):
        if (type(c) is not HealCapability):
            raise Exception(f"Invalid Creature '{c}' "
                            "for this defensive strategy")
        c.attack()
        c.heal()
