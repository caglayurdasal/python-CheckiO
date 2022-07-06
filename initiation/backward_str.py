def backward_string(val: str) -> str:
    reversed = ""
    i = len(val)-1
    while (i >= 0):
        reversed += val[i]
        i -= 1

    return reversed


if __name__ == '__main__':
    print("Example:")
    print(backward_string('val'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string('val') == 'lav'
    assert backward_string('') == ''
    assert backward_string('ohho') == 'ohho'
    assert backward_string('123456789') == '987654321'
    print("Coding complete? Click 'Check' to earn cool rewards!")
