import ast


def analyze_syntax(code: str):
    try:
        ast.parse(code)

        return {
            "valid": True,
            "issues": []
        }

    except SyntaxError as error:
        return {
            "valid": False,
            "issues": [
                {
                    "type": "Syntax",
                    "severity": "High",
                    "message": error.msg,
                    "line": error.lineno
                }
            ]
        }