

import argparse
from antlr4 import *
from ANTLRv4Lexer import ANTLRv4Lexer
# from ANTLRv4ParserVisitor import ANTLRv4ParserVisitor
from ANTLRv4Parser import ANTLRv4Parser
from pikchrParserVisitor import pikchrParserVisitor
import sys
#!coding=utf-8
import os
import glob
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)


def main(grammer, txtLoc='', txtext='pikchr', SVGLoc='', htmlLoc=''):
    # take the input of the file
    # Input = FileStream(argv[1])
    Input = FileStream(grammer)
    lexer = ANTLRv4Lexer(Input)
    stream = CommonTokenStream(lexer)
    parser = ANTLRv4Parser(stream)
    tree = parser.grammarSpec()
    visitor = pikchrParserVisitor()
    transVisitor = visitor.visit(tree)

    if txtLoc != '':
        if not os.path.isdir(txtLoc):
            os.makedirs(txtLoc)
        try:
            for i, c in visitor.pikDict.items():
                filename = os.path.join(txtLoc, (i + '.' + txtext))
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
                filename = htmlLoc + '/test.html'
                cmd = './pikchr/pikchr  ' + txtLoc + '/*.txt > ' + filename
                print(cmd)
                os.system(cmd)


if __name__ == '__main__':

    # parser = argparse.ArgumentParser("g4 To pikchr")
    # parser.add_argument(
    #     '-g', "--grammar", help="path of the g4 grammer file", type=str)
    # parser.add_argument("-op", "--OutputPikchr",
    #                     help="pikchr file folder path", type=str, default='')
    # parser.add_argument("-os", "--OutputSVG",
    #                     help="svg file folder path", type=str, default='')
    # args = parser.parse_args()

    # main(grammer=args.grammar,
    #      txtLoc=args.OutputPikchr, SVGLoc=args.OutputSVG)
    main(grammer='./test.g4', txtLoc='./test', txtext='txt')
    # main(grammer='./ApplEdible.g4', txtLoc='./test/testpik')
    # main(grammer='./py/ApplEdible.g4', txtLoc='./testLex/outpik')
