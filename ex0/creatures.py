from abc import ABC, abstractmethod


class Creature(ABC):
    @abstractmethod
    def attack() -> str:
        ...

    @abstractmethod
    def describe() -> str:
        ...


class CreatureFactory(ABC):
    @abstractmethod
    def create_base() -> Creature:
        ...

    @abstractmethod
    def create_evolved() -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Flameling())

    def create_evolved(self) -> Creature:
        return (Pyrodon())

class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Aquabub())

    def create_evolved(self) -> Creature:
        return (Torragon())


class Flameling(Creature):
    def attack(self) -> str:
        return "Flameling uses Ember!"

    def describe(self) -> str:
        return "Flameling is a Fire type Creature"


class Pyrodon(Creature):
    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"

    def describe(self) -> str:
        return "Pyrodon is a Fire type Creature"


class Aquabub(Creature):
    def attack(self) -> str:
        return "Aquabub uses Water Gun!"

    def describe(self) -> str:
        return "Aquabub is a Water type Creature"


class Torragon(Creature):
    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"

    def describe(self) -> str:
        return "Torragon is a Water type Creature"
