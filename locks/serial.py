import sys
from dispenser import TicketDispenserSerial
from utils.elapsed_time.decorators import milis_time
from config import tickets_to_obtain, threads


def worker(dispenser: TicketDispenserSerial, mul: int) -> None:
    for _ in range(tickets_to_obtain*mul):
        ticket = dispenser.get_ticket()
        # print(f"Ticket: {ticket}")


@milis_time
def main(mul):
    dispenser = TicketDispenserSerial()
    worker(dispenser, mul)


if __name__ == "__main__":
    mul = threads
    try:
        mul = int(sys.argv[1])
    except IndexError:
        pass
    main(mul)
