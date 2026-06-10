import math

class Calculator:
    def __init__(self):
        self.last_result = " "

    def calculate(self, expression: str):
        """
        Calcula uma expressão matematica de forma controlada.
        """
        if not expression:
            return " "
        
        safe_environment = {
            "__builtins__": None,  # Desabilita acesso a built-ins

            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),

            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "factorial": math.factorial,
            "abs": abs,
            "pow": pow,

            "pi": math.pi,
            "e": math.e,
        }
        try:
            result = eval(expression, safe_environment)

            if isinstance(result, (int, float)):
                result = round(result, 10)

            self.last_result = str(result)     
            return result
        except Exception:
            return "Erro: Expressão inválida"
        