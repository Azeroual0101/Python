from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        """Retourne une instance de la créature de base"""
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        """Retourne une instance de la créature évoluée"""
        pass
