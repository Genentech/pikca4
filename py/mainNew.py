

from antlr4 import *
from ANTLRv4Lexer import ANTLRv4Lexer
from ANTLRv4ParserVisitor import ANTLRv4ParserVisitor
from ANTLRv4Parser import ANTLRv4Parser
import sys
#!coding=utf-8
import os
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

# branchList

# level

# altList


def toHtml(name='test', loc=''):
    pass


def main(grammer, txtLoc='', SVGLoc='', htmlLoc=''):
    # take the input of the file
    # Input = FileStream(argv[1])
    Input = FileStream(grammer)
    lexer = ANTLRv4Lexer(Input)
    stream = CommonTokenStream(lexer)
    parser = ANTLRv4Parser(stream)
    tree = parser.grammarSpec()
    visitor = ANTLRv4ParserVisitor()
    transVisitor = visitor.visit(tree)

    if txtLoc != '':
        if not os.path.isdir(txtLoc):
            os.makedirs(txtLoc)
        try:
            for i, c in visitor.pikDict.items():
                filename = os.path.join(txtLoc, (i + '.txt'))
                t = open(filename, mode='w', encoding='utf8')
                t.write(c)
            t.close()
        except:
            print('save failed, print pikchr to terminal')
            print(traceback.print_exc())

        if SVGLoc != '':
            if not os.path.isdir(SVGLoc):
                os.makedirs(SVGLoc)
            cmd = "bash ./pikchr/pikchrToSVG.sh -i " + txtLoc + " -o " + SVGLoc
            os.system(cmd)
            if htmlLoc != '':
                if not os.path.isdir(htmlLoc):
                    os.makedirs(htmlLoc)
                # toHtml(name = report, loc = htmlLoc)


if __name__ == '__main__':

    main(grammer='./SQLiteParser.g4',
         txtLoc='./SQLite/OutPikchr', SVGLoc='./SQLite/OutSVG')
    # print(os.path.join('test1', 'test2', 'test.txt'))
