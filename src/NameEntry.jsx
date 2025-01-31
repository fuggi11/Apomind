import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function NameEntry({ setName }) {
  const [inputName, setInputName] = useState(""); // Track input name
  const navigate = useNavigate();

  const handleSubmit = () => {
    if (!inputName.trim()) {
      alert("Please enter your name to continue.");
      return;
    }
    setName(inputName); // ✅ Store the name globally
    navigate("/assessment"); // ✅ Navigate to the test page
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h1 className="text-2xl font-bold">Enter Your Name</h1>
      <input
        type="text"
        className="w-64 p-2 mt-4 border rounded"
        placeholder="Enter your name"
        value={inputName}
        onChange={(e) => setInputName(e.target.value)}
      />
      <button
        className="mt-4 bg-blue-500 text-white px-4 py-2 rounded"
        onClick={handleSubmit}
      >
        Start Test
      </button>
    </div>
  );
}
