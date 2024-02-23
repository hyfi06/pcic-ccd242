import hashlib
import time


def proof_of_work(input_data: str, difficulty: int = 4) -> int:
    """
    Realiza una prueba de trabajo sobre la entrada dada, buscando un nonce tal que
    el hash SHA-256 de (input_data + nonce) comience con 'difficulty' número de ceros.

    :param input_data: Los datos de entrada para la prueba de trabajo.
    :param difficulty: La dificultad de la prueba, definida como el número de ceros
                       al inicio del hash.
    :return: El nonce que resuelve la prueba de trabajo.
    """
    nonce = 0
    start_time = time.time()
    # El objetivo hash debe comenzar con 'difficulty' ceros.
    target = '0' * difficulty

    while True:
        # Concatena la entrada con el nonce actual y calcula el hash SHA-256.
        input_with_nonce = f"{input_data}{nonce}".encode()
        hash_result = hashlib.sha256(input_with_nonce).hexdigest()

        # Verifica si el hash cumple con la dificultad requerida.
        if hash_result.startswith(target):
            end_time = time.time()
            print(f"Nonce: {nonce}")
            print(f"Hash: {hash_result}")
            print(f"Tiempo tomado: {end_time - start_time} segundos")
            return nonce

        nonce += 1


# Uso de la función
if __name__ == "__main__":
    input_data = "Hola, mundo!"
    difficulty = 4  # Ajusta este valor para cambiar la dificultad
    nonce = proof_of_work(input_data, difficulty)
