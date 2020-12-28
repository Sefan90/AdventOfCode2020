import re

file = open("input.txt","r").readlines()
ruledict = {r[:r.index(":")]:"".join([i for i in r[r.index(":")+1:].replace('"',"").strip()]) for r in file if ":" in r}
messagelist = [r.strip() for r in file if ":" not in r][1:]

def gen_regex(rules, messages):
    def get_regex(s):
        if s == '|':
            return s
        rule = ruledict[s]
        if rule in ["a","b"]:
            return rule
        else:
            return f'({"".join(get_regex(part) for part in rule.split())})'
    
    reg_0 = re.compile("^"+get_regex("0")+"$")
    rules["8"] = "42 | 42 8"
    rules["11"] = "42 31 | 42 11 31"
    reg_42 = re.compile(get_regex("42"))
    reg_31 = re.compile(get_regex("31"))

    part1count = 0
    part2count = 0
    for message in messages:
        pos = 0

        if re.search(reg_0, message):
            part1count += 1

        count_42 = 0
        match = reg_42.match(message, pos)
        while match:
            count_42 += 1
            pos = match.end()
            match = reg_42.match(message, pos)
        
        count_31 = 0
        match = reg_31.match(message, pos)
        while match:
            count_31 += 1
            pos = match.end()
            match = reg_31.match(message, pos)

        if pos == len(message) and 0 < count_31 < count_42:
            part2count += 1
    
    return part1count, part2count
            
part1, part2 = gen_regex(ruledict, messagelist)
print("Part1: "+ str(part1))
print("Part2: "+ str(part2))