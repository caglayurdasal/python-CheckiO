def split_pairs(a):
    i = 0
    res = []
    len_str = len(a)
    while (i < len_str):
        if (i+2 == len_str+1):
            res.append(a[i] + '_')
        else:
            res.append(a[i:i+2])
        i += 2
    return res


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
