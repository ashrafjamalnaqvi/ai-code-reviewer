def calculate_score(issues, complexity_level):
    score = 100

    for issue in issues:
        severity = issue.get("severity", "Low")

        if severity == "High":
            score -= 10
        elif severity == "Medium":
            score -= 5
        else:
            score -= 2

    if complexity_level == "High":
        score -= 10
    elif complexity_level == "Medium":
        score -= 5

    return max(score, 0)