def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


def parse(s: str):
    s = s.replace(" bags contain ", ",").replace(" bags", "").replace(" bag", "").replace(", ", ",").replace(".", "")
    list_ = [line.split(",") for line in s.split("\n")]
    dic = dict()
    for li in list_:
        d = dict()
        dic[li[0]] = d
        for el in li[1:]:
            sp = el.split(" ", 1)
            d[sp[1]] = 0 if sp[0] == "no" else int(sp[0])
    return dic


def contains_gold_bag(s: str, d: dict):
    bags = d[s]
    if "shiny gold" in bags:
        return True

    if "other" in bags:
        return False

    return any([contains_gold_bag(bag, d) for bag in bags])


def count_bag_amount(s: str, d: dict):
    bags = d[s]
    if "other" in bags:
        return 1

    su = 0
    for k, v in bags.items():
        rec = count_bag_amount(k, d)
        su += v * rec if rec == 1 else v + (v * rec)
    return su


def main():
    # list of lines
    s = prepare()

    p = parse(s)
    gold = 0
    for bag in p:
        if contains_gold_bag(bag, p):
            gold += 1
    print("Part One: {}".format(gold))
    print("Part Two: {}".format(count_bag_amount("shiny gold", p)))


if __name__ == "__main__":
    main()
