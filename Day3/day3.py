from typing import List


def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def count_trees(lol: List[str], x_step: int, y_step: int) -> int:
    trees = 0
    line_width = len(lol[0])

    x = 0
    for y in range(y_step, len(lol), y_step):
        x = (x + x_step) % line_width
        if lol[y][x] == "#":
            trees += 1
    return trees


def main():
    s = prepare()
    # list of lines
    lol = s.split("\n")

    # part one
    trees = count_trees(lol, 3, 1)
    print("right 3, down 1 = {} trees".format(trees))

    # part two
    calls = [(1, 1), (5, 1), (7, 1), (1, 2)]
    results = list()
    for tup in calls:
        x, y = tup
        result = count_trees(lol, x, y)
        results.append(str(result))
        print("right {}, down {} = {} trees".format(x, y, result))
        trees *= count_trees(lol, x, y)

    multi = " x ".join(results)
    print("{} = {}".format(multi, trees))


if __name__ == "__main__":
    main()
