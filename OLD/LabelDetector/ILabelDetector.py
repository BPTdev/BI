from abc import ABC, abstractmethod


class ILabelDetector(ABC):
    @abstractmethod
    def analyze(self, remote_full_path: str, max_labels: int = 10, min_confidence_level: float = 90) -> str:
        pass
