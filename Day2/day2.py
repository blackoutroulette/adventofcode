import re


def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def parse(s: str) -> list:
    reg = re.compile(r"(\d+)-(\d+)\s(\w):\s(\w+)")
    return reg.findall(s)


def find_valid_passwords_a(lom: list) -> int:
    valid = 0
    for tup in lom:
        _min, _max, char, pw = tup
        if pw.count(char) in range(int(_min), int(_max) + 1):
            valid += 1
    return valid


def find_valid_passwords_b(lom: list) -> int:
    valid = 0
    for tup in lom:
        pos1, pos2, char, pw = tup
        pos1 = int(pos1)-1
        pos2 = int(pos2)-1
        if (pw[pos1] == char != pw[pos2]) or (pw[pos1] != char == pw[pos2]):
            valid += 1
    return valid


def main():
    s = prepare()
    lom = parse(s)
    a = find_valid_passwords_a(lom)
    b = find_valid_passwords_b(lom)
    print("Part1: {} out of {} passwords are valid".format(a, len(lom)))
    print("Part2: {} out of {} passwords are valid".format(b, len(lom)))


if __name__ == "__main__":
    main()
