import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NameEntry from "./NameEntry";
import Assessment from "./Assessment";
import { useState } from "react";

export default function App() {
  const [name, setName] = useState(""); // ✅ Store the user's name

  return (
    <Router>
      <Routes>
        <Route path="/" element={<NameEntry setName={setName} />} />
        <Route path="/assessment" element={<Assessment name={name} />} />
      </Routes>
    </Router>
  );
}


