def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    max = 0
    occurrences = 0
    occurredWord = ""
    word = str(data)
    for x in data:
        occurrences = word.count(x)
        if (occurrences >= max):
            max = occurrences
            occurredWord = x

    return occurredWord


if __name__ == "__main__":
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))
    print(most_frequent(["a", "a", "bi", "bi", "bi"]))
