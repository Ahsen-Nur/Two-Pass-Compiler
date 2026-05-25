from lexer.token_types import TokenType
from parser.ast_nodes import ASTNode


class Parser:

    def __init__(self, tokens):

        self.tokens = tokens
        self.position = 0

    def current_token(self):

        if self.position >= len(self.tokens):
            return None

        return self.tokens[self.position]

    def eat(self, expected_type=None, expected_value=None):

        token = self.current_token()

        if token is None:
            raise Exception("Unexpected end of input")

        if expected_type and token.type != expected_type:
            raise Exception(
                f"Expected {expected_type} but got {token.type}"
            )

        if expected_value and token.value != expected_value:
            raise Exception(
                f"Expected {expected_value} but got {token.value}"
            )

        self.position += 1

        return token

    def parse(self):

        root = ASTNode("PROGRAM")

        while self.current_token().type != TokenType.EOF:

            stmt = self.parse_statement()

            root.add_child(stmt)

        return root

    def parse_statement(self):

        token = self.current_token()

        # declaration
        if (
            token.type == TokenType.KEYWORD
            and token.value in ["int", "float"]
        ):
            return self.parse_declaration()

        # assignment
        elif token.type == TokenType.IDENTIFIER:
            return self.parse_assignment()

        # print
        elif (
            token.type == TokenType.KEYWORD
            and token.value == "print"
        ):
            return self.parse_print()

        else:
            raise Exception(
                f"Invalid statement at line {token.line}"
            )

    def parse_declaration(self):

        type_token = self.eat(TokenType.KEYWORD)

        id_token = self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.DELIMITER, ";")

        node = ASTNode("DECLARATION")

        node.add_child(
            ASTNode("TYPE", type_token.value)
        )

        node.add_child(
            ASTNode("IDENTIFIER", id_token.value)
        )

        return node

    def parse_assignment(self):

        id_token = self.eat(TokenType.IDENTIFIER)

        self.eat(TokenType.OPERATOR, "=")

        expr = self.parse_expression()

        self.eat(TokenType.DELIMITER, ";")

        node = ASTNode("ASSIGNMENT")

        node.add_child(
            ASTNode("IDENTIFIER", id_token.value)
        )

        node.add_child(expr)

        return node

    def parse_print(self):

        self.eat(TokenType.KEYWORD, "print")

        self.eat(TokenType.DELIMITER, "(")

        expr = self.parse_expression()

        self.eat(TokenType.DELIMITER, ")")

        self.eat(TokenType.DELIMITER, ";")

        node = ASTNode("PRINT")

        node.add_child(expr)

        return node

    def parse_expression(self):

        node = self.parse_term()

        while (
            self.current_token().value in ["+", "-"]
        ):

            op = self.eat(TokenType.OPERATOR)

            right = self.parse_term()

            op_node = ASTNode("OPERATOR", op.value)

            op_node.add_child(node)
            op_node.add_child(right)

            node = op_node

        return node

    def parse_term(self):

        node = self.parse_factor()

        while (
            self.current_token().value in ["*", "/"]
        ):

            op = self.eat(TokenType.OPERATOR)

            right = self.parse_factor()

            op_node = ASTNode("OPERATOR", op.value)

            op_node.add_child(node)
            op_node.add_child(right)

            node = op_node

        return node

    def parse_factor(self):

        token = self.current_token()

        # number
        if token.type in [
            TokenType.INTEGER_LITERAL,
            TokenType.FLOAT_LITERAL
        ]:

            self.eat(token.type)

            return ASTNode("NUMBER", token.value)

        # string
        elif token.type == TokenType.STRING_LITERAL:

            self.eat(TokenType.STRING_LITERAL)

            return ASTNode("STRING", token.value)

        # identifier
        elif token.type == TokenType.IDENTIFIER:

            self.eat(TokenType.IDENTIFIER)

            return ASTNode("IDENTIFIER", token.value)

        # ( expression )
        elif token.value == "(":

            self.eat(TokenType.DELIMITER, "(")

            node = self.parse_expression()

            self.eat(TokenType.DELIMITER, ")")

            return node

        else:

            raise Exception(
                f"Unexpected token {token.value}"
            )