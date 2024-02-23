import threading


class TicketDispenserConcurrent:
    def __init__(self) -> None:
        self.ticket_number: int = 0
        self.lock = threading.Lock()

    def get_ticket(self) -> int:
        # with self.lock:
        self.lock.acquire()
        try:
            self.ticket_number += 1
            return self.ticket_number
        finally:
            self.lock.release()


class TicketDispenserSerial:
    def __init__(self) -> None:
        self.ticket_number: int = 0

    def get_ticket(self) -> int:
        self.ticket_number += 1
        return self.ticket_number
