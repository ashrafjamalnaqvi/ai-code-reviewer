import { useState } from "react";
import CodeEditor from "./components/CodeEditor";
import ReviewResult from "./components/ReviewResult";
import { reviewCode } from "./api/reviewApi";

function App() {
  const [language, setLanguage] = useState("python");

  const [code, setCode] = useState(`import os

def run_command(command):
    os.system(command)

run_command("ls")
`);

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleReview = async () => {
    try {
      setLoading(true);

      const data = await reviewCode({
        language,
        code,
      });

      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Backend connection error. Make sure FastAPI is running.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white">
      <nav className="border-b border-gray-800 px-8 py-5">
        <h1 className="text-2xl font-bold">
          AI Code Reviewer
        </h1>
        <p className="text-gray-400 text-sm">
          Static analysis + AI-powered code feedback
        </p>
      </nav>

      <main className="p-8 grid grid-cols-1 lg:grid-cols-2 gap-8">
        <section>
          <div className="flex justify-between items-center mb-4">
            <div>
              <h2 className="text-xl font-semibold">
                Paste Your Code
              </h2>
              <p className="text-gray-400 text-sm">
                Currently supports Python review.
              </p>
            </div>

            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="bg-gray-900 border border-gray-700 rounded-lg px-3 py-2"
            >
              <option value="python">Python</option>
            </select>
          </div>

          <CodeEditor
            code={code}
            setCode={setCode}
            language={language}
          />

          <button
            onClick={handleReview}
            disabled={loading}
            className="mt-5 w-full bg-blue-600 hover:bg-blue-700 disabled:bg-gray-700 px-5 py-3 rounded-xl font-medium"
          >
            {loading ? "Reviewing Code..." : "Review Code"}
          </button>
        </section>

        <section>
          <h2 className="text-xl font-semibold mb-4">
            Review Output
          </h2>

          <ReviewResult result={result} />
        </section>
      </main>
    </div>
  );
}

export default App;