import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import filedialog

from lexer.lexer import Lexer
from parser.parser import Parser
from semantic.semantic_analyzer import SemanticAnalyzer


class CompilerGUI:

    def __init__(self, root):

        self.root = root

        self.root.title("Mini Compiler")

        self.root.geometry("1400x900")

        self.create_widgets()

    def create_widgets(self):

        # TITLE
        title = tk.Label(
            self.root,
            text="MINI COMPILER",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=10)

        # TOP FRAME
        top_frame = tk.Frame(self.root)

        top_frame.pack(fill=tk.BOTH, expand=True)

        # SOURCE CODE
        source_frame = tk.Frame(top_frame)

        source_frame.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True,
            padx=10
        )

        source_label = tk.Label(
            source_frame,
            text="SOURCE CODE"
        )

        source_label.pack()

        self.source_text = scrolledtext.ScrolledText(
            source_frame,
            width=50,
            height=25,
            font=("Consolas", 12)
        )

        self.source_text.bind(
            "<KeyRelease>",
            self.highlight_syntax
        )


        self.source_text.pack(fill=tk.BOTH, expand=True)

        # TOKENS
        token_frame = tk.Frame(top_frame)

        token_frame.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True,
            padx=10
        )

        token_label = tk.Label(
            token_frame,
            text="TOKENS"
        )

        token_label.pack()

        self.token_text = scrolledtext.ScrolledText(
            token_frame,
            width=50,
            height=25,
            font=("Consolas", 11)
        )

        self.token_text.pack(fill=tk.BOTH, expand=True)

        # AST
        ast_label = tk.Label(
            self.root,
            text="AST TREE"
        )

        ast_label.pack()

        self.ast_text = scrolledtext.ScrolledText(
            self.root,
            height=8,
            font=("Consolas", 11)
        )

        self.ast_text.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=5
        )

        # SYMBOL TABLE
        symbol_label = tk.Label(
            self.root,
            text="SYMBOL TABLE"
        )

        symbol_label.pack()

        self.symbol_text = scrolledtext.ScrolledText(
            self.root,
            height=6,
            font=("Consolas", 11)
        )

        self.symbol_text.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=5
        )

        # ERRORS
        error_label = tk.Label(
            self.root,
            text="ERRORS"
        )

        error_label.pack()

        self.error_text = scrolledtext.ScrolledText(
            self.root,
            height=4,
            fg="red",
            font=("Consolas", 11)
        )

        self.error_text.pack(
            fill=tk.BOTH,
            expand=True,
            padx=10,
            pady=5
        )


        # BUTTON FRAME
        button_frame = tk.Frame(self.root)

        button_frame.pack(pady=10)


        # OPEN BUTTON
        open_button = tk.Button(
            button_frame,
            text="OPEN FILE",
            command=self.open_file,
            bg="#2196F3",
            fg="black",
            font=("Arial", 12, "bold")
        )

        open_button.pack(side=tk.LEFT, padx=10)


        # COMPILE BUTTON
        compile_button = tk.Button(
            button_frame,
            text="COMPILE",
            command=self.compile_code,
            bg="#4CAF50",
            fg="black",
            font=("Arial", 12, "bold")
        )

        compile_button.pack(side=tk.LEFT, padx=10)


        # SAVE BUTTON
        save_button = tk.Button(
            button_frame,
            text="SAVE",
            command=self.save_file,
            bg="#FF9800",
            fg="black",
            font=("Arial", 12, "bold")
        )

        save_button.pack(side=tk.LEFT, padx=10)


    def compile_code(self):

        # temizle
        self.token_text.delete(1.0, tk.END)
        self.ast_text.delete(1.0, tk.END)
        self.error_text.delete(1.0, tk.END)
        self.symbol_text.delete(1.0, tk.END)

        source_code = self.source_text.get(
            1.0,
            tk.END
        )

        try:

            # LEXER
            lexer = Lexer(source_code)

            tokens = lexer.tokenize()

            for token in tokens:
                self.token_text.insert(
                    tk.END,
                    str(token) + "\n"
                )

            # lexical errors
            lexical_errors = [
                t for t in tokens
                if t.type.value == "ERROR"
            ]

            for error in lexical_errors:

                self.error_text.insert(
                    tk.END,
                    f"Lexical Error at line "
                    f"{error.line}: {error.value}\n"
                )

            # PARSER
            parser = Parser(tokens)

            ast = parser.parse()

            self.print_ast(ast)

            # SEMANTIC
            semantic = SemanticAnalyzer()

            semantic.analyze(ast)

            for error in semantic.errors:

                self.error_text.insert(
                    tk.END,
                    error + "\n"
                )

            # no errors
            if (
                not lexical_errors
                and not semantic.errors
            ):

                self.error_text.insert(
                    tk.END,
                    "Compilation successful."
                )

            # SYMBOL TABLE DISPLAY
            for name, var_type in semantic.symbol_table.items():

                self.symbol_text.insert(
                    tk.END,
                    f"{name:<15} {var_type}\n"
                )    

        except Exception as e:

            self.error_text.insert(
                tk.END,
                f"Parser Error: {str(e)}"
            )

    def print_ast(self, node, level=0):

        indent = "  " * level

        self.ast_text.insert(
            tk.END,
            f"{indent}{node.node_type}: "
            f"{node.value}\n"
        )

        for child in node.children:
            self.print_ast(child, level + 1)

    

    def open_file(self):

        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt")]
        )

        if not file_path:
            return

        with open(file_path, "r") as file:

            content = file.read()

        self.source_text.delete(1.0, tk.END)

        self.source_text.insert(tk.END, content)


    def save_file(self):

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")]
        )

        if not file_path:
            return

        source_code = self.source_text.get(
            1.0,
            tk.END
        )

        tokens = self.token_text.get(
            1.0,
            tk.END
        )

        ast = self.ast_text.get(
            1.0,
            tk.END
        )

        symbols = self.symbol_text.get(
            1.0,
            tk.END
        )

        errors = self.error_text.get(
            1.0,
            tk.END
        )

        report = f"""
    ==============================
    SOURCE CODE
    ==============================

    {source_code}

    ==============================
    TOKENS
    ==============================

    {tokens}

    ==============================
    AST TREE
    ==============================

    {ast}

    ==============================
    SYMBOL TABLE
    ==============================

    {symbols}

    ==============================
    ERRORS
    ==============================

    {errors}
    """

        with open(file_path, "w") as file:

            file.write(report)

        messagebox.showinfo(
            "Saved",
            "Compiler report saved successfully"
        )


    def highlight_syntax(self, event=None):

        content = self.source_text.get(
            "1.0",
            tk.END
        )

        self.source_text.tag_remove(
            "keyword",
            "1.0",
            tk.END
        )

        keywords = [
            "int",
            "float",
            "if",
            "else",
            "while",
            "print"
        ]

        for keyword in keywords:

            start = "1.0"

            while True:

                pos = self.source_text.search(
                    keyword,
                    start,
                    stopindex=tk.END
                )

                if not pos:
                    break

                end = f"{pos}+{len(keyword)}c"

                self.source_text.tag_add(
                    "keyword",
                    pos,
                    end
                )

                start = end

        self.source_text.tag_config(
            "keyword",
            foreground="#00BFFF"
        )

