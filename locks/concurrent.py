import sys
import threading
from dispenser import TicketDispenserConcurrent
from config import tickets_to_obtain, threads
from utils.elapsed_time.decorators import milis_time


def worker(dispenser: TicketDispenserConcurrent, workerName: int) -> None:
    for _ in range(tickets_to_obtain):
        ticket = dispenser.get_ticket()
        # print(f"Worker {workerName} got the ticket {ticket}")


@milis_time
def main(threads_num):
    dispenser = TicketDispenserConcurrent()
    threads = []
    for i in range(threads_num):
        thread = threading.Thread(target=worker, args=(dispenser, i))
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()


if __name__ == "__main__":
    threads_num = threads
    try:
        threads_num = int(sys.argv[1])
    except IndexError:
        pass
    main(threads_num)
