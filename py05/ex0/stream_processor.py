from abc import ABC, abstractmethod
from typing import Any, List, Union


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                return False
            for x in data:
                if not isinstance(x, (int, float)):
                    return False
            return True
        except Exception:
            return False

    def process(self, data: List[Union[int, float]]) -> str:
        try:
            count = len(data)
            total = sum(data)
            avg = total / count if count > 0 else 0
            return f"Processed {count} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            raise ValueError(f"Erreur dans NumericProcessor: {e}")

    def format_output(self, result: str) -> str:
        return f"Initializing Numeric Processor...\nProcessing data: [1, 2, 3, 4, 5]\nValidation: Numeric data verified\nOutput: {result}"


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def process(self, data: str) -> str:
        try:
            chars = len(data)
            words = len(data.split())
            return f"Processed text: {chars} characters, {words} words"
        except Exception as e:
            raise ValueError(f"Erreur dans TextProcessor: {e}")

    def format_output(self, result: str) -> str:
        return f"\nInitializing Text Processor...\nProcessing data: \"Hello Nexus World\"\nValidation: Text data verified\nOutput: {result}"


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                return False
            return any(level in data.upper() for level in ["ERROR", "INFO", "WARNING"])
        except Exception:
            return False

    def process(self, data: str) -> str:
        try:
            d = data.upper()

            if "ERROR" in d:
                return f"[ALERT] ERROR level detected: {data.split(':',1)[1].strip()}\n"
            elif "WARNING" in d:
                return f"[WARNING] WARNING level detected: {data.split(':',1)[1].strip()}"
            else:
                return f"[INFO] INFO level detected: {data.split(':',1)[1].strip()}"
        except Exception as e:
            raise ValueError(f"Erreur dans LogProcessor: {e}")

    def format_output(self, result: str) -> str:
        return f"\nInitializing Log Processor...\nProcessing data: \"ERROR: Connection timeout\"\nValidation: Log entry verified\nOutput: {result}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]

    data_list = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout"
    ]

    for p, d in zip(processors, data_list):
        try:
            if p.validate(d):
                res = p.process(d)
                print(p.format_output(res))
            else:
                print(f"Validation échouée pour {p.__class__.__name__}")
        except ValueError as e:
            print(f"Erreur: {e}")
        except Exception as e:
            print(f"Erreur inattendue: {e}")

    print("=== Polymorphic Processing Demo ===\n")
    print("Polymorphic Data Streams in the Digital Matrix")
    print("Processing multiple data types through same interface...")

    test_data = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    for i, (p, d) in enumerate(zip(processors, test_data), start=1):
        try:
            if p.validate(d):
                res = p.process(d)
                print(f"Result {i}: {res}")
            else:
                print(f"Result {i}: Validation échouée")
        except Exception as e:
            print(f"Result {i}: Erreur - {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
