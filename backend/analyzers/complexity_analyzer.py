from radon.complexity import cc_visit
from radon.metrics import mi_visit


def analyze_complexity(code: str):
    issues = []

    try:
        blocks = cc_visit(code)
        maintainability_index = mi_visit(code, True)

        max_complexity = 1

        for block in blocks:
            max_complexity = max(max_complexity, block.complexity)

            if block.complexity >= 11:
                issues.append({
                    "type": "Complexity",
                    "severity": "High",
                    "message": f"{block.name} has high cyclomatic complexity: {block.complexity}",
                    "line": block.lineno
                })

            elif block.complexity >= 6:
                issues.append({
                    "type": "Complexity",
                    "severity": "Medium",
                    "message": f"{block.name} has medium cyclomatic complexity: {block.complexity}",
                    "line": block.lineno
                })

        if maintainability_index < 50:
            issues.append({
                "type": "Maintainability",
                "severity": "Medium",
                "message": f"Maintainability index is low: {round(maintainability_index, 2)}",
                "line": None
            })

        if max_complexity >= 11:
            complexity_level = "High"
        elif max_complexity >= 6:
            complexity_level = "Medium"
        else:
            complexity_level = "Low"

        return {
            "complexity": complexity_level,
            "maintainability_index": round(maintainability_index, 2),
            "issues": issues
        }

    except Exception as error:
        return {
            "complexity": "Unknown",
            "maintainability_index": None,
            "issues": [
                {
                    "type": "Complexity",
                    "severity": "Low",
                    "message": f"Could not analyze complexity: {str(error)}",
                    "line": None
                }
            ]
        }