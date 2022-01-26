# Generated from ./py/ANTLRv4Parser.g4 by ANTLR 4.9.2
from antlr4 import *
from random import randrange

# To do
# ebnfsuffix
# ebnf add offset
# Close loose end


def rand():
    return randrange(10000)

# line from L5760 right until even with L566.e-(0.5*linerad,0) then up until even with L566


def closeLooseEnd(dictOfLooseEnd, pik):
    for idx, end in dictOfLooseEnd.items():
        if idx == '0':
            r = rand()
            anchor = 'L' + str(r)
            pik += anchor + ': line from ' + end + ' right linerad*3\n'
        else:
            pik += 'line from ' + end + 'until .e even with ' + \
                anchor + '.e then up to ' + anchor + '\n'

    return pik


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
        self.altList = []  # stack saving all endpoint of each branch of each alt

        r = rand()
        nid = 'L' + str(r)
        self.nodeid.append(nid)
        prs = ctx.getChild(0).getText()

        self.pik = '$h = 0.5\nlinerad = 20px\nlinewid *= 0.5\n'
        self.pik += 'text ' + '\"' + prs + '\"' + '\n'
        self.pik += 'circle radius 10%\n'
        self.pik += 'L' + str(r) + ': line right linerad\n'
        self.visitChildren(ctx)
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
        r = rand()
        # initialize a dict for branches endpoint
        self.altList.append({})
        nid = 'C' + str(r)
        self.nodeid.append(nid)
        self.branchList.append(0)
        parentNode = self.nodeid[-1]
        self.pik += parentNode + ': circle radius 0\n'
        self.visitChildren(ctx)
        # self.pik += ''
        print('RULEALTLIST:', self.altList)
        self.nodeid.pop()
        self.branchList.pop()
        looseEnd = self.altList.pop()
        # self.pik = closeLooseEnd(looseEnd, self.pik)
    # Visit a parse tree produced by ANTLRv4Parser#labeledAlt.

    def visitLabeledAlt(self, ctx: ANTLRv4Parser.LabeledAltContext):
        # print(self.sibling, 'LabeledAlt found', ctx.getChild(0))
        # r = rand()

        # branch = self.sibling
        # parentNode = self.nodeid[-1]
        # if branch > 0:
        #     self.pik += 'A' + str(r) + ': ' + \
        #         'arrow from ' + parentNode + ' down linerad*' + \
        #         str(branch) + ' then right linerad\n'
        # else:
        #     self.pik += 'A' + str(r) + ': arrow from ' + \
        #         parentNode + ' right linerad\n'
        self.visitChildren(ctx)
        # self.altList[-1][str(branch)] = self.currEndPoint

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
        print('lexer element found', ctx.getText())
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
        r = rand()
        # initialize a dict for branches endpoint
        self.altList.append({})
        nid = 'C' + str(r)
        self.nodeid.append(nid)

        self.branchList.append(0)

        self.pik += nid + ': circle radius 0\n'
        self.visitChildren(ctx)
        # self.pik += ''
        print('RULEALTLIST:', self.altList)
        self.nodeid.pop()
        self.branchList.pop()
        looseEnd = self.altList.pop()
        # self.pik = closeLooseEnd(looseEnd, self.pik)
    # Visit a parse tree produced by ANTLRv4Parser#alternative.

    def visitAlternative(self, ctx: ANTLRv4Parser.AlternativeContext):
        r = rand()

        currbranch = self.branchList.pop()
        self.branchList.append(currbranch+1)
        branch = currbranch*2

        parentNode = self.nodeid[-1]
        if branch > 0:
            self.pik += 'A' + str(r) + ': ' + \
                'arrow from ' + parentNode + ' down linerad*' + \
                str(branch) + ' then right linerad\n'
        else:
            self.pik += 'A' + str(r) + ': arrow from ' + \
                parentNode + ' right linerad\n'
        self.visitChildren(ctx)
        self.altList[-1][str(branch)] = self.currEndPoint

    #############################################################
    #################### Building Block ######################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#element.
    def visitElement(self, ctx: ANTLRv4Parser.ElementContext):
        print('element', ctx.getChild(0))
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
        print('special sign found', ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerAtom.
    def visitLexerAtom(self, ctx: ANTLRv4Parser.LexerAtomContext):
        print('LexerAtom', ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#atom.
    def visitAtom(self, ctx: ANTLRv4Parser.AtomContext):
        print('atom', ctx.getText())
        r = rand()
        self.pik += 'A' + str(r) + ': ' + 'arrow linerad \n'
        self.pik += 'B' + str(r) + ': ' + 'box \"' + ctx.getText() + '\" fit\n'
        self.pik += 'L' + str(r) + ': ' + 'line linerad\n'
        self.currEndPoint = 'L' + str(r)
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
        print('ruleref found', ctx.getText())
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
        print('Identifier', ctx.getText())
        return self.visitChildren(ctx)


del ANTLRv4Parser
