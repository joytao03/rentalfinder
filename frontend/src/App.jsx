import { useState } from "react";

function App() {
  const [selectedText, setSelectedText] = useState("");
  const [result, setResult] = useState(null);

  // 获取网页选中文字
  const getSelectedText = async () => {
    const [tab] = await chrome.tabs.query({
      active: true,
      currentWindow: true,
    });

    const [{ result }] = await chrome.scripting.executeScript({
      target: { tabId: tab.id },
      func: () => window.getSelection().toString(),
    });

    return result;
  };

  // 提取按钮
  const handleExtract = async () => {
    // 获取用户选中文字
    const text = await getSelectedText();

    setSelectedText(text);

    // 发给 FastAPI
    const response = await fetch("http://127.0.0.1:8000/extract", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();

    setResult(data);
  };

  return (
    <div
      style={{
        width: "350px",
        padding: "20px",
        fontFamily: "Arial",
      }}
    >
      <h2>Rental Finder</h2>

      <button
        onClick={handleExtract}
        style={{
          background: "#2563eb",
          color: "white",
          border: "none",
          padding: "10px 16px",
          borderRadius: "8px",
          cursor: "pointer",
        }}
      >
        Extract Selected Text
      </button>

      <div style={{ marginTop: "20px" }}>
        <strong>Selected Text:</strong>

        <p
          style={{
            background: "#f3f3f3",
            padding: "10px",
            borderRadius: "8px",
          }}
        >
          {selectedText || "No text selected"}
        </p>
      </div>

      {result && (
        <pre
          style={{
            marginTop: "20px",
            background: "#111",
            color: "#0f0",
            padding: "15px",
            borderRadius: "10px",
            overflowX: "auto",
          }}
        >
          {JSON.stringify(result, null, 2)}
        </pre>
      )}
    </div>
  );
}

export default App;