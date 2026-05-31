from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.review_models import ReviewRequest, ReviewResponse
from analyzers.syntax_analyzer import analyze_syntax
from analyzers.complexity_analyzer import analyze_complexity
from analyzers.security_analyzer import analyze_security
from analyzers.ai_reviewer import get_ai_review
from analyzers.scoring import calculate_score


app = FastAPI(title="AI Code Reviewer API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI Code Reviewer API is running"
    }


@app.post("/api/review", response_model=ReviewResponse)
def review_code(request: ReviewRequest):
    language = request.language.lower()
    code = request.code

    if language != "python":
        return {
            "score": 0,
            "complexity": "Unsupported",
            "maintainability_index": None,
            "issues": [
                {
                    "type": "Language",
                    "severity": "Medium",
                    "message": "Currently only Python code review is supported.",
                    "line": None
                }
            ],
            "ai_feedback": "Please select Python for now.",
            "improved_code": code
        }

    syntax_result = analyze_syntax(code)

    if not syntax_result["valid"]:
        issues = syntax_result["issues"]

        return {
            "score": calculate_score(issues, "Unknown"),
            "complexity": "Unknown",
            "maintainability_index": None,
            "issues": issues,
            "ai_feedback": "Fix syntax errors before deeper review.",
            "improved_code": code
        }

    complexity_result = analyze_complexity(code)
    security_result = analyze_security(code)

    static_summary = {
        "syntax": "valid",
        "complexity": complexity_result,
        "security": security_result
    }

    ai_result = get_ai_review(code, language, static_summary)

    issues = []
    issues.extend(syntax_result["issues"])
    issues.extend(complexity_result["issues"])
    issues.extend(security_result["issues"])
    issues.extend(ai_result.get("issues", []))

    score = calculate_score(
        issues,
        complexity_result["complexity"]
    )

    return {
        "score": score,
        "complexity": complexity_result["complexity"],
        "maintainability_index": complexity_result["maintainability_index"],
        "issues": issues,
        "ai_feedback": ai_result.get("feedback", ""),
        "improved_code": ai_result.get("improved_code", code)
    }