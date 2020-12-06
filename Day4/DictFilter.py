import re
from typing import Dict


def is_int(s: str) -> bool:
    try:
        int(s)
    except ValueError:
        return False
    return True


class DictFilter:
    _ecl = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    _hgt = re.compile(r"(\d+)(cm|in)")
    _hcl = re.compile(r"#[0-9a-f]{6}")
    _pid = re.compile(r"^\d{9}$")

    def __call__(self, d: Dict[str, str]) -> bool:
        return all([self.__getattribute__(k)(v) for k, v in d.items()])

    def eyr(self, s: str) -> bool:
        return is_int(s) and int(s) in range(2020, 2031)

    def byr(self, s: str) -> bool:
        return is_int(s) and int(s) in range(1920, 2003)

    def iyr(self, s: str) -> bool:
        return is_int(s) and int(s) in range(2010, 2021)

    def pid(self, s:str) -> bool:
        return bool(self._pid.match(s))

    def ecl(self, s: str) -> bool:
        return s in self._ecl

    def hcl(self, s: str) -> bool:
        return bool(self._hcl.match(s))

    def hgt(self, s: str) -> bool:
        m = self._hgt.match(s)
        if not (bool(m) and is_int(m.group(1))):
            return False

        i = int(m.group(1))
        return ((m.group(2) == "cm" and i in range(150, 194)) or
                (m.group(2) == "in" and i in range(59, 77)))

    def cid(self, s: str) -> bool:
        return True

    def is_valid(self):
        return self._valid
