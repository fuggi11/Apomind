import express from "express";
import cors from "cors";
import fetch from "node-fetch"; // Required to call ChatGPT API

const app = express();
app.use(cors());
app.use(express.json());

app.post("/analyze-thinking", async (req, res) => {
  const { text } = req.body;

  // Send the user response to my API (ChatGPT)
  const chatGPTResponse = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer YOUR_OPENAI_API_KEY`
    },
    body: JSON.stringify({
      model: "gpt-4",
      messages: [
        { role: "system", content: "Analyze the user's response and classify their thinking style as either Abstract, Concrete, Sequential, Parallel, Risk-Taking, or Risk-Averse." },
        { role: "user", content: text }
      ]
    })
  });

  const data = await chatGPTResponse.json();
  res.json({ style: data.choices[0].message.content });
});

app.listen(3001, () => console.log("Server running on port 3001"));
