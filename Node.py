import utility


class Pic:
    def __init__(self, name='placeholder', nBox=0, nArrow=0, nLine=0):
        self.name = name
        self.nBox = nBox
        self.nArrow = nArrow
        self.nLine = nLine


class Node:
    def __init__(self, name='placeholder', parent=None, children=[], child_rel=None, inp=None, outp=None, level=None):
        self.name = name
        self.parent = parent
        self.children = children
        self.child_rel = child_rel  # either or, chain
        self.inp = inp
        self.outp = outp
        self.level = level

    def __repr__(self):
        return self.name

    def pikchr(self):
        pik = ''
        pik = pik + 'Box'


class startNode(Node):
    def __init__():
        pass


class starNode(Node):
    def __init__():
        pass


class endNode(Node):
    def __init__():
        pass


class eitherOrNode(Node):
    def __init__():
        pass


def tree_generator(parseTree, start):
    if len(utility.get_levels(parseTree, 1)) == 0:
        return

    for child in utility.get_levels(parseTree, 1):
        newNode = Node(name=child.split(
            ' ')[0], children=[], parent=start, level=start.level+1)
        start.children.append(newNode)
        tree_generator(child, start=newNode)


def tree_traverse(start):
    if len(start.children) == 0:
        return
    for child in start.children:
        tree_traverse(child)


if __name__ == '__main__':
    t = open('./ApplEdible.txt', mode='r', encoding='utf8')
    treeRaw = t.read()
    t.close()
    treeSplit = treeRaw.split('parserRuleSpec')
    parseRuleList = {}
    for parseRule in treeSplit:
        parseRuleName = parseRule.split(' ')[1]
        parseRuleList[parseRuleName] = utility.cleanParseRule(parseRule)

    venn_op = parseRuleList['venn_op']
    prim_expr = parseRuleList['prim_expr']

    startNode = Node(name='venn_op', parent=None, level=1)
    # utility.testIfValidAndReturnLevel('venn_op', venn_op)
    try:
        tree_generator(venn_op, start=startNode)
    except:
        print('Tree Generation Failed')
    tree_traverse(startNode)
