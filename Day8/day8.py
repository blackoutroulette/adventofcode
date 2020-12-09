def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def execute(pos: int, li: list, acc=0, visited=None, trace=None) -> [int, list]:
    if not visited:
        visited = set()
    if not trace:
        trace = list()

    if pos >= len(li):
        return acc, None
    if pos in visited:
        return acc, trace

    op, num = li[pos]
    num = int(num)
    visited.add(pos)
    trace.append((op, num, pos, acc))

    if op == "acc":
        acc += num
        pos += 1
    elif op == "jmp":
        pos += num
    else:
        pos += 1
    return execute(pos, li, acc, visited, trace)


def execute_terminate(trace: list, li: list) -> int:
    for tup in reversed(trace):
        op, num, pos, acc = tup
        if op == "jmp":
            pos += 1
        if op == "nop":
            pos += num
        acc, trc = execute(pos, li, acc)
        if not trc:
            return acc
    return -1


def main():
    s = prepare()

    li = [tuple(st.split(" ")) for st in s.split("\n")]
    acc, trace = execute(0, li)
    print("Part One: {}".format(acc))
    acc = execute_terminate(trace, li)
    print("Part Two: {}".format(acc))


if __name__ == "__main__":
    main()
