import utility
from random import randrange


def rand():
    return randrange(10000)


class Pic:
    def __init__(self, name='placeholder', startNode=None):
        self.name = name
        self.depth = 0
        self.width = 1
        self.curOffset = 0
        self.startNode = startNode
        self.__config = '$h = 0.5\nlinerad = 20px\nlinewid *= 0.5\n'
        self.pik = ''

    def tree_traverse(self, start):
        # print(start.name, start.olderSibling)
        # print(start)
        if start.sibling == 1:
            self.pik += start.pikchr()
        else:
            self.pik += start.pikchr(offset=start.parent.branchWidth)
            # pik += start.pikchr(offset=self.width)
            # print(start, start.parent.branchWidth)

        if start.sibling != 1:
            start.branchWidth = 1
        if isinstance(start, starNode) or isinstance(start, plusNode) or isinstance(start, questionMarkNode):
            start.branchWidth = 2

        if len(start.children) != 0:
            for child in start.children:
                self.tree_traverse(child)
                if child.sibling == 1:
                    start.branchWidth = child.branchWidth
                else:
                    start.branchWidth += child.branchWidth

    # def tree_traverse(self, start, pik):
    #     # print(start.name, start.olderSibling)
    #     # print(start)
    #     if start.sibling == 1:
    #         pik += start.pikchr()
    #         # if isinstance(start.parent, start)
    #         print(start, start.branchWidth)
    #     else:
    #         # print('before', start, start.parent.branchWidth)
    #         pik += start.pikchr(offset=start.parent.branchWidth)
    #         # pik += start.pikchr(offset=self.width)
    #         print(start, start.branchWidth)

    #     # if len(start.children) != 0:
    #     #     for child in start.children:
    #     #         if child.sibling != 1:
    #     #             self.width += 1
    #     #         if isinstance(child, starNode) or isinstance(child, plusNode) or isinstance(child, questionMarkNode):
    #     #             self.width += 1
    #     #         pik = self.tree_traverse(child, pik)
    #     # else:
    #     #     self.depth = max(self.depth, start.level)  # pic depth
    #     if start.sibling != 1:
    #         self.width += 1
    #         start.parent.branchWidth += 1
    #     if isinstance(start, starNode) or isinstance(start, plusNode) or isinstance(start, questionMarkNode):
    #         self.width += 1
    #         start.parent.branchWidth += 1

    #     if len(start.children) != 0:
    #         for child in start.children:
    #             pik = self.tree_traverse(child, pik)
    #             start.branchWidth += child.branchWidth
    #     else:
    #         start.parent.branchWidth = start.branchWidth

    #     return pik

    def paint(self):
        # pik = ''
        self.pik += self.__config
        self.tree_traverse(self.startNode)
        return self.pik

    def save(self, filename):
        try:
            t = open(filename, mode='w', encoding='utf8')
            treeRaw = t.write(self.paint())
            t.close()
        except:
            print('save failed, print pikchr to terminal')
            print(traceback.print_exc())
            print(self.paint())


class Node:
    def __init__(self, name='placeholder',
                 parent=None, children=[], child_rel=None, sibling=0,
                 olderSibling=None, inp=None, outp=None, level=None,
                 branchWidth=1, ifend=False):
        self.name = name
        self.parent = parent
        self.children = children
        self.child_rel = child_rel  # either or
        self.inp = inp
        self.outp = outp
        self.level = level
        self.sibling = sibling
        self.olderSibling = olderSibling
        self.branchWidth = 1
        self.ifend = ifend

    def __repr__(self):
        return self.name

    def pikchr(self, offset=0):
        # print('current at', self.name)
        # print(self.parent.outp)
        self.inp = self.parent.outp
        pik = ''
        r = rand()

        # if self.sibling == 1:
        #     pik += 'A' + str(r) + ': ' + \
        #         'arrow linerad from ' + self.inp + '\n'
        #     pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        #     self.box = 'B' + str(r)
        #     pik += 'L' + str(r) + ': ' + 'line linerad\n'

        # else:
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + \
            '\" fit with .w at ' + self.inp + \
            '.end+(linerad, -$h*' + str(offset) + ')\n'
        self.box = 'B' + str(r)
        pik += 'arrow from ' + self.inp + ' to ' + self.box + '.w\n'
        pik += 'L' + str(r) + ': ' + \
            'line linerad from ' + self.box + '.e\n'
        if self.ifend:
            pik += 'arrow right linerad\ncircle radius 10%\n'
        else:
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


class starNode(Node):  # DONE Zero or More
    def pikchr(self, offset=0):
        self.inp = self.parent.outp
        pik = ''
        r = rand()

        if self.sibling != 1:
            pik += 'line from ' + self.inp + '.e right linerad/2 then down $h*' + \
                str(offset) + ' then right linerad/2\n'
            pik += 'A' + str(r) + ': ' + 'arrow linerad*2\n'

        else:
            pik += 'A' + str(r) + ': ' + 'arrow linerad*2 from ' + \
                self.inp + '.e\n'

        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + \
            '\" fit with .w at (linerad right of A' + str(r) + \
            '.e , $h below A' + str(r) + ')\n'

        pik += 'A' + str(r+1) + ': arrow from A' + str(r) + \
            '.e right last box.width + 3*linerad\n'
        pik += 'A' + str(r+2) + ': arrow from A' + str(r+1) + \
            '.c right last box.width/2 + linerad/2 then down even with B' + \
            str(r) + ' then to B' + str(r) + '.e\n'
        pik += 'L' + str(r+2) + ': line from B' + str(r) + \
            '.w left even with A' + \
            str(r) + '.c then up even with A' + str(r) + \
            '.c then right to A' + str(r) + '.e\n'

        pik += 'L' + str(r) + ': ' + 'line from A' + \
            str(r+1) + '.e right linerad\n'

        if self.ifend:
            pik += 'arrow right linerad\ncircle radius 10%\n'
        else:
            self.outp = 'L' + str(r)
        return pik

# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .c at (linewid right of A0.e, $h below A0)
# A1: arrow from A0.e right last box.width + 2*linerad
# A2: arrow from A1.c right last box.width/2+linerad/2 then down even with SSL then to SSL.e
# A3: line from SSL.w left even with A0.c then up even with A0.c then right to A0.e


class plusNode(Node):  # one or more
    def pikchr(self, offset=0):
        self.inp = self.parent.outp
        pik = ''
        r = rand()

        if self.sibling != 1:
            pik += 'line from ' + self.inp + '.e right linerad/2 then down $h*' + \
                str(offset) + ' then right linerad/2\n'
            pik += 'A' + str(r) + ': ' + 'arrow linerad\n'
        else:
            pik += 'A' + str(r) + ': ' + \
                'arrow linerad from ' + self.inp + '.e\n'
        pik += 'L' + str(r+1) + ': ' + 'line linerad*2\n'
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        pik += 'L' + str(r) + ': ' + 'line linerad*2\n'
        pik += 'A' + str(r+1) + ': ' + 'arrow from B' + str(r) + \
            '.e right linerad then down $h then left last box.width/2 + linerad\n'
        pik += 'A' + str(r+2) + ': ' + 'arrow from A' + str(r+1) + \
            '.end left last box.width/2 + linerad then up $h then right to B' + \
            str(r) + '.w\n'
        if self.ifend:
            pik += 'arrow right linerad from L' + \
                str(r) + '.end\ncircle radius 10%\n'
        else:
            self.outp = 'L' + str(r)
        return pik


# C0:  circle radius 10%
# A0: arrow linerad from C0.e
# L0: line linerad*2
# B0: box "child" fit
# A1: arrow linerad*2
# L1: line linerad*2
# A2: arrow from B0.e right linerad then down 1.25*linerad then left last box.width/2 + linerad
# A3: arrow from A2.end left last box.width/2 + linerad then up linerad*1.25 then right to B0.w


class questionMarkNode(Node):  # DONE zero or one
    def pikchr(self, offset=0):
        self.inp = self.parent.outp
        pik = ''
        r = rand()

        if self.sibling != 1:
            pik += 'line from ' + self.inp + '.e right linerad/2 then down $h*' + \
                str(offset) + ' then right linerad/2\n'
            pik += 'A' + str(r+3) + ': ' + 'arrow linerad\n'
        else:
            pik += 'A' + str(r+3) + ': ' + \
                'arrow linerad from ' + self.inp + '.e\n'
        pik += 'A' + str(r+1) + ': ' + 'arrow linerad from A' + \
            str(r+3) + '.end right linerad*0.5 then down $h then right linerad*0.5\n'
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        pik += 'A' + \
            str(r+2) + ': ' + \
            'arrow right linerad then up $h then right linerad\n'
        pik += 'A' + str(r) + ':' + ' arrow from A' + \
            str(r+3) + '.e right to A' + str(r+2) + '.end\n'
        pik += 'L' + str(r) + ': ' + 'line linerad\n'
        if self.ifend:
            pik += 'arrow right linerad\ncircle radius 10%\n'
        else:
            self.outp = 'L' + str(r)
        return pik

# C1:  circle radius 10%
# A272: arrow linerad from S911
# A270: arrow linerad from A272.end right linerad*0.5 then down 1.25*linerad then right linerad*.5
# B269: box "children" fit
# A271: arrow right linerad then up 1.25*linerad then right linerad
# A269: arrow from A272.e right to A271.end
# L269: line linerad


class eitherOrNode(Node):
    def pikchr(self):
        self.inp = self.parent.outp
        pik = ''
        r = rand()
        pik += 'A' + str(r) + ': ' + 'arrow linerad from ' + self.inp + '\n'
        pik += 'B' + str(r) + ': ' + 'box \"' + self.name + '\" fit\n'
        pik += 'L' + str(r) + ': ' + 'line linerad\n'
        self.outp = 'L' + str(r)
        return pik


def tree_generator(parseTree, start):
    if len(utility.get_levels(parseTree, 1)) == 0:
        # print(parseTree)
        # start.parent.branchWidth += start.branch.width
        return
    rankInSibling = 0
    for child in utility.get_levels(parseTree, 1):
        rankInSibling += 1
        if len(utility.get_levels(child, 1)) != 0:

            if rankInSibling == 1:
                newNode = Node(name=child.split(
                    ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling)
            else:
                newNode = Node(name=child.split(
                    ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling, olderSibling=brother)
                # start.branchWidth += 1

            start.children.append(newNode)
            tree_generator(child, start=newNode)

            brother = newNode
        else:

            if child.count('?') == 1:
                newEndNode = questionMarkNode(name=child.split(
                    ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling, ifend=True)
                start.children.append(newEndNode)
                # start.branchWidth += 1
            elif child.count('*') == 1:
                newEndNode = starNode(name=child.split(
                    ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling, ifend=True)
                start.children.append(newEndNode)
                # start.branchWidth += 1
            elif child.count('+') == 1:
                newEndNode = plusNode(name=child.split(
                    ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling, ifend=True)
                start.children.append(newEndNode)
                # start.branchWidth += 1
            else:
                newNode = Node(name=child.split(
                    ' ')[0], children=[], parent=start, level=start.level+1, sibling=rankInSibling)
                start.children.append(newNode)
                newEndNode = Node(name=child.split(
                    ' ')[1], children=[], parent=newNode, level=newNode.level+1, sibling=rankInSibling, ifend=True)
                newNode.children.append(newEndNode)


if __name__ == '__main__':

    # pnode = Node(name='parent', outp='anynode')
    # cnode = Node(name='child', parent=pnode)
    # pnode.children.append(cnode)
    # print('questionMarkNode')
    # print(cnode.pikchr(offset=2))
    # print(cnode, 'is kNode:', isinstance(cnode, Node))
    print('-----------------------------')

    pnode = Node(name='parent', outp='anynode')
    cnode = questionMarkNode(name='child', parent=pnode, sibling=2)
    pnode.children.append(cnode)
    print('questionMarkNode')
    print(cnode.pikchr(offset=2))
    print(cnode, 'is questionMarkNode:', isinstance(cnode, questionMarkNode))
    print('-----------------------------')

    pnode = Node(name='parent', outp='anynode')
    cnode = starNode(name='child', parent=pnode, sibling=2)
    pnode.children.append(cnode)
    print('starNode')
    print(cnode.pikchr(offset=2))
    print(cnode, 'is starNode:', isinstance(cnode, starNode))
    print('-----------------------------')

    pnode = Node(name='parent', outp='anynode')
    cnode = plusNode(name='child', parent=pnode, sibling=2)
    pnode.children.append(cnode)
    print('plusNode')
    print(cnode.pikchr(offset=2))
    print(cnode, 'is plusNode:', isinstance(cnode, plusNode))
    print('-----------------------------')
