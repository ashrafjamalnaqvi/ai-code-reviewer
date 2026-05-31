function ScoreCard({ score }) {
  let label = "Needs Improvement";

  if (score >= 85) {
    label = "Excellent";
  } else if (score >= 70) {
    label = "Good";
  } else if (score >= 50) {
    label = "Average";
  }

  return (
    <div className="bg-gray-900 border border-gray-700 rounded-xl p-5">
      <p className="text-gray-400 text-sm">Code Quality Score</p>

      <div className="flex items-end gap-2 mt-2">
        <h2 className="text-5xl font-bold text-white">{score}</h2>
        <span className="text-gray-400 mb-2">/100</span>
      </div>

      <p className="mt-2 text-blue-400 font-medium">{label}</p>
    </div>
  );
}

export default ScoreCard;