def prepare():
    with open("input.txt") as f:
        return f.read()


def count_jolts(li: list):
    one_jolt = 0
    three_jolt = 1
    last = 0
    for n in li:
        dif = n - last
        if dif == 1:
            one_jolt += 1
        elif dif == 3:
            three_jolt += 1
        last = n
    return one_jolt * three_jolt


# pretty hard problem i couldn't solve myself in time, solution from
# https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfi8hrt/?context=3
def count_possibilities(arr):
    memo = {0: 1}
    for r in arr:
        memo[r] = memo.get(r - 3, 0) \
                  + memo.get(r - 2, 0) \
                  + memo.get(r - 1, 0)
    return memo[arr[-1]]


def main():
    s = prepare()
    li = [int(st) for st in s.split("\n")]
    li.sort()
    j = count_jolts(li)
    print("Part One: {}".format(j))
    k = count_possibilities(li)
    print("Part Two: {}".format(k))


if __name__ == "__main__":
    main()
