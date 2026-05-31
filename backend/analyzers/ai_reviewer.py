def get_ai_review(code: str, language: str, static_summary: dict):
    improved_code = code
    issues = []

    if "os.system" in code:
        improved_code = """import subprocess


def run_command(command):
    try:
        result = subprocess.run(
            command,
            shell=False,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout

    except subprocess.CalledProcessError as error:
        return f"Command failed: {error}"


print(run_command(["ls"]))
"""

        issues.append({
            "type": "Security",
            "severity": "High",
            "message": "Avoid using os.system() because it can lead to command injection. Use subprocess.run() with shell=False instead.",
            "line": None
        })

    elif "eval(" in code:
        improved_code = code.replace("eval(", "# Avoid eval for security reasons. Refactor this logic safely.\n# eval(")

        issues.append({
            "type": "Security",
            "severity": "High",
            "message": "Avoid using eval() because it can execute unsafe code.",
            "line": None
        })

    elif "print(" in code and "def " in code:
        issues.append({
            "type": "Best Practice",
            "severity": "Low",
            "message": "Use return values inside functions instead of only printing output.",
            "line": None
        })

    else:
        issues.append({
            "type": "Best Practice",
            "severity": "Low",
            "message": "Code looks okay. Add comments, error handling, and meaningful variable names where needed.",
            "line": None
        })

    feedback = """
Static analysis completed successfully.

This version uses rule-based review because API quota is unavailable.
The project still checks syntax, complexity, maintainability, and security issues using Python analysis tools.
"""

    return {
        "feedback": feedback.strip(),
        "improved_code": improved_code,
        "issues": issues
    }