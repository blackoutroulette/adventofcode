from typing import List, Set


def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def parse_a(s: str) -> List[Set[str]]:
    return [{c for c in st} for st in (line.replace("\n", "") for line in s.split("\n\n"))]


def parse_b(s: str) -> List[List[Set[str]]]:
    return [[{c for c in st} for st in line.split("\n")] for line in s.split("\n\n")]


def main():
    # list of lines
    s = prepare()
    lol = parse_a(s)
    _sum = sum([len(c) for c in lol])
    print("Part One: {}".format(_sum))

    los = parse_b(s)
    los = [li[0].intersection(*li[1:]) for li in los]
    _sum = sum([len(c) for c in los])
    print("Part Two: {}".format(_sum))


if __name__ == "__main__":
    main()
