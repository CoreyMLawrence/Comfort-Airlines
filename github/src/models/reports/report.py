from abc import ABC, abstractmethod

class Report(ABC):
    @abstractmethod
    def __init__(self, outfile: str) -> None:
        pass
    
    @abstractmethod
    def __del__(self) -> None:
        pass