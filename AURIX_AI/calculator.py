import re
import ast
import operator

# ==========================================
# SAFE OPERATIONS MAP
# ==========================================

ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

# ==========================================
# SAFE EVALUATOR (NO DANGEROUS EVAL)
# ==========================================

def safe_eval(node):

    if isinstance(node, ast.Num):  # numbers
        return node.n

    elif isinstance(node, ast.BinOp):
        left = safe_eval(node.left)
        right = safe_eval(node.right)
        return ops[type(node.op)](left, right)

    elif isinstance(node, ast.Expression):
        return safe_eval(node.body)

    else:
        raise ValueError("Invalid expression")

# ==========================================
# SMART CALCULATOR FUNCTION
# ==========================================

def calculate(expression):

    try:

        expression = expression.lower().strip()

        # Replace words with math symbols
        replacements = {
            "plus": "+",
            "minus": "-",
            "times": "*",
            "multiplied by": "*",
            "multiply": "*",
            "x": "*",
            "×": "*",
            " X ": "*",
            "into": "*",
            "divided by": "/",
            "divide": "/",
            "mod": "%",
            "power": "**",
            "raised to": "**"
        }

        for word, symbol in replacements.items():
            expression = expression.replace(word, symbol)

        # Remove extra words
        remove_words = [
            "calculate",
            "what is",
            "solve",
            "equals",
            "equal to"
        ]

        for word in remove_words:
            expression = expression.replace(word, "")

        expression = expression.strip()

        # Allow only safe characters
        if not re.fullmatch(r"[0-9+\-*/().%\s]+", expression):
            return "Invalid mathematical expression."

        # Parse safely using AST
        node = ast.parse(expression, mode="eval")
        result = safe_eval(node)

        return f"The answer is {result}"

    except ZeroDivisionError:
        return "Division by zero is not allowed."

    except Exception:
        return "Sorry, I couldn't calculate that."