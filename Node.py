import utility
from random import randrange


def rand():
    return randrange(10000)


class Pic:
    def __init__(self, name='placeholder', nBox=0,
                 nArrow=0, nLine=0, startNode=None):
        self.name = name
        self.nBox = nBox
        self.nArrow = nArrow
        self.nLine = nLine
        self.startNode = startNode
        self.__config = '$h = 0.5\nlinerad = 10px\nlinewid *= 0.5\n'
        self.pik = ''

    def tree_traverse(self, start, pik):
        # print(start.name, start.olderSibling)
        print(start)
        pik += start.pikchr()
        if len(start.children) != 0:
            for child in start.children:
                pik = self.tree_traverse(child, pik)
        return pik

    def paint(self):
        pik = ''
        pik += self.__config
        self.pik = self.tree_traverse(self.startNode, pik)
        return self.pik

    def save(self, filename):
        pass


class Node:
    def __init__(self, name='placeholder',
                 parent=None, children=[], child_rel=None, sibling=0,
                 olderSibling=None, inp=None, outp=None, level=None):
        self.name = name
        self.parent = parent
        self.children = children
        self.child_rel = child_rel  # either or, chain
        self.inp = inp
        self.outp = outp
        self.level = level
        self.sibling = sibling
        self.olderSibling = olderSibling

    def __repr__(self):
        return self.name

    def pikchr(self):
        # print('current at', self.name)
        # print(self.parent.outp)
        self.inp = self.parent.outp
        pik = ''
        r = rand()

        if self.sibling == 1:
            pik += 'A' + str(r) + ': ' + \
                'arrow linerad from ' + self.inp + '\n'
            pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
            self.box = 'B' + str(r)
            pik += 'L' + str(r) + ': ' + 'line linerad\n'
        else:
            pik += 'B' + str(r) + ': ' + 'box \"' + self.name + \
                '\" fit at $h below ' + self.olderSibling.box + '\n'
            self.box = 'B' + str(r)
            pik += 'arrow from ' + self.inp + ' to ' + self.box + '.w\n'
            pik += 'L' + str(r) + ': ' + \
                'line linerad from ' + self.box + '.e\n'

        self.outp = 'L' + str(r)
        return pik


class startNode(Node):  # DONE
    def pikchr(self):
        pik = ''
        pik += 'text ' + '\"' + self.name + '\"' + '\n'
        pik += 'circle radius 10%\n'
        r = rand()
        pik += 'L' + str(r) + ': ' + 'line right linerad\n'
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

# C1:  circle radius 10%
# A0:  arrow right $h from C1.e then down 1.25*$h then right $h
# SSL: box "sql_stmt_list" fit
# A1:  arrow right $h then up 1.25*$h then right $h
# A2:  arrow from C1.e right to A1.end


class endNode(Node):  # DONE
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
    rankInSibling = 0
    for child in utility.get_levels(parseTree, 1):
        rankInSibling += 1
        if rankInSibling == 1:
            newNode = Node(name=child.split(
                ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling)
        else:
            newNode = Node(name=child.split(
                ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling, olderSibling=brother)
        start.children.append(newNode)
        tree_generator(child, start=newNode)

        if len(utility.get_levels(child, 1)) == 0:
            newEndNode = endNode(name=child.split(
                ' ')[1], children=[], parent=newNode, level=newNode.level+1)
            newNode.children.append(newEndNode)
        brother = newNode


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
    # tree_generator(venn_op, start=startNode)
    testpic = Pic(name='test', startNode=startNode)
    print(testpic.paint())

    # for i in range(10):
    #     print(i, utility.get_levels(venn_op, i))

    # def tree_traverse(start, pik):
    #     # print('before', pik)
    #     pik += start.pikchr()
    #     # print('after', pik)
    #     if len(start.children) != 0:
    #         for child in start.children:
    #             # pik += child.pikchr()
    #             pik = tree_traverse(child, pik)
    #     return pik

    # pik = '$h = 0.21\nlinerad = 10px\nlinewid *= 0.5\n'
    # print(tree_traverse(startNode, pik))
