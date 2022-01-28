# Generated from ./py/ANTLRv4Parser.g4 by ANTLR 4.9.2
from antlr4 import *
from random import randrange

# To do
# ebnfsuffix
# ebnf add offset
# Close loose end: use id to reflect the order in the chain


def rand():
    return randrange(10000)

# line from L5760 right until even with L566.e-(0.5*linerad,0) then up until even with L566


def idGen(typeN, level, rand):
    return typeN + '_' + str(level) + '_' + str(rand)

# def maxIdx(dictIn):
#     for idx, c in dictIn:
#         if int


def closeLooseEnd(dictOfLooseEnd, pik):

    for idx, end in dictOfLooseEnd.items():
        # print(idx, end)
        if idx != '0':
            if int(level) < int(end.split('_')[1]):
                level = end.split('_')[1]
                longIdx = idx
                selEnd = end
        else:
            longIdx = '0'
            level = end.split('_')[1]
            selEnd = end
    r = rand()
    # anchor = 'L' + str(r)
    anchor = idGen('L', int(level)+1, r)
    pik += anchor + ': line from ' + \
        dictOfLooseEnd[longIdx] + ' right linerad*3\n'
    for idx, end in dictOfLooseEnd.items():
        if idx != longIdx:
            pik += 'line from ' + end + ' right until even with ' + \
                anchor + \
                '.e - (0.5*linerad, 0) then up until even with ' + \
                anchor + '\nright\n'
    # print(dictOfLooseEnd, 'close loose', longIdx, level, selEnd)
    return pik, anchor


if __name__ is not None and "." in __name__:
    from .ANTLRv4Parser import ANTLRv4Parser
else:
    from ANTLRv4Parser import ANTLRv4Parser

# This class defines a complete generic visitor for a parse tree produced by ANTLRv4Parser.
# This class will overwrite the default vistor

#############################################################
############### All Alt List for branches ###################
#############################################################


class ANTLRv4ParserVisitor(ParseTreeVisitor):
    def __init__(self):
        self.pikDict = {}
        self.nodeid = []
        self.pik = ''

    def visitChildren(self, node):
        result = self.defaultResult()
        n = node.getChildCount()
        for i in range(n):
            self.sibling = i
            if not self.shouldVisitNextChild(node, result):
                return result
            c = node.getChild(i)
            childResult = c.accept(self)
            result = self.aggregateResult(result, childResult)

        return result

    # Visit a parse tree produced by ANTLRv4Parser#grammarSpec.
    def visitGrammarSpec(self, ctx: ANTLRv4Parser.GrammarSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#grammarDecl.
    def visitGrammarDecl(self, ctx: ANTLRv4Parser.GrammarDeclContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#grammarType.
    def visitGrammarType(self, ctx: ANTLRv4Parser.GrammarTypeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#prequelConstruct.
    def visitPrequelConstruct(self, ctx: ANTLRv4Parser.PrequelConstructContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#optionsSpec.
    def visitOptionsSpec(self, ctx: ANTLRv4Parser.OptionsSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#option.
    def visitOption(self, ctx: ANTLRv4Parser.OptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#optionValue.
    def visitOptionValue(self, ctx: ANTLRv4Parser.OptionValueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#delegateGrammars.
    def visitDelegateGrammars(self, ctx: ANTLRv4Parser.DelegateGrammarsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#delegateGrammar.
    def visitDelegateGrammar(self, ctx: ANTLRv4Parser.DelegateGrammarContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#tokensSpec.
    def visitTokensSpec(self, ctx: ANTLRv4Parser.TokensSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#channelsSpec.
    def visitChannelsSpec(self, ctx: ANTLRv4Parser.ChannelsSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#idList.
    def visitIdList(self, ctx: ANTLRv4Parser.IdListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#action_.
    def visitAction_(self, ctx: ANTLRv4Parser.Action_Context):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#actionScopeName.
    def visitActionScopeName(self, ctx: ANTLRv4Parser.ActionScopeNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#actionBlock.
    def visitActionBlock(self, ctx: ANTLRv4Parser.ActionBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#argActionBlock.
    def visitArgActionBlock(self, ctx: ANTLRv4Parser.ArgActionBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#modeSpec.
    def visitModeSpec(self, ctx: ANTLRv4Parser.ModeSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#rules.
    def visitRules(self, ctx: ANTLRv4Parser.RulesContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleSpec.
    def visitRuleSpec(self, ctx: ANTLRv4Parser.RuleSpecContext):
        return self.visitChildren(ctx)

    #############################################################
    #################### Name of each rule ######################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#parserRuleSpec.
    def visitParserRuleSpec(self, ctx: ANTLRv4Parser.ParserRuleSpecContext):
        print('new parserRule',  ctx.getChild(0).getText())
        self.currEndPoint = ''
        self.branchList = []  # stack saving current branch
        # stack saving all endpoint of each branch of each alt
        self.altList = [{'0': '0'}]
        self.level = [1]  # saving for generating id

        r = rand()
        # nid = 'L_' + str(self.level[-1]) + '_' + str(r)
        nid = idGen('L', self.level[-1], r)
        self.nodeid.append(nid)
        prs = ctx.getChild(0).getText()

        self.pik = '$h = 0.5\nlinerad = 20px\nlinewid *= 0.5\nhline = 30px\n'
        self.pik += 'text ' + '\"' + prs + '\"' + '\n'
        self.pik += 'circle radius 10%\n'
        self.pik += nid + ': line right linerad\n'
        self.visitChildren(ctx)

        # print('the end or parseRuleSpec', self.altList)
        self.pik += list(self.altList[-1].values())[0] + \
            ': line right linerad*2\ncircle radius 10%\n '
        self.pikDict[prs] = self.pik
        self.nodeid.pop()
    # Visit a parse tree produced by ANTLRv4Parser#exceptionGroup.

    def visitExceptionGroup(self, ctx: ANTLRv4Parser.ExceptionGroupContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#exceptionHandler.
    def visitExceptionHandler(self, ctx: ANTLRv4Parser.ExceptionHandlerContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#finallyClause.
    def visitFinallyClause(self, ctx: ANTLRv4Parser.FinallyClauseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#rulePrequel.
    def visitRulePrequel(self, ctx: ANTLRv4Parser.RulePrequelContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleReturns.
    def visitRuleReturns(self, ctx: ANTLRv4Parser.RuleReturnsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#throwsSpec.
    def visitThrowsSpec(self, ctx: ANTLRv4Parser.ThrowsSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#localsSpec.
    def visitLocalsSpec(self, ctx: ANTLRv4Parser.LocalsSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleAction.
    def visitRuleAction(self, ctx: ANTLRv4Parser.RuleActionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleModifiers.
    def visitRuleModifiers(self, ctx: ANTLRv4Parser.RuleModifiersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleModifier.
    def visitRuleModifier(self, ctx: ANTLRv4Parser.RuleModifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleBlock.
    def visitRuleBlock(self, ctx: ANTLRv4Parser.RuleBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleAltList.
    def visitRuleAltList(self, ctx: ANTLRv4Parser.RuleAltListContext):
        self.level.append(self.level[-1])
        r = rand()
        # initialize a dict for levels of endpoints
        self.altList.append({'0': '0'})
        nid = idGen('C', self.level[-1], r)
        self.nodeid.append(nid)
        self.branchList.append(0)
        parentNode = self.nodeid[-1]
        # print('RULEALTLIST: at in of ruleAltList', self.altList)
        self.pik += parentNode + ': circle radius 0\n'
        self.visitChildren(ctx)
        # print('RULEALTLIST: before out of ruleAltList', self.altList)
        self.nodeid.pop()
        self.branchList.pop()
        looseEnd = self.altList.pop()
        self.level.pop()
        self.pik, newEnd = closeLooseEnd(looseEnd, self.pik)
        self.currEndPoint = newEnd
        self.altList[-1][list(self.altList[-1].keys())[-1]] = newEnd
        # print('RULEALTLIST: at end of ruleAltList', self.altList)
    # Visit a parse tree produced by ANTLRv4Parser#labeledAlt.

    def visitLabeledAlt(self, ctx: ANTLRv4Parser.LabeledAltContext):
        # print('labeledAlt', ctx.getText(), self.branchList)
        # self.branchList.append(0)
        # self.altList[-1][0] = '0'
        self.visitChildren(ctx)
        # self.branchList
        # looseEnd = self.altList.pop()
        # self.level.pop()
        # self.pik, newEnd = closeLooseEnd(looseEnd, self.pik)
        # self.altList[-1][list(self.altList[-1].keys())[-1]] = newEnd

    # Visit a parse tree produced by ANTLRv4Parser#lexerRuleSpec.

    def visitLexerRuleSpec(self, ctx: ANTLRv4Parser.LexerRuleSpecContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerRuleBlock.
    def visitLexerRuleBlock(self, ctx: ANTLRv4Parser.LexerRuleBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerAltList.
    def visitLexerAltList(self, ctx: ANTLRv4Parser.LexerAltListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerAlt.
    def visitLexerAlt(self, ctx: ANTLRv4Parser.LexerAltContext):
        # print('LexerAlt Found', ctx.getChild(0))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerElements.
    def visitLexerElements(self, ctx: ANTLRv4Parser.LexerElementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerElement.
    def visitLexerElement(self, ctx: ANTLRv4Parser.LexerElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#labeledLexerElement.
    def visitLabeledLexerElement(self, ctx: ANTLRv4Parser.LabeledLexerElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerBlock.
    def visitLexerBlock(self, ctx: ANTLRv4Parser.LexerBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerCommands.
    def visitLexerCommands(self, ctx: ANTLRv4Parser.LexerCommandsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerCommand.
    def visitLexerCommand(self, ctx: ANTLRv4Parser.LexerCommandContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerCommandName.
    def visitLexerCommandName(self, ctx: ANTLRv4Parser.LexerCommandNameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerCommandExpr.
    def visitLexerCommandExpr(self, ctx: ANTLRv4Parser.LexerCommandExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#altList.
    def visitAltList(self, ctx: ANTLRv4Parser.AltListContext):
        self.level.append(self.level[-1])
        # print('altlist', ctx.getText(), self.level[-1])
        r = rand()
        # initialize a dict for branches endpoint
        self.altList.append({'0': '0'})
        # nid = 'C' + str(r)
        nid = idGen('C', self.level[-1], r)
        self.nodeid.append(nid)

        self.branchList.append(0)
        # print('at in of ALTLIST:', self.altList)
        self.pik += nid + ': circle radius 0\n'
        self.visitChildren(ctx)
        # self.pik += ''
        # print('before out of ALTLIST:', self.altList)
        self.nodeid.pop()
        currbranch = self.branchList.pop()
        self.branchList[-1] += currbranch - 1
        looseEnd = self.altList.pop()
        self.level.pop()
        self.pik, newEnd = closeLooseEnd(looseEnd, self.pik)
        self.altList[-1][str(int(list(self.altList[-1].keys())[-1])+1)] = newEnd
        self.currEndPoint = newEnd
        # self.pik, newEnd = closeLooseEnd(looseEnd, self.pik)
        # self.altList[-1][list(self.altList[-1].keys())[-1]] = newEnd

        # print('at out of ALTLIST:', self.altList)
    # Visit a parse tree produced by ANTLRv4Parser#alternative.

    def visitAlternative(self, ctx: ANTLRv4Parser.AlternativeContext):
        self.level.append(self.level[-1])
        # print('alt', ctx.getText(), self.level[-1])
        # self.altList.append({})
        r = rand()
        # print(ctx.getText(), 'level1:', self.level1)
        currbranch = self.branchList.pop()
        self.branchList.append(currbranch+1)
        offset = currbranch

        parentNode = self.nodeid[-1]

        nid = idGen('A', self.level[-1], r)
        if offset > 0:
            self.pik += nid + ': ' + \
                'arrow from ' + parentNode + ' down hline*' + \
                str(offset) + ' then right linerad\n'
        else:
            self.pik += nid + ': arrow from ' + \
                parentNode + ' right linerad\n'
        self.visitChildren(ctx)
        # print('current branch:', currbranch)
        self.altList[-1][str(currbranch)] = self.currEndPoint
        self.level.pop()

    #############################################################
    #################### Building Block ######################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#element.

    def visitElement(self, ctx: ANTLRv4Parser.ElementContext):
        # print('element', ctx.getChild(0))
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#labeledElement.
    def visitLabeledElement(self, ctx: ANTLRv4Parser.LabeledElementContext):
        return self.visitChildren(ctx)

    #############################################################
    ######################## ？/ */ + ###########################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#ebnf.
    def visitEbnf(self, ctx: ANTLRv4Parser.EbnfContext):
        # print('this is a special terminal node', ctx)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#blockSuffix.
    def visitBlockSuffix(self, ctx: ANTLRv4Parser.BlockSuffixContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ebnfSuffix.
    def visitEbnfSuffix(self, ctx: ANTLRv4Parser.EbnfSuffixContext):
        # print('special sign found', ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerAtom.
    def visitLexerAtom(self, ctx: ANTLRv4Parser.LexerAtomContext):
        # print('LexerAtom', ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#atom.

    def visitAtom(self, ctx: ANTLRv4Parser.AtomContext):

        self.level[-1] += 1

        print('atom', ctx.getText(), self.level[-1], self.altList)
        r = rand()
        # nid = idGen('C', self.level[-1], r)

        # self.pik += 'A' + str(r) + ': ' + 'arrow linerad \n'
        # self.pik += 'B' + str(r) + ': ' + 'box \"' + ctx.getText() + '\" fit\n'
        # self.pik += 'L' + str(r) + ': ' + 'line linerad\n'
        # self.currEndPoint = 'L' + str(r)
        self.pik += idGen('A', self.level[-1], r) + ': ' + 'arrow linerad \n'
        self.pik += idGen('B', self.level[-1], r) + \
            ': ' + 'box \"' + ctx.getText() + '\" fit\n'
        self.pik += idGen('L', self.level[-1], r) + ': ' + 'line linerad\n'
        self.currEndPoint = idGen('L', self.level[-1], r)
        self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#notSet.
    def visitNotSet(self, ctx: ANTLRv4Parser.NotSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#blockSet.
    def visitBlockSet(self, ctx: ANTLRv4Parser.BlockSetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#setElement.
    def visitSetElement(self, ctx: ANTLRv4Parser.SetElementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#block.
    def visitBlock(self, ctx: ANTLRv4Parser.BlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#ruleref.
    def visitRuleref(self, ctx: ANTLRv4Parser.RulerefContext):
        # print('ruleref found', ctx.getText())
        # r = rand()
        # self.pik += 'A' + str(r) + ': ' + 'arrow linerad \n'
        # self.pik += 'B' + str(r) + ': ' + 'box \"' + ctx.getText() + '\" fit\n'
        # self.pik += 'L' + str(r) + ': ' + 'line linerad\n'
        self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#characterRange.
    def visitCharacterRange(self, ctx: ANTLRv4Parser.CharacterRangeContext):
        # print('character range')
        return self.visitChildren(ctx)

    #############################################################
    ################# Father of Each End Point ##################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#terminal.
    def visitTerminal(self, ctx: ANTLRv4Parser.TerminalContext):
        # t = ctx.getText()
        # print('terminal', t)
        # r = rand()
        # if t not in [':', '|', ';']:
        #     self.pik += 'A' + str(r) + ': ' + 'arrow linerad \n'
        #     self.pik += 'B' + str(r) + ': ' + 'box \"' + \
        #         t + '\" fit\n'
        #     self.pik += 'L' + str(r) + ': ' + 'line linerad\n'
        self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#elementOptions.
    def visitElementOptions(self, ctx: ANTLRv4Parser.ElementOptionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#elementOption.
    def visitElementOption(self, ctx: ANTLRv4Parser.ElementOptionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#identifier.
    def visitIdentifier(self, ctx: ANTLRv4Parser.IdentifierContext):
        # print('Identifier', ctx.getText())
        return self.visitChildren(ctx)


del ANTLRv4Parser
