from lexer.lexer import Lexer


source_code = """
int x;
int y;

x = 10;
y = x + 5;

print("hello");
"""


lexer = Lexer(source_code)

tokens = lexer.tokenize()


print("\nLINE  TOKEN           TYPE")
print("-" * 40)

for token in tokens:
    print(token)