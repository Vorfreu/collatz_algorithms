from collatz.algorithms import *

numbers_to_test = [10**21]

for i in numbers_to_test:
    print(f"Number checked:{i}")
    print(check_collatz(i))
    print("")