from lexer.token_types import TokenType
from lexer.token import Token


KEYWORDS = {
    "int",
    "float",
    "if",
    "else",
    "while",
    "print"
}

OPERATORS = {
    "+", "-", "*", "/",
    "=",
    "==", "!=", "<", ">",
    "<=", ">=",
    "&&", "||"
}

DELIMITERS = {
    ";", "(", ")", "{", "}", ","
}


class Lexer:

    def __init__(self, source_code):

        self.source_code = source_code

        self.position = 0
        self.line = 1

        self.tokens = []

    def peek(self):

        if self.position >= len(self.source_code):
            return None

        return self.source_code[self.position]

    def advance(self):

        char = self.peek()

        self.position += 1

        return char

    def tokenize(self):

        while self.position < len(self.source_code):

            current = self.peek()

            # boşluk
            if current in [' ', '\t', '\r']:
                self.advance()
                continue

            # yeni satır
            if current == '\n':
                self.line += 1
                self.advance()
                continue

            # identifier / keyword
            if current.isalpha() or current == "_":
                self.tokenize_identifier()
                continue

            # sayı
            if current.isdigit():
                self.tokenize_number()
                continue

            # string
            if current == '"':
                self.tokenize_string()
                continue

            # operator
            if self.is_operator_start(current):
                self.tokenize_operator()
                continue

            # delimiter
            if current in DELIMITERS:
                self.tokens.append(
                    Token(TokenType.DELIMITER, current, self.line)
                )

                self.advance()
                continue

            # lexical error
            self.tokens.append(
                Token(TokenType.ERROR, current, self.line)
            )

            self.advance()

        self.tokens.append(
            Token(TokenType.EOF, "EOF", self.line)
        )

        return self.tokens

    def tokenize_identifier(self):

        value = ""

        while self.peek() and (
            self.peek().isalnum() or self.peek() == "_"
        ):
            value += self.advance()

        if value in KEYWORDS:
            token_type = TokenType.KEYWORD
        else:
            token_type = TokenType.IDENTIFIER

        self.tokens.append(
            Token(token_type, value, self.line)
        )

    def tokenize_number(self):

        value = ""
        dot_count = 0

        while self.peek() and (
            self.peek().isdigit() or self.peek() == "."
        ):

            if self.peek() == ".":
                dot_count += 1

            value += self.advance()

        if dot_count > 1:

            self.tokens.append(
                Token(TokenType.ERROR, value, self.line)
            )

            return

        if "." in value:
            token_type = TokenType.FLOAT_LITERAL
        else:
            token_type = TokenType.INTEGER_LITERAL

        self.tokens.append(
            Token(token_type, value, self.line)
        )

    def tokenize_string(self):

        self.advance()

        value = ""

        while self.peek() and self.peek() != '"':

            if self.peek() == '\n':
                self.line += 1

            value += self.advance()

        if self.peek() != '"':

            self.tokens.append(
                Token(TokenType.ERROR, value, self.line)
            )

            return

        self.advance()

        self.tokens.append(
            Token(TokenType.STRING_LITERAL, value, self.line)
        )

    def is_operator_start(self, char):

        for op in OPERATORS:
            if op.startswith(char):
                return True

        return False

    def tokenize_operator(self):

        current = self.advance()

        next_char = self.peek()

        combined = current

        if next_char:
            temp = current + next_char

            if temp in OPERATORS:
                combined = temp
                self.advance()

        self.tokens.append(
            Token(TokenType.OPERATOR, combined, self.line)
        )