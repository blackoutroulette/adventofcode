from typing import List, Final

target = 2020


def find_two_sum(lon: List[int]):
    while len(lon) > 1:
        print(lon)
        filter_list(lon)
        i: Final[int] = lon.pop(0)
        for k in reversed(lon):
            _sum: Final[int] = i + k

            if _sum == target:
                return i, k

            if _sum < target:
                break
    return 0, 0


# remove all numbers x with x > target - min
def filter_list(lon: List[int]):
    _min: Final[int] = lon[0]
    _max: Final[int] = target - _min
    for i in range(len(lon) - 1, 0, -1):
        if lon[i] <= _max:
            del lon[i + 1:]
            return


def prepare():
    # prepare list of data from file
    lon: Final[List[int]] = list()
    with open("Day1/input.txt") as f:
        for line in f:
            lon.append(int(line))

    # sort the list
    lon.sort()
    i, k = find_two_sum(lon)
    print("\nResult: {} + {} = {}\nAnswer: {}".format(i, k, target, k * i))


if __name__ == "__main__":
    prepare()
