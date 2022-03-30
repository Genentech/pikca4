from Node import *

if __name__ == '__main__':
    t = open('./ApplEdible.txt', mode='r', encoding='utf8')
    treeRaw = t.read()
    t.close()
    treeSplit = treeRaw.split('parserRuleSpec')
    parseRuleList = {}
    for parseRule in treeSplit:
        parseRuleName = parseRule.split(' ')[1]
        parseRuleList[parseRuleName] = utility.cleanParseRule(parseRule)

    parserule = parseRuleList['partial_term']

    startNode = startNode(name='condition_list',
                          parent=None, level=1, sibling=1)

    # utility.testIfValidAndReturnLevel('venn_op', venn_op)
    try:
        tree_generator(parserule, start=startNode)
        testpic = Pic(name='test', startNode=startNode)

    except:
        print('Tree Generation Failed', traceback.print_exc())

    # print(testpic.paint())
    testpic.save('./textout.txt')
    # print("picture's depth is", testpic.depth)
    # print("picture's width is", testpic.width)

    # for i in range(16):
    # print(i, utility.get_levels(parserule, i))
