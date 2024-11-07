from abc import ABC, abstractmethod


class IDataObject(ABC):
    @abstractmethod
    def does_exist(self, remote_full_path: str) -> bool:
        pass

    @abstractmethod
    def upload(self, file: bytearray) -> None:
        pass

    @abstractmethod
    def download(self, remote_full_path: str, local_file_path: str) -> bytearray:
        pass

    @abstractmethod
    def publish(self, remote_full_path: str, expiration_time: int = 90) -> str:
        pass

    @abstractmethod
    def remove(self, remote_full_path: str, recursive: bool = False) -> None:
        pass
