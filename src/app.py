from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import subprocess

app = Flask(__name__)
CORS(app)

# ✅ Configure MySQL connection
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Aji2611#",
    "database": "Apomind"
}

@app.route("/analyze-thinking", methods=["POST"])
def analyze_thinking():
    data = request.get_json()
    
    # ✅ Check for missing fields
    required_fields = ["name", "questionId", "text"]
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields", "details": data}), 400

    print("Received Data:", data)

    response_text = data["text"]
    username = data["name"]
    questionid = data["questionId"]

    try:
        # ✅ Run Ollama for classification
        result = subprocess.run(
            ["ollama", "run", "mistral", f"Classify this response into Abstract, Concrete, Sequential, Parallel, Risk-Taking, or Risk-Averse: give a single word output if u feel like it comes in two or more categories give the names separated by commas '{response_text}'"],
            capture_output=True, text=True, check=True, encoding="utf-8", errors="ignore"
        )
        
        thinking_style = result.stdout.strip()
        print("Ollama Output:", thinking_style)

        # ✅ Store response in MySQL
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        query = "INSERT INTO responses (username, question_id, response_text, thinking_style) VALUES (%s, %s, %s, %s)"
        values = (username, questionid, response_text, thinking_style)
        cursor.execute(query, values)
        connection.commit()
        cursor.close()
        connection.close()

        response = jsonify({"style": thinking_style, "message": "Response saved successfully"})
        response.headers.add("Access-Control-Allow-Origin", "*")  # ✅ Manually add CORS header
        return response, 200

    except subprocess.CalledProcessError as e:
        return jsonify({"error": "Error processing request", "details": e.stderr}), 500

    except mysql.connector.Error as err:
        return jsonify({"error": "Database error", "details": str(err)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
