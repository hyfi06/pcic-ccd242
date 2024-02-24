import threading
from typing import TypeVar, List, Generic
T = TypeVar('T')


class DispenserConcurrent(Generic[T]):
    def __init__(self, data: List[T]) -> None:
        self.data: List[T] = data
        self.lock: threading.Lock = threading.Lock()
        self.head = 0

    def next(self) -> T:
        if (self.head < len(self.data)):
            self.lock.acquire()
            try:
                idx = self.head
                self.head += 1
            finally:
                self.lock.release()
            return self.data[self.head]
        else:
            raise IndexError()


class DispenserSerial(Generic[T]):
    def __init__(self, data: List[T]) -> None:
        self.data: List[T] = data

    def next(self) -> T:
        return self.data.pop()
