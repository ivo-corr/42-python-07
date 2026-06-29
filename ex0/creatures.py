from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

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
        return (Flameling("Flamey", "Flameling"))

    def create_evolved(self) -> Creature:
        return (Pyrodon("Pyrite", "Pyrodon"))


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return (Aquabub("Aqui", "Aquabub"))

    def create_evolved(self) -> Creature:
        return (Torragon("Tor", "Torragon"))


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
