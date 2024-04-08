from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def generate(filepath: str) -> None:
        pass