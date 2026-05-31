import json
import os
import subprocess
import tempfile


def analyze_security(code: str):
    temp_file_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".py",
            delete=False,
            encoding="utf-8"
        ) as temp_file:
            temp_file.write(code)
            temp_file_path = temp_file.name

        result = subprocess.run(
            ["bandit", "-q", "-f", "json", temp_file_path],
            capture_output=True,
            text=True,
            timeout=10
        )

        if not result.stdout:
            return {"issues": []}

        data = json.loads(result.stdout)
        issues = []

        for item in data.get("results", []):
            severity = item.get("issue_severity", "LOW").capitalize()

            issues.append({
                "type": "Security",
                "severity": severity,
                "message": f"{item.get('test_name')}: {item.get('issue_text')}",
                "line": item.get("line_number")
            })

        return {"issues": issues}

    except Exception as error:
        return {
            "issues": [
                {
                    "type": "Security",
                    "severity": "Low",
                    "message": f"Security analysis failed: {str(error)}",
                    "line": None
                }
            ]
        }

    finally:
        if temp_file_path and os.path.exists(temp_file_path):
            os.remove(temp_file_path)