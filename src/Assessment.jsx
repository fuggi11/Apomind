import { useState } from "react";
import Flashcard from "./Flashcard";

const questions = [
  {
    "id": 1,
    "question": "Imagine a world where gravity suddenly became twice as strong. How would everyday life and scientific principles change?"
  },
  {
    "id": 2,
    "question": "You need to explain the concept of prime numbers to someone with no math background. How would you do it?"
  },
  {
    "id": 3,
    "question": "Scientists discover a new element with properties between metals and nonmetals. How would you classify and test it?"
  },
  {
    "id": 4,
    "question": "A programmer is optimizing an algorithm. What factors should they consider when deciding between time complexity and space complexity?"
  },
  {
    "id": 5,
    "question": "A new drug shows promising results in small-scale testing. What steps should be taken before making it available to the public?"
  },
  {
    "id": 6,
    "question": "You are given an unknown circuit with multiple components. How would you systematically determine its function?"
  },
  {
    "id": 7,
    "question": "A startup is considering launching an innovative but untested product. What factors would you consider before taking the risk, and would you proceed?"
  },
  {
    "id": 8,
    "question": "A spacecraft is traveling towards Mars, and a critical system fails. How would you approach troubleshooting and prioritizing fixes?"
  },
  {
    "id": 9,
    "question": "A company is deciding whether to invest in quantum computing for faster processing. What aspects should they evaluate before making a decision?"
  },
  {
    "id": 10,
    "question": "You are tasked with designing a secure encryption method for online transactions. What principles would you prioritize?"
  }
];

export default function Assessment({ name }) {
  const [index, setIndex] = useState(0);
  const [responses, setResponses] = useState([]);
  const [key, setKey] = useState(0); // To reset the Flashcard component

  const storeResponse = (data) => {
    setResponses((prev) => [...prev, data]);
    console.log("Updated Dataset:", responses);
  };

  const changeQuestion = (direction) => {
    setIndex((prev) => {
      const newIndex = Math.max(0, Math.min(prev + direction, questions.length - 1));
      setKey((prevKey) => prevKey + 1); // Change key to force input reset
      return newIndex;
    });
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <h2 className="text-xl font-bold">Welcome, {name}!</h2>
      <Flashcard 
        key={key} // Forces re-render to clear input
        question={questions[index]} 
        name={name} 
        storeResponse={storeResponse} 
      />

      <div className="mt-4 flex space-x-4">
        <button
          className="bg-gray-500 text-white px-4 py-2 rounded"
          onClick={() => changeQuestion(-1)}
        >
          Previous
        </button>
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded"
          onClick={() => changeQuestion(1)}
        >
          Next
        </button>
      </div>
    </div>
  );
}



