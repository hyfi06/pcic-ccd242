from dispenser import TicketDispenserSerial
from utils.elapsed_time.decorators import execution_time
from config import tickets_to_obtain, threads


def worker(dispenser: TicketDispenserSerial):
    for _ in range(tickets_to_obtain*threads):
        ticket = dispenser.get_ticket()
        print(f"Ticket: {ticket}")


@execution_time
def main():
    dispenser = TicketDispenserSerial()
    worker(dispenser)


if __name__ == "__main__":
    main()
