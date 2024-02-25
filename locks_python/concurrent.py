import sys
import threading
from dispenser import ConcurrentDispenser
from elapsed_time.decorators import execution_time
from elapsed_time.tools import print_seconds
from config import data_len, threads
from work import proof_of_work


def worker(dispenser: ConcurrentDispenser, workerName: int) -> None:
    try:
        while True:
            data: str = dispenser.next()
            nonce, hash_result, seconds = proof_of_work(data)
            # print(
            #     f"Worker {workerName}: {data} -> {hash_result} with {nonce} in {seconds} s")
    finally:
        return


@execution_time(print_seconds)
def main(threads_num: int, length: int):
    dispenser = ConcurrentDispenser(list(range(length)))
    threads = []
    for i in range(threads_num):
        thread = threading.Thread(target=worker, args=(dispenser, i))
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()


if __name__ == "__main__":
    threads_num = threads
    length = data_len
    try:
        threads_num = int(sys.argv[1])
        length = int(sys.argv[2])
    except IndexError:
        pass
    main(threads_num, length)
