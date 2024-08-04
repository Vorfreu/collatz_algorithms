def check_collatz(number: int, steps: int = 0) -> list:
    if number == 1:
        return [True, steps]

    if number % 2 == 0:
        return check_collatz(number // 2, steps + 1)
    else:
        return check_collatz((number * 3 + 1)//2, steps + 1)

def check_collatz_binary(number:int) -> bool:
    number_new = bin(number)[2:]
    if number_new[-1]==0:
        number_new == number_new >> 1
        if number_new == 1:
            return True
        return check_collatz_binary(number_new)
    else:
        number_new