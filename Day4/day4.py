from typing import List, Dict
from Day4.DictFilter import DictFilter

key_filter_ = {"ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"}


def prepare():
    # prepare list of data from file
    s = str()
    with open("input.txt") as f:
        s = f.read()
    return s


# took me some time for this huge list comprehension
def parse_passports(s: str):
    return [{k: v for k, v in (pair.split(":") for pair in item)} for item in
            [line.replace("\n", " ").split(" ") for line in s.split("\n\n")]]


def get_valid_passports(lop: List[Dict[str, str]], _filter=None) -> int:
    valid = 0
    for passport in lop:
        k = passport.keys()
        v = bool(k >= key_filter_)
        if v and (not _filter or _filter(passport)):
            valid += 1
    return valid


def main():
    s = prepare()
    lop = parse_passports(s)

    print("Part One: {} passports are valid".format(get_valid_passports(lop)))
    df = DictFilter()
    print("Part Two: {} passports are valid".format(get_valid_passports(lop, df)))


if __name__ == "__main__":
    main()
