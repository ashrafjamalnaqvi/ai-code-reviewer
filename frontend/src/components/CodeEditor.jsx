import Editor from "@monaco-editor/react";

function CodeEditor({ code, setCode, language }) {
  return (
    <div className="border border-gray-700 rounded-xl overflow-hidden">
      <Editor
        height="420px"
        language={language}
        value={code}
        theme="vs-dark"
        onChange={(value) => setCode(value || "")}
        options={{
          fontSize: 14,
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
          automaticLayout: true,
        }}
      />
    </div>
  );
}

export default CodeEditor;