def is_all_upper(text: str) -> bool:
    check = False
    if (text == ''):
        return True
    for ch in text:
        # check if character is a space, integer or uppercase
        if (ch.isspace() or ch.isdigit() or ch.isupper()):
            check = True
        else:
            return False
    return check


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
