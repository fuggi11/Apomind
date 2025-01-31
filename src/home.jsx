import { useNavigate } from "react-router-dom";
import { Card, CardContent } from "./Card";
import { Button } from "./Button";


export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="flex flex-col items-center justify-center h-screen">
      <Card className="p-6 text-center">
        <h1 className="text-2xl font-bold mb-4">Welcome to the Thinking Style Assessment</h1>
        <Button className="text-xl p-4 mt-4" onClick={() => navigate("/assessment")}>
          🧠 Take Assessment
        </Button>
      </Card>
    </div>
  );
}
