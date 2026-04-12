from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict


class DataProcessor(ABC):

    def __init__(self) -> None:
        self.data: list[str] = []
        self.count = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self.data:
            return (1, "No data processed")
        value = self.data.pop(0)
        rank = self.count
        self.count += 1

        return (rank, value)


class NumericProcessor(DataProcessor):

    def validate(self, data) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            for e in data:
                if not isinstance(e, (int, float)):
                    return False
            return True
        return False

    def ingest(self, data):
        if self.validate(data):
            self.data.append(str(data))


class TextProcessor(DataProcessor):

    def validate(self, data: Union[str, List[str]]) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for e in data:
                if not isinstance(e, str):
                    return False
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if self.validate(data):
            self.data.append(str(data))


class LogProcessor(DataProcessor):

    def validate(
        self,
        data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> bool:

        if isinstance(data, dict):
            for k, v in data.items():
                if not (isinstance(k, str) and isinstance(v, str)):
                    return False
            return True

        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                for k, v in d.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
            return True

        return False

    def ingest(
        self,
        data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:

        if self.validate(data):
            self.data.append(str(data))


if __name__ == "__main__":

    numb = LogProcessor()
    nbrs = {"a": "Hello Azeroual How are you", "b": "Heloo", "c": "whats"}
    nbrs1 = {"d": "Hello Azeroual How are you", "e": "Heloo", "f": "whats"}
    numb.ingest(nbrs)
    print(numb.output())
    numb.ingest(nbrs1)
    print(numb.output())
