// src/Card.jsx
export function Card({ children }) {
    return <div className="p-4 border rounded shadow-md">{children}</div>;
  }
  
  export function CardContent({ children }) {
    return <div className="mt-2">{children}</div>;
  }
  