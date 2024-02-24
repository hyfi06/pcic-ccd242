import hashlib
import time
from typing import Tuple
import config


def proof_of_work(input_data: str, difficulty: int = config.difficulty) -> Tuple[int, str, float]:
    """
    Realiza una prueba de trabajo sobre la entrada dada, buscando un nonce tal que
    el hash SHA-256 de (input_data + nonce) comience con 'difficulty' número de ceros.

    :param input_data: Los datos de entrada para la prueba de trabajo.
    :param difficulty: La dificultad de la prueba, definida como el número de ceros al inicio del hash.
    :return: El nonce que resuelve la prueba de trabajo.
    """
    nonce = 0
    start_time = time.time()
    target = '0' * difficulty

    while True:
        input_with_nonce = f"{input_data}{nonce}".encode()
        hash_result = hashlib.sha256(input_with_nonce).hexdigest()

        if hash_result.startswith(target):
            end_time = time.time()
            seconds = end_time - start_time
            return nonce, hash_result, seconds

        nonce += 1
