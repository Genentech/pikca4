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

    parserule = parseRuleList['condition_list']
    utility.visualizeLevel(parserule)
    # prim_expr = parseRuleList['prim_expr']

    startNode = startNode(name='stmt', parent=None, level=1)

    # utility.testIfValidAndReturnLevel('venn_op', venn_op)
    try:
        tree_generator(parserule, start=startNode)
        testpic = Pic(name='test', startNode=startNode)
    except:
        print('Tree Generation Failed', traceback.print_exc())
    # tree_generator(venn_op, start=startNode)

    print(testpic.paint())

    # print(
    # startNode.children[0].children[0].children[0].children[0].children[1].children)
    # utility.visualize_all(parseRuleList)

    # print(venn_op)
    # for i in range(16):
    #     print(i, utility.get_levels(venn_op, i))
    # test = '(test xxxx +)'
    # print(utility.get_levels(test, 0))
    # print(utility.get_levels(test, 1))
