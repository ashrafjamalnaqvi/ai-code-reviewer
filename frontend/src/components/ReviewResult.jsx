import ScoreCard from "./ScoreCard";

function ReviewResult({ result }) {
  if (!result) {
    return (
      <div className="bg-gray-900 border border-gray-700 rounded-xl p-5 text-gray-400">
        Review result will appear here.
      </div>
    );
  }

  return (
    <div className="space-y-5">
      <ScoreCard score={result.score} />

      <div className="bg-gray-900 border border-gray-700 rounded-xl p-5">
        <h3 className="text-xl font-semibold text-white mb-3">
          Summary
        </h3>

        <p className="text-gray-300 whitespace-pre-wrap">
          {result.ai_feedback}
        </p>

        <div className="mt-4 grid grid-cols-2 gap-3 text-sm">
          <div className="bg-gray-800 p-3 rounded-lg">
            <p className="text-gray-400">Complexity</p>
            <p className="text-white font-medium">{result.complexity}</p>
          </div>

          <div className="bg-gray-800 p-3 rounded-lg">
            <p className="text-gray-400">Maintainability</p>
            <p className="text-white font-medium">
              {result.maintainability_index ?? "N/A"}
            </p>
          </div>
        </div>
      </div>

      <div className="bg-gray-900 border border-gray-700 rounded-xl p-5">
        <h3 className="text-xl font-semibold text-white mb-3">
          Issues Found
        </h3>

        {result.issues.length === 0 ? (
          <p className="text-green-400">No major issues found.</p>
        ) : (
          <div className="space-y-3">
            {result.issues.map((issue, index) => (
              <div
                key={index}
                className="bg-gray-800 border border-gray-700 rounded-lg p-4"
              >
                <div className="flex justify-between items-center">
                  <p className="text-white font-medium">{issue.type}</p>

                  <span
                    className={`text-xs px-2 py-1 rounded-full ${
                      issue.severity === "High"
                        ? "bg-red-500/20 text-red-400"
                        : issue.severity === "Medium"
                        ? "bg-yellow-500/20 text-yellow-400"
                        : "bg-blue-500/20 text-blue-400"
                    }`}
                  >
                    {issue.severity}
                  </span>
                </div>

                <p className="text-gray-300 mt-2">{issue.message}</p>

                {issue.line && (
                  <p className="text-gray-500 text-sm mt-1">
                    Line: {issue.line}
                  </p>
                )}
              </div>
            ))}
          </div>
        )}
      </div>

      <div className="bg-gray-900 border border-gray-700 rounded-xl p-5">
        <h3 className="text-xl font-semibold text-white mb-3">
          Improved Code
        </h3>

        <pre className="bg-black text-green-400 p-4 rounded-lg overflow-x-auto text-sm">
          <code>{result.improved_code}</code>
        </pre>
      </div>
    </div>
  );
}

export default ReviewResult;