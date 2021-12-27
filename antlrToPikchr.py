import sys
import os
import utility

# TODO LIST
# 1. How to cope with multiple input
# 2. How to cope with multiple levels of brackets


# (xyz)*
# Example:
# text "parse"
# linerad = 10px
# linewid *= 0.5
# $h = 0.21
# C1:  circle radius 10%
# A0: arrow right linerad*2
# SSL: box "sql_stmt_list" fit with .w at(linewid right of C1.e, $h below C1)
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
# SSL: box "sql_stmt_list" fit with .w at(linewid right of C1.e, $h below C1)
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


class convertor:
    def __init__(self, inFileName: str):
        infile = open(inFileName, mode='r', encoding='utf8')
        treeRaw = infile.read()
        infile.close()

        self.pikchr = {}

    def start(ruleName: str):
        outfile.write()

        return nout

    def writePikchr(self, outPikchrDir):
        for i in self.pikchr:
            f = open(os.path.join(outPikchrDir, i))
            f.write(self.pikchr[i])
            f.close()


class pik:
    def __init__(self, inNode, outNode):
        pass


if __name__ == '__main__':

    t = open('./ApplEdible.txt', mode='r', encoding='utf8')
    treeRaw = t.read()
    t.close()

    treeSplit = treeRaw.split('parserRuleSpec')

    parseRuleList = {}
    for parseRule in treeSplit:

        parseRuleName = parseRule.split(' ')[1]
        parseRuleList[parseRuleName] = utility.cleanParseRule(parseRule)

    # print(len(parseRuleList))  # 45
    # print(parseRuleList.keys())

    test = parseRuleList['venn_op']
    max_level = utility.testIfValidAndReturnLevel('venn_op', test)
    print(max_level)

    textSplit = test.split(' ')

    print(textSplit)
    outfile = open('./testout.txt', mode='w', encoding='utf8')

    level = 0

    config = 'linerad = 10px\nlinewid *= 0.5\n'
    outfile.write(config)
    outfile.writelines('text \"venn_op\"\n')
    outfile.writelines('START: circle radius 10%\nA0: arrow right linewid\n')

    for txt in textSplit:

        if txt.startswith('('):
            level += txt.count('(')

        else:
            level -= txt.count(')')

    outfile.close()

# A0: arrow right linewid
# B1: box "XYZ" fit
# A1: arrow right linewid
# B2: box "ZYXXYZ" fit
# A2: arrow right linewid
