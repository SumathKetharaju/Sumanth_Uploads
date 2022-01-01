import sys
DIGIT_MAP = {
    "zero": '0',
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7'
}


def convert(s):
    # if not isinstance(s,list):
        # raise TypeError("argument must be a list")

    try:
        number = ' '
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)

    except(KeyError, TypeError) as e:
        print(f"conversion error:{e!r}",file=sys.stderr)
        # raise
        return -1


convert("fail".split())