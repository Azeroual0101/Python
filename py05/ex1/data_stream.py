from abc import ABC, abstractmethod
from typing import Any, List, Tuple, Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.data: List[str] = []
        self.total_processed: int = 0
        self.rank: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> None:
        pass

    def output(self) -> Tuple[int, str]:
        if not self.data:
            return (0, "No data")

        value = self.data.pop(0)
        rank = self.rank
        self.rank += 1

        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(x, (int, float)) for x in data)
        return False

    def process(self, data: Any) -> None:
        if not self.validate(data):
            return
        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
                self.total_processed += 1
        else:
            self.data.append(str(data))
            self.total_processed += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def process(self, data: Any) -> None:
        if not self.validate(data):
            return
        if isinstance(data, list):
            for item in data:
                self.data.append(str(item))
                self.total_processed += 1
        else:
            self.data.append(str(data))
            self.total_processed += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def check(d):
            for k, v in d.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True

        if isinstance(data, dict):
            return check(data)
        if isinstance(data, list):
            return all(isinstance(x, dict) and check(x) for x in data)
        return False

    def process(self, data: Any) -> None:
        if not self.validate(data):
            return
        if isinstance(data, dict):
            formatted = f"{data.get('log_level')}: {data.get('log_message')}"
            self.data.append(formatted)
            self.total_processed += 1
        else:
            for d in data:
                formatted = f"{d.get('log_level')}: {d.get('log_message')}"
                self.data.append(formatted)
                self.total_processed += 1


class ExportPlugin(Protocol):
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        pass


class CSVPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("CSV Output:")
        row = []
        for _, value in data:
            row.append(value)
        print(",".join(row))


class JSONPlugin:
    def process_output(self, data: List[Tuple[int, str]]) -> None:
        print("JSON Output:")
        result = {}

        for i, (_, value) in enumerate(data, start=1):
            result[f"item_{i}"] = value

        print(result)


class DataStream:
    def __init__(self) -> None:
        self.processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)

    def process_stream(self, stream: List[Any]) -> None:
        for element in stream:
            handled = False

            for proc in self.processors:
                if proc.validate(element):
                    proc.process(element)
                    handled = True
                    break

            if not handled:
                print(
                    f"DataStream error - Can't process element "
                    f"in stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            print(
                f"{proc.__class__.__name__}: "
                f"total {proc.total_processed} items processed, "
                f"remaining {len(proc.data)} on processor"
            )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        collected: List[Tuple[int, str]] = []

        for proc in self.processors:
            for _ in range(min(nb, len(proc.data))):
                collected.append(proc.output())

        plugin.process_output(collected)


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")

    ds = DataStream()

    print("\nInitialize Data Stream...")
    ds.print_processors_stats()

    print("\nRegistering Numeric Processor")
    ds.register_processor(NumericProcessor())

    stream = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print("\nSend first batch of data on stream:", end="")
    print(stream)

    ds.process_stream(stream)
    ds.print_processors_stats()

    print("\nRegistering other data processors")
    ds.register_processor(TextProcessor())
    ds.register_processor(LogProcessor())

    print("Send the same batch again")
    ds.process_stream(stream)
    ds.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    numeric_proc = ds.processors[0]
    text_proc = ds.processors[1]
    log_proc = ds.processors[2]

    for _ in range(3):
        numeric_proc.output()

    for _ in range(2):
        text_proc.output()

    for _ in range(1):
        log_proc.output()

    ds.print_processors_stats()
