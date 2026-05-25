class SemanticAnalyzer:

    def __init__(self):

        self.symbol_table = {}

        self.errors = []

    def analyze(self, node):

        method_name = f"visit_{node.node_type}"

        method = getattr(
            self,
            method_name,
            self.generic_visit
        )

        method(node)

    def generic_visit(self, node):

        for child in node.children:
            self.analyze(child)

    # PROGRAM
    def visit_PROGRAM(self, node):

        for child in node.children:
            self.analyze(child)

    # DECLARATION
    def visit_DECLARATION(self, node):

        var_type = node.children[0].value
        var_name = node.children[1].value

        # duplicate variable
        if var_name in self.symbol_table:

            self.errors.append(
                f"Semantic Error: Variable '{var_name}' already declared"
            )

            return

        self.symbol_table[var_name] = var_type

    # ASSIGNMENT
    def visit_ASSIGNMENT(self, node):

        var_name = node.children[0].value

        # undeclared variable
        if var_name not in self.symbol_table:

            self.errors.append(
                f"Semantic Error: Variable '{var_name}' not declared"
            )

            return

        expr_type = self.evaluate_expression(
            node.children[1]
        )

        var_type = self.symbol_table[var_name]

        # type mismatch
        if var_type != expr_type:

            # int içine float verilmesi
            if not (
                var_type == "float"
                and expr_type == "int"
            ):

                self.errors.append(
                    f"Semantic Error: Cannot assign {expr_type} to {var_type}"
                )

    # PRINT
    def visit_PRINT(self, node):

        self.evaluate_expression(node.children[0])

    def evaluate_expression(self, node):

        # NUMBER
        if node.node_type == "NUMBER":

            if "." in node.value:
                return "float"

            return "int"

        # STRING
        if node.node_type == "STRING":
            return "string"

        # IDENTIFIER
        if node.node_type == "IDENTIFIER":

            if node.value not in self.symbol_table:

                self.errors.append(
                    f"Semantic Error: Variable '{node.value}' not declared"
                )

                return "unknown"

            return self.symbol_table[node.value]

        # OPERATOR
        if node.node_type == "OPERATOR":

            left_type = self.evaluate_expression(
                node.children[0]
            )

            right_type = self.evaluate_expression(
                node.children[1]
            )

            # string operation unsupported
            if (
                left_type == "string"
                or right_type == "string"
            ):

                self.errors.append(
                    "Semantic Error: Invalid string operation"
                )

                return "unknown"

            # float dominance
            if (
                left_type == "float"
                or right_type == "float"
            ):
                return "float"

            return "int"
        
        
        # CONDITION_OPERATOR
        if node.node_type == "CONDITION_OPERATOR":

            self.evaluate_expression(node.children[0])

            self.evaluate_expression(node.children[1])

            return "bool"

        
        # LOGICAL_OPERATOR
        if node.node_type == "LOGICAL_OPERATOR":

            self.evaluate_expression(node.children[0])

            self.evaluate_expression(node.children[1])

            return "bool"


        return "unknown"


    # IF
    def visit_IF(self, node):

        self.evaluate_expression(node.children[0])

        self.analyze(node.children[1])

        if len(node.children) > 2:
            self.analyze(node.children[2])


    # WHILE
    def visit_WHILE(self, node):

        self.evaluate_expression(node.children[0])

        self.analyze(node.children[1])


    # BLOCK
    def visit_BLOCK(self, node):

        for child in node.children:
            self.analyze(child)  
