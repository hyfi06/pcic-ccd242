import threading
from typing import TypeVar, List
T = TypeVar('T')


class DispenserConcurrent(T):
    def __init__(self, data: List[T]) -> None:
        self.data = data
        self.lock = threading.Lock()

    def get_ticket(self) -> int:
        # with self.lock:
        self.lock.acquire()
        try:
            return self.data.pop()
        finally:
            self.lock.release()


class DispenserSerial:
    def __init__(self) -> None:
        self.ticket_number: int = 0

    def get_ticket(self) -> int:
        self.ticket_number += 1
        return self.ticket_number
