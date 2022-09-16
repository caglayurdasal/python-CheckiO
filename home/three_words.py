def checkio(words: str) -> bool:
    numOfWordsInSuccession = 0
    check = 0
    wordList = words.split(" ")

    for word in wordList:
        for letter in word:
            if (letter <= "z" and letter >= "a") or (letter <= "Z" and letter >= "A"):
                check = 1
            else:
                if numOfWordsInSuccession < 3:
                    numOfWordsInSuccession = 0
                    check = 0
                else:
                    return True
        if check:
            numOfWordsInSuccession += 1
    if numOfWordsInSuccession < 3:
        return False
    return True


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    print(checkio("one two 3 four five 6 seven eight 9 ten eleven 12"))
    print("Example:")
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
