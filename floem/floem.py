import ast
import operator
import re

MISSING = None


class Floem:
    def __init__(self):
        self.env = {}

    def define(self, match):
        self.env[match.group(1)] = match.group(2)

    def replace(self, match):
        return self.env.get(match.group(1), "__import__('floem').MISSING")

    def control_flow(self, match):
        left, right = ast.literal_eval(match.group(1)), ast.literal_eval(match.group(3))
        op = match.group(2)

        if getattr(operator, op)(left, right):
            code = match.group(5)
            return f"{code[1:]}\n"


class Ksilem:
    """Regex based parser for
    preprocessor project floem"""

    RULES = {
        "define": r"!define\s([^\s]+)\sas\s(([^\n]+))?",
        "replace": r"<([^\s]+)>",
        "control_flow": r"^\s+!startif\s([^\s]+)\s(eq|ne|gt|lt|ge|le)\s(([^\n]+))((.|\n)*?)!endif$",
    }

    RULES = {k: re.compile(v, re.MULTILINE) for k, v in RULES.items()}

    def __init__(self):
        self.floem = Floem()

    def parse(self, text):
        for rule, pattern in self.RULES.items():
            text = re.sub(pattern, getattr(self.floem, rule), text)

        return text.strip()
