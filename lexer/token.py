class Token:

    def __init__(self, token_type, value, line):
        self.type = token_type
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.line:<5} {self.value:<15} {self.type.value}"