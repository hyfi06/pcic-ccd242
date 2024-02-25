import sys
from dispenser import SerialDispenser
from elapsed_time.decorators import execution_time
from elapsed_time.tools import print_seconds
from config import data_len
from work import proof_of_work


def worker(dispenser: SerialDispenser) -> None:
    try:
        while True:
            data: str = dispenser.next()
            nonce, hash_result, seconds = proof_of_work(data)
            # print(f"{data} -> {hash_result} with {nonce} in {seconds} s")
    finally:
        return


@execution_time(print_seconds)
def main(length):
    dispenser = SerialDispenser(list(range(length)))
    worker(dispenser)


if __name__ == "__main__":
    length = data_len
    try:
        length = int(sys.argv[1])
    except IndexError:
        pass
    main(length)
