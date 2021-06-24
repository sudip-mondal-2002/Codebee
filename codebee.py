#######################################
# IMPORTS
#######################################

from Lexer import *
from Symbol import *
from Parser import *
from Context import *
from Interpretor import *


#######################################
# RUN
#######################################


global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number(0))


def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error:
        return None, error

    # Generate Abstract Syntax Tree
    parser = Parser(tokens)
    ast = parser.parse()

    if ast.error:
        return None, ast.error

    context = Context("Program")
    context.symbol_table = global_symbol_table
    interpretor = Interpretor()
    result = interpretor.visit(ast.node, context)
    return result.value, result.err
