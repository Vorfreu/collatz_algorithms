import time


def check_collatz(number: int, steps: int = 0) -> list:
    # Record the start time
    start_time = time.time()

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = number * 3 + 1

        steps += 1
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time:.10f} seconds")

    return [True, steps]


def check_collatz_binary(number: int) -> list:
    steps = 0

    # Record the start time
    start_time = time.time()

    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = (number * 3 + 1)

        steps += 1

    # Calculate elapsed time
    elapsed_time = time.time() - start_time

    print(f"Time taken: {elapsed_time:.10f} seconds")

    return [True, steps]
