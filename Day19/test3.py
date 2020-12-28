import functools
import re

data = open("input.txt").read().split("\n")

messages = []
dct_rules = {}
summa = 0

istrue = False
for line in data:
    if line == "":
        istrue = True
    elif istrue:
        messages.append(line)
    else:
        k, v = line.split(": ")
        k = int(k)
        if v[0] == '"':
            v = v[1]
            dct_rules[k] = [v]
            continue
        tmp_list = []
        for item in v.split('|'):
            tmp_list.append(tuple(map(int, item.split())))
        dct_rules[k] = tmp_list

def gen_regex(rules, start):
    @functools.lru_cache()
    def rec(start):
        parts = []
        for item in rules[start]:
            if isinstance(item, str):
                parts.append(item)
            else:
                parts.append(''.join(rec(i) for i in item))
        if len(parts) == 1:
            return parts[0]
        return '(?:' + '|'.join(parts) + ')'
    return rec(start)

validator = re.compile('^' + gen_regex(dct_rules, 0) + "$")
for item in messages:
    if bool(re.search(validator, item)):
        summa += 1

print("summa")