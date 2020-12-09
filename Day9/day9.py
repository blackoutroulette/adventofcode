from typing import List, Final


def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def two_sum(lon: List[int], target: int) -> bool:
    while len(lon) > 1:
        lon = filter_list(lon, lon[0], target)
        i: int = lon.pop(0)
        for k in reversed(lon):
            _sum: int = i + k

            if _sum == target:
                return True

            if _sum < target:
                break
    return False


def filter_list(lon: List[int], _min: int, target: int) -> List[int]:
    _max: Final[int] = target - _min
    for i in range(len(lon) - 1, 0, -1):
        n = lon[i]
        if n <= _max:
            return lon[:i + 1]
    return lon


def find_number(li: List[int]) -> int:
    preamble = 25

    for i, num in enumerate(li[preamble:]):
        p = li[i:i + preamble]
        p.sort()
        if not two_sum(p, num):
            return num
    return -1


def find_contiguous_set(li: List[int], target: int) -> int:
    for i in range(len(li)):
        l = list()
        sum_ = 0
        for num in li[i:]:
            sum_ += num
            l.append(num)
            if sum_ == target:
                l.sort()
                return l[0] + l[-1]

            if sum_ > target:
                break
    return -1


def main():
    s = prepare()
    li = [int(st) for st in s.split("\n")]
    n = find_number(li)
    print("Part One: {}".format(n))
    print("Part Two: {}".format(find_contiguous_set(li, n)))


if __name__ == "__main__":
    main()
