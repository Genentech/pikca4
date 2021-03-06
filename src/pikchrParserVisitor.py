# Generated from ./py/ANTLRv4Parser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ANTLRv4Parser import ANTLRv4Parser
    from .ANTLRv4ParserVisitor import ANTLRv4ParserVisitor
else:
    from ANTLRv4Parser import ANTLRv4Parser
    from ANTLRv4ParserVisitor import ANTLRv4ParserVisitor

# This class defines a complete generic visitor for a parse tree produced by ANTLRv4Parser.
# Generated from ./py/ANTLRv4Parser.g4 by ANTLR 4.9.2

from random import randrange
import math

# To do
# ebnfsuffix
# ebnf add offset: Fixed
# Close loose end: use id to reflect the order in the chain: Fixed
# candidate offset to the next label_offset
# level number refine: fixed
# overlap for neighboring suffix


def rand():
    return randrange(10000)

# line from L5760 right until even with L566.e-(0.5*linerad,0) then up until even with L566


def idGen(typeN, level, rand):
    return typeN + '_' + str(level) + '_' + str(rand)


def closeLooseEnd(dictOfLooseEnd, pik):
    if len(dictOfLooseEnd) > 1:
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
            dictOfLooseEnd[longIdx] + '.e right linerad*4\n'
        for idx, end in dictOfLooseEnd.items():
            if idx != longIdx:
                pik += 'line from ' + end + ' right until even with ' + \
                    anchor + \
                    '.e - (2*linerad, 0) then up until even with ' + \
                    anchor + '\nright\n'
        # print(dictOfLooseEnd, 'close loose', longIdx, level, selEnd)
    elif len(dictOfLooseEnd) <= 1:
        anchor = list(dictOfLooseEnd.values())[-1]
    return pik, anchor


# This class defines a complete generic visitor for a parse tree produced by ANTLRv4Parser.
# This class will overwrite the default vistor

#############################################################
############### Alt List for branches ###################
#############################################################


class pikchrParserVisitor(ANTLRv4ParserVisitor):
    def __init__(self):
        self.pikDict = {}
        self.splitNodeStack = []
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
        try:
            print('\n\nnew parserRule',  ctx.getChild(0).getText())
            self.currEndPoint = ''
            self.branchList = []  # stack saving current branch
            # stack saving all endpoint of each branch of each alt
            self.altList = [{'0': '0'}]
            self.level = [1]  # saving for generating id
            self.elementStart = []
            self.blockSuf = False
            self.suffixOffset = [1]

            r = rand()
            # nid = 'L_' + str(self.level[-1]) + '_' + str(r)
            nid = idGen('L', self.level[-1], r)
            self.splitNodeStack.append(nid)
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
            self.splitNodeStack.pop()
        except:
            print(ctx.getChild(0).getText(), 'failed')
            print(traceback.print_exc())
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
        self.currEndPoint = nid
        self.splitNodeStack.append(nid)
        self.branchList.append(0)
        self.labelAltEnd = {}
        self.labelAltOrd = 0

        parentNode = self.splitNodeStack[-1]
        # print('RULEALTLIST: at in of ruleAltList', self.altList)
        self.pik += parentNode + ': circle radius 0\n'
        self.visitChildren(ctx)
        # print('RULEALTLIST: before out of ruleAltList', self.altList)
        self.splitNodeStack.pop()
        self.branchList.pop()
        looseEnd = self.altList.pop()
        self.level.pop()
        # self.pik, newEnd = closeLooseEnd(looseEnd, self.pik)
        self.pik, newEnd = closeLooseEnd(self.labelAltEnd, self.pik)
        self.currEndPoint = newEnd
        self.altList[-1][list(self.altList[-1].keys())[-1]] = newEnd
        # print('RULEALTLIST: at end of ruleAltList', self.altList)
    # Visit a parse tree produced by ANTLRv4Parser#labeledAlt.

    def visitLabeledAlt(self, ctx: ANTLRv4Parser.LabeledAltContext):
        # print('labeledAlt', ctx.getText(), self.branchList)
        self.candLabeledAltOffset = [0]
        self.prevBranchWidth = 1

        self.visitChildren(ctx)
        # self.branchList.pop()
        print('labeledAlt', self.candLabeledAltOffset)
        self.branchList[-1] += max(self.candLabeledAltOffset)
        self.labelAltEnd[str(self.labelAltOrd)] = self.currEndPoint
        self.labelAltOrd += 1

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
        self.splitNodeStack.append(nid)

        self.branchList.append(0)
        # print('at in of ALTLIST:', self.altList)
        self.pik += nid + ': circle radius 0 at ' + self.currEndPoint + '.e\n'
        self.currEndPoint = nid
        self.visitChildren(ctx)

        self.splitNodeStack.pop()
        currbranch = self.branchList.pop()
        self.prevBranchWidth = max(currbranch, self.prevBranchWidth)
        self.suffixOffset[-1] = max(currbranch, self.suffixOffset[-1])

        # print('previous branch width', self.prevBranchWidth)
        self.candLabeledAltOffset.append(currbranch - 1)
        # self.branchList[-1] += currbranch - 1

        looseEnd = self.altList.pop()
        self.level.pop()
        self.pik, newEnd = closeLooseEnd(looseEnd, self.pik)
        self.altList[-1][str(int(list(self.altList[-1].keys())[-1]))] = newEnd
        self.currEndPoint = newEnd
        # self.splitNodeStack.append(newEnd)
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
        currbranch = self.branchList[-1]

        offset = currbranch

        parentNode = self.splitNodeStack[-1]

        nid1 = idGen('A', self.level[-1], r)
        nid2 = idGen('L', self.level[-1], r)
        if offset > 0:
            self.pik += nid1 + ': ' + \
                'line from ' + parentNode + ' down hline*' + \
                str(offset) + ' then right linerad\n'
            self.pik += nid2 + ': line right linerad\n'
        else:
            self.pik += nid1 + ': line from ' + \
                parentNode + ' right linerad\n'
            self.pik += nid2 + ': line right linerad\n'

        self.currEndPoint = nid2
        self.visitChildren(ctx)
        # print('branchlist:', self.branchList, '\nend of current branch:', str(currbranch), 'change from',
        #       self.altList[-1], 'to', self.currEndPoint)
        self.branchList[-1] = currbranch+1
        self.altList[-1][str(currbranch)] = self.currEndPoint
        self.level.pop()

    #############################################################
    #################### Building Block ######################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#element.

    def visitElement(self, ctx: ANTLRv4Parser.ElementContext):
        self.elementStart.append(self.currEndPoint)
        # print('element start:', self.elementStart)
        self.visitChildren(ctx)
        self.elementStart.pop()
        # print('element out', self.elementStart)

    # Visit a parse tree produced by ANTLRv4Parser#labeledElement.
    def visitLabeledElement(self, ctx: ANTLRv4Parser.LabeledElementContext):
        return self.visitChildren(ctx)

    #############################################################
    ######################## ???/ */ + ###########################
    #############################################################
    # Visit a parse tree produced by ANTLRv4Parser#ebnf.
    def visitEbnf(self, ctx: ANTLRv4Parser.EbnfContext):
        self.suffixOffset.append(1)
        self.visitChildren(ctx)
        out = self.suffixOffset.pop()
        self.suffixOffset[-1] = max(out, self.suffixOffset[-1])
    # Visit a parse tree produced by ANTLRv4Parser#blockSuffix.

    def visitBlockSuffix(self, ctx: ANTLRv4Parser.BlockSuffixContext):
        self.blockSuf = True
        self.visitChildren(ctx)
        self.blockSuf = False
    # Visit a parse tree produced by ANTLRv4Parser#ebnfSuffix.

    def visitEbnfSuffix(self, ctx: ANTLRv4Parser.EbnfSuffixContext):
        # print('special sign found', ctx.getText())
        # print('previous endpoint', self.elementStart)
        # print('previousbranch width', self.prevBranchWidth)
        startNode = self.elementStart[-1]

        cat = ctx.getText()

        if self.blockSuf and self.suffixOffset[-1] != 1:
            offset = self.suffixOffset[-1]
        else:
            offset = 1

        if cat == '+' or cat == '?':
            self.suffixOffset[-1] += 1
            self.prevBranchWidth += 1
        elif cat == '*':
            self.suffixOffset[-1] += 2
            self.prevBranchWidth += 2

        self.candLabeledAltOffset.append(self.prevBranchWidth + 1)

        # offset = max(offset, self.candLabeledAltOffset-1)
        if cat == '*':
            self.pik += 'line from ' + startNode + '.c + (0.5*linerad,0) left 0.2*linerad then down hline*' + str(offset) + ' then right until even with ' + \
                startNode + '.c + (' + self.currEndPoint + \
                '.e.x*0.5 - ' + startNode + '.c.x*0.5, 0)\n'
            self.pik += 'arrow <- right until even with ' + self.currEndPoint + \
                '.c then up even with ' + self.currEndPoint + '.c then left 10px\nright\n'
            self.pik += 'arrow from ' + startNode + '.c down hline*' + str(offset+1) + ' then right until even with ' + \
                startNode + '.c + (' + self.currEndPoint + \
                '.e.x*0.5 - ' + startNode + '.c.x*0.5, 0)\n'
            self.pik += 'line right until even with ' + self.currEndPoint + \
                '.c then up even with ' + self.currEndPoint + '.c\nright\n'

        elif cat == '+':
            self.pik += 'line from ' + startNode + '.c + (0.5*linerad,0) left 0.2*linerad then down hline*' + str(offset) + ' then right until even with ' + \
                startNode + '.c + (' + self.currEndPoint + \
                '.e.x*0.5 - ' + startNode + '.c.x*0.5, 0)\n'
            self.pik += 'arrow <- right until even with ' + self.currEndPoint + \
                '.c then up even with ' + self.currEndPoint + '.c then left 10px\nright\n'
            # self.branchList[-1] += 1

        elif cat == '?':
            self.pik += 'arrow from ' + startNode + '.c down hline*' + str(offset) + ' then right until even with ' + \
                startNode + '.c + (' + self.currEndPoint + \
                '.e.x*0.5 - ' + startNode + '.c.x*0.5, 0)\n'
            self.pik += 'line right until even with ' + self.currEndPoint + \
                '.c then up even with ' + self.currEndPoint + '.c\nright\n'
            # self.branchList[-1] += 1
        self.level[-1] += 1
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#lexerAtom.
    def visitLexerAtom(self, ctx: ANTLRv4Parser.LexerAtomContext):
        # print('LexerAtom', ctx.getText())
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ANTLRv4Parser#atom.

    def visitAtom(self, ctx: ANTLRv4Parser.AtomContext):

        # if len(ctx.getText()) > 12:
        #     self.level[-1] += 2
        # else:
        #     self.level[-1] += 1

        self.level[-1] += math.floor(len(ctx.getText())/12) + 1

        print('atom', ctx.getText(),
              self.level[-1], self.altList, self.branchList)
        r = rand()
        print(ctx.getText(), idGen('L', self.level[-1], r))

        # nid = idGen('C', self.level[-1], r)

        # self.pik += 'A' + str(r) + ': ' + 'arrow linerad \n'
        # self.pik += 'B' + str(r) + ': ' + 'box \"' + ctx.getText() + '\" fit\n'
        # self.pik += 'L' + str(r) + ': ' + 'line linerad\n'
        # self.currEndPoint = 'L' + str(r)
        # ***** add from currEndPoint
        self.pik += idGen('A', self.level[-1], r) + ': ' + \
            'arrow linerad from ' + self.currEndPoint + '.e\n'
        self.pik += idGen('B', self.level[-1], r) + \
            ': ' + 'box \"' + ctx.getText() + '\" fit\n'
        self.pik += idGen('L', self.level[-1], r) + ': ' + 'line linerad\n'
        self.currEndPoint = idGen('L', self.level[-1], r)
        self.altList[-1][str(self.branchList[-1])] = self.currEndPoint
        print('atom', ctx.getText(),
              self.level[-1], self.altList, self.branchList)
        # self.altList[-1][str(int(list(self.altList[-1].keys())[-1]))
        #                  ] = self.currEndPoint
        # self.altList[-1][str(int(list(self.altList[-1].keys())[-1]))
        #                  ] = self.currEndPoint
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

        self.visitChildren(ctx)

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
