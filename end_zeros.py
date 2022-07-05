def end_zeros(num: int) -> int:
    numZeros = 0
    temp = num
    if (temp % 10 == 0 and temp > 0):
        while(temp % 10 == 0 and temp > 0):
            numZeros += 1
            temp /= 10
    elif (temp == 0):
        numZeros = 1
    return numZeros


if __name__ == "__main__":
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
