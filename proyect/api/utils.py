from antlr4 import *
import lenguage.GrammarLexer as GrammarLexer
import lenguage.GrammarParser as GrammarParser
import lenguage.MyVisitor as MyVisitor
import io
import sys

def run_code(code:str):
    input_stream=InputStream(code)
    lexer= GrammarLexer(input_stream)
    stream=CommonTokenStream(lexer)
    parser=GrammarParser(stream)
    tree=parser.program()

    # Captura la salida
    old_stdout=sys.stdout()
    buf = io.StringIO()
    sys.stdout = buf

    # Creamos un objeto de nuestro visitor
    visitor = MyVisitor()
    # Visitamos el arbol con nuestro visitor
    visitor.visit(tree)
    # Capturamos la salida
    output=buf.getvalue()

    return output