import re


def build_result(s, l, f=False):
    t = ''
    while (n := next(s, None)) is not None:
        if not l and (not f or n != ')'):
            t += n
        if n == ')':
            break
        if n == '(':
            if not l:
                t += ''.join(build_result(s, l if not l else l-1, l-1 == 0))
            else:
                yield from build_result(s, l if not l else l-1, l-1 == 0)
    yield from ([] if not t else [t])


def get_levels(text, level):
    return list(build_result(iter(re.findall("\(|\)|[!#$%&'()*+,./:;<=>?@\^_`{|}~-]|[\w\s]+", text)), level))


def cleanParseRule(rule: str):
    out = rule.strip().split(' ')[2:-4]
    out = (' '.join(out))
    return out


def testIfValidAndReturnLevel(ruleName: str, rule: str):
    textSplit = rule.split(' ')
    bracket = 0

    maxi = bracket
    # print(test)
    for txt in textSplit:
        if txt.startswith('('):
            bracket += txt.count('(')
            maxi = max(maxi, bracket)
            # print('new level')
        else:
            bracket -= txt.count(')')
            # print('break from current level')
    if bracket != 0:
        print(ruleName, 'Is not a valid parse rule, please check')
    else:
        print(ruleName, 'Is a valid parse rule, please continue')

    return maxi


def visualizeLevel(rule: str):
    textSplit = rule.split(' ')
    level = 0

    for txt in textSplit:
        if txt.startswith('('):
            level += txt.count('(')
            print(' '*level, txt)
        else:
            print(' '*level, txt)
            level -= txt.count(')')
            # print('break from current level')


def visualize_all(all_rule: dict):
    for ruleName in all_rule.keys():
        print('-----------------------')
        print(ruleName)
        visualizeLevel(all_rule[ruleName])


def get_tree(startNode):
    pass
