#*for testing the lexer only*

# from lexer.lexer import Lexer

# source_code = """
# int x;
# int y;

# x = 10;
# y = x + 5;

# print("hello");
# """


# lexer = Lexer(source_code)

# tokens = lexer.tokenize()


# print("\nLINE  TOKEN           TYPE")
# print("-" * 40)

# for token in tokens:
#     print(token)

#----------------------------------------------------------------

#*for testing the parser only*

# from lexer.lexer import Lexer
# from parser.parser import Parser


# source_code = """
# int x;
# int y;

# x = 10;
# y = x + 5 * 2;

# print(y);
# """


# lexer = Lexer(source_code)

# tokens = lexer.tokenize()

# print("\nTOKENS")
# print("-" * 40)

# for token in tokens:
#     print(token)


# print("\nAST")
# print("-" * 40)

# parser = Parser(tokens)

# ast = parser.parse()

# ast.print_tree()
#----------------------------------------------------------------

#*for testing the semantic analyzer only*
# from lexer.lexer import Lexer
# from parser.parser import Parser
# from semantic.semantic_analyzer import SemanticAnalyzer


# source_code = """
# int x;
# float y;

# x = 10;

# y = x + 5.5;

# z = 7;

# int x;

# x = "hello";

# print(y);
# """


# # LEXER
# lexer = Lexer(source_code)

# tokens = lexer.tokenize()

# print("\nTOKENS")
# print("-" * 50)

# for token in tokens:
#     print(token)


# # PARSER
# parser = Parser(tokens)

# ast = parser.parse()

# print("\nAST")
# print("-" * 50)

# ast.print_tree()


# # SEMANTIC ANALYSIS
# semantic = SemanticAnalyzer()

# semantic.analyze(ast)

# print("\nSYMBOL TABLE")
# print("-" * 50)

# for name, var_type in semantic.symbol_table.items():
#     print(f"{name} -> {var_type}")


# print("\nSEMANTIC ERRORS")
# print("-" * 50)

# if semantic.errors:

#     for error in semantic.errors:
#         print(error)

# else:
#     print("No semantic errors")

#-----------------------------------------------------------------

# from lexer.lexer import Lexer
# from parser.parser import Parser
# from semantic.semantic_analyzer import SemanticAnalyzer


# source_code = """
# int x;
# int y;

# x = 10;
# y = 5;

# if (x > y) {

#     print(x);

# }
# else {

#     print(y);

# }

# while (x > 0) {

#     x = x - 1;

# }
# """


# # LEXER
# lexer = Lexer(source_code)

# tokens = lexer.tokenize()

# print("\nTOKENS")
# print("-" * 50)

# for token in tokens:
#     print(token)


# # PARSER
# parser = Parser(tokens)

# ast = parser.parse()

# print("\nAST")
# print("-" * 50)

# ast.print_tree()


# # SEMANTIC
# semantic = SemanticAnalyzer()

# semantic.analyze(ast)

# print("\nSYMBOL TABLE")
# print("-" * 50)

# for name, var_type in semantic.symbol_table.items():
#     print(f"{name} -> {var_type}")

# print("\nSEMANTIC ERRORS")
# print("-" * 50)

# if semantic.errors:
#     for error in semantic.errors:
#         print(error)
# else:
#     print("No semantic errors")

#-----------------------------------------------------------------

#*for testing the whole compiler in the GUI*
import tkinter as tk

from gui.compiler_gui import CompilerGUI


root = tk.Tk()

app = CompilerGUI(root)

root.mainloop()