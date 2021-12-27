import utility
from random import randrange


class Pic:
    def __init__(self, name='placeholder', nBox=0,
                 nArrow=0, nLine=0, startNode=None):
        self.name = name
        self.nBox = nBox
        self.nArrow = nArrow
        self.nLine = nLine
        self.startNode = startNode
        self.__config = '$h = 0.21\nlinerad = 10px\nlinewid *= 0.5\n'
        self.pik = ''
        pik1 = ''

    def tree_traverse(self, start, pik):
        # print('before', pik)
        pik += start.pikchr()
        # print('after', pik)
        if len(start.children) == 0:
            return
        # print('current at', start)
        # print('inp', start.inp)
        # print('outp', start.outp)

        for child in start.children:
            # pik += child.pikchr()
            self.tree_traverse(child, pik)

    def paint(self):
        pik = ''
        pik += self.__config
        self.tree_traverse(self.startNode, pik)
        self.pik = pik
        # return self.pik
        return self.pik


def rand():
    return randrange(10000)


class Node:
    def __init__(self, name='placeholder',
                 parent=None, children=[], child_rel=None,
                 inp=None, outp=None, level=None):
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
        # print('current at', self.name)
        # print(self.parent.outp)
        self.inp = self.parent.outp
        pik = ''
        r = rand()
        pik += 'A' + str(r) + ': ' + 'arrow linerad from ' + self.inp + '\n'
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        pik += 'L' + str(r) + ': ' + 'line linerad\n'
        self.outp = 'L' + str(r)
        return pik


class startNode(Node):
    def pikchr(self):
        pik = ''
        pik += 'text ' + '\"' + self.name + '\"' + '\n'
        pik += 'circle radius 10%\n'
        r = rand()
        pik += 'L' + str(r) + ': ' + 'line right linerad'
        self.outp = 'L' + str(r)
        return pik


class starNode(Node):
    def pikchr(self):
        self.inp = self.parent.outp
        pik = ''
        r = rand()
        pik += 'A' + str(r) + ': ' + 'arrow linerad from ' + self.inp + '\n'

        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + \
            '\" fit with .w at (linewid right of ' + \
            self.inp + '.e , $h below' + self.inp + ')\n'

        pik += 'L' + str(r) + ': ' + 'line linerad from ' + \
            'A' + str(r) + '.e right last box.width*2\n'

        # pik += 'A' + rand()
        self.outp = 'L' + str(r)
        return pik
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .w at (linewid right of C1.e, $h below C1)
# A1: arrow from C1.e right last box.width*2
# A2: arrow from A1.c right last box.width/2*1.3 then down even with SSL then to SSL.e
# A3: line from SSL.w left even with C1.e then up even with A1 then right to A1.c


class oneOrZero(Node):
    def pikchr(self):
        self.inp = self.parent.outp
        pik = ''
        r = rand()
        pik += 'A' + str(r) + ': ' + 'arrow linerad from ' + self.inp + '\n'
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        pik += 'L' + str(r) + ': ' + 'line linerad\n'
        self.outp = 'L' + str(r)
        return pik


class endNode(Node):
    def pikchr(self):
        self.inp = self.parent.outp
        pik = ''
        r = rand()
        pik += 'A' + str(r) + ': ' + 'arrow linerad from ' + self.inp + '\n'
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        pik += 'A' + str(r) + ': ' + 'arrow linerad\n'
        pik += 'circle radius 10%\n'
        return pik


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


# def tree_traverse(start):

#     if len(start.children) == 0:
#         return
#     for child in start.children:
#         tree_traverse(child)


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
    # prim_expr = parseRuleList['prim_expr']

    startNode = startNode(name='venn_op', parent=None, level=1)

    # utility.testIfValidAndReturnLevel('venn_op', venn_op)
    try:
        tree_generator(venn_op, start=startNode)
    except:
        print('Tree Generation Failed')

    # tree_traverse(startNode)

    # print(startNode.pikchr())
    # print(startNode.outp)
    # print(startNode.pikchr())
    # print(startNode.children[0].children[0].parent)
    # print(startNode.children[0].parent.children)
    # print(startNode.children[0].parent.outp)
    # print(startNode.children[0].pikchr())
    # print(startNode.children[0].children[0].inp)

    # print(startNode.children[0].children)
    testpic = Pic(name='test', startNode=startNode)

    # print(testpic)
    # print(testpic.pik)
    print(testpic.paint())
