import re

from typing import List

reg = re.compile(r"([FB]+)([RL]+)")


def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def binary_search(s: str, start: int, stop: int):
    # print(s, start, stop)
    if not s:
        return start

    half = int((stop - start) / 2)
    if s[0] in {"F", "L"}:
        return binary_search(s[1:], start, start + half)
    if s[0] in {"B", "R"}:
        return binary_search(s[1:], start + half, stop)


def get_seat_ids(lol: List[str]) -> List[int]:
    return [binary_search(m.group(1), 0, 128) * 8 + binary_search(m.group(2), 0, 8) for m in
            (reg.match(line) for line in lol)]


def find_seat(seats: List[int], _max: int) -> int:
    sos = set(seats)
    for i in range(_max):
        if i not in sos and i - 1 in sos and i + 1 in sos:
            return i
    return -1


def main():
    # list of lines
    lol = prepare().split("\n")

    seats = get_seat_ids(lol)
    _max = max(seats)
    print("The highest seat ID is: {}".format(_max))
    print("The ID of my seat is: {}".format(find_seat(seats, _max)))


if __name__ == "__main__":
    main()
