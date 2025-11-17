import sympy as sp

def clean_expression(expr: str):
    expr = expr.lower()
    for token in ("integrate", "differentiate", "simplify", "solve", "dx"):
        expr = expr.replace(token, "")
    return expr.strip()

def verify_equation(expression: str, operation: str):
    try:
        x = sp.symbols('x')
        expr_raw = clean_expression(expression)
        # If the user typed an equation with '=', preserve that for Solve
        if operation == "Solve" and "=" in expression:
            left, right = expression.split("=", 1)
            left = sp.sympify(left)
            right = sp.sympify(right)
            return sp.solve(left - right)
        expr = sp.sympify(expr_raw)

        if operation == "Integrate":
            return sp.integrate(expr, x)
        elif operation == "Differentiate":
            return sp.diff(expr, x)
        elif operation == "Simplify":
            return sp.simplify(expr)
        elif operation == "Solve":
            return sp.solve(expr)
        else:
            return "Unknown operation"
    except Exception as e:
        return f"Verification error: {e}"
