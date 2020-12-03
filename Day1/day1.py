from typing import List, Final

target = 2020


def two_sum(lon: List[int]):
    while len(lon) > 1:
        lon = filter_list(lon, lon[0])
        i: int = lon.pop(0)
        for k in reversed(lon):
            _sum: int = i + k

            if _sum == target:
                return i, k

            if _sum < target:
                break
    return 0, 0


def three_sum(lon: List[int]):
    while len(lon) > 2:
        lon = filter_list(lon, lon[0] + lon[1])
        iv: int = lon.pop(0)
        for k in range(len(lon)):
            for l in range(len(lon)-1, k, -1):
                kv = lon[k]
                lv = lon[l]
                _sum: int = iv + kv + lv

                if _sum == target:
                    return iv, kv, lv

                if _sum < target:
                    break
    return 0, 0, 0


# most of the numbers can be filtered under the assumption
# that for 2 sum: {x | x∈ Numbers : target < x + min} can be removed
# and for 3 sum: {x | ∀n∈ Numbers ∃m1,m2∈ Numbers : m1 ≤ m2 ≤ n ⋀ m1 ≠ m2 ≠ n ⋀ target < x + m1 + m2}
# can be removed
def filter_list(lon: List[int], _min: int) -> List[int]:
    _max: Final[int] = target - _min
    for i in range(len(lon) - 1, 0, -1):
        n = lon[i]
        if n <= _max:
            return lon[:i + 1]
    return lon


def prepare():
    # prepare list of data from file
    lon: Final[List[int]] = list()
    with open("Day1/input.txt") as f:
        for line in f:
            lon.append(int(line))

    # sort the list
    lon.sort()
    i, k = two_sum(lon)
    print("\n2 Sum: {} + {} = {}\nAnswer: {}".format(i, k, target, k * i))
    i, k, l = three_sum(lon)
    print("\n3 Sum: {} + {} + {} = {}\nAnswer: {}".format(i, k, l, target, k * i * l))


if __name__ == "__main__":
    prepare()
