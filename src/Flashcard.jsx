import { useState } from "react";

export default function Flashcard({ question, name, storeResponse }) {
  const [response, setResponse] = useState("");
  const [feedback, setFeedback] = useState(""); // New feedback input
  const [thinkingStyle, setThinkingStyle] = useState(null);
  const [submitted, setSubmitted] = useState(false);
  const [loading, setLoading] = useState(false); // Loading state

  const submitResponse = async () => {
    if (!response.trim()) {
      alert("Please enter your response before submitting!");
      return;
    }

    setLoading(true); // Show loading state

    try {
      const res = await fetch("http://localhost:8000/analyze-thinking", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, questionId: question.id, text: response, feedback }),
      });

      console.log("Response Status:", res.status);

      if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);

      const data = await res.json();
      console.log("Received Data:", data);

      setThinkingStyle(data.style);
      storeResponse({ name, questionId: question.id, response, feedback, thinkingStyle: data.style });

      setSubmitted(true);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false); // Hide loading state
    }
  };

  return (
    <div className="border p-4 rounded w-96">
      <h2 className="text-lg font-bold">{question.question}</h2>
      
      <textarea
        className="w-full h-24 mt-4 p-2 border rounded"
        placeholder="Type your answer here..."
        value={response}
        onChange={(e) => setResponse(e.target.value)}
      />
      
      <textarea
        className="w-full h-16 mt-4 p-2 border rounded"
        placeholder="Provide feedback on this question..."
        value={feedback}
        onChange={(e) => setFeedback(e.target.value)}
      />

      <button
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
        onClick={submitResponse}
        disabled={loading} // Disable button while loading
      >
        {loading ? "Processing..." : "Submit"} {/* Show loading text */}
      </button>

      {submitted && <p className="mt-4 text-green-600">✅ Your response has been submitted.</p>}
      {thinkingStyle && <p className="mt-4 text-green-600">Your Thinking Style: <strong>{thinkingStyle}</strong></p>}
    </div>
  );
}





