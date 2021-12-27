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
    return list(build_result(iter(re.findall('\(|\)|[\w\s]+', text)), level))


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


def tree_generator(parseTree, start):
    if len(get_levels(parseTree, 1)) == 0:
        return

    rankInSibling = 0
    for child in get_levels(parseTree, 1):
        rankInSibling += 1
        n = len(get_levels(parseTree, 1))
        newNode = Node(name=child.split(
            ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling)

        start.children.append(newNode)

        tree_traverse(child, start=newNode)
# (xyz)*
# Example:
# text "parse"
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .w at (linewid right of C1.e, $h below C1)
# A1: arrow from C1.e right last box.width*2
# A2: arrow from A1.c right last box.width/2*1.3 then down even with SSL then to SSL.e
# A3: line from SSL.w left even with C1.e then up even with A1 then right to A1.c


def star(nin, nout):
    pass

# (X)?
# Example:
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0:  arrow right $h from C1.e then down 1.25*$h then right $h
# SSL: box "sql_stmt_list" fit
# A1:  arrow right $h then up 1.25*$h then right $h
# A2:  arrow from C1.e right to A1.end


def questionMark(nin, nout):
    pass

# (X|Y)
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .w at (linewid right of C1.e, $h below C1)
# A1: arrow from C1.e right last box.width*2
# A2: arrow from A1.c right last box.width/2*1.3 then down even with SSL then to SSL.e
# A3: line from SSL.w left even with C1.e then up even with A1 then right to A1.c


def eitherOr(nin, nout):
    pass

# (XY) chain
# text "parse"
# linerad = 10px
# # linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linewid
# B1: box "XYZ" fit
# A1: arrow right linewid
# B2: box "ZYXXYZ" fit
# A2: arrow right linewid


def chain(nin, nout):
    pass
