from sentence_transformers import SentenceTransformer
import numpy as np
from scipy.spatial.distance import cosine

# Load a pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small & fast for testing

# Predefined thinking style examples
thinking_styles = {
    "Concrete": "People would struggle to walk, buildings might collapse, and we'd need stronger materials.",
    "Abstract": "This would redefine Newtonian physics and change how we understand force and motion.",
    "Creative": "Humans would evolve differently, maybe shorter and stockier. Space travel would be a nightmare.",
    "Analytical": "F = ma, so weight doubles, meaning muscles must exert twice the force. Over time, biological adaptation might occur."
}

# Convert predefined styles to embeddings
style_embeddings = {style: model.encode(text) for style, text in thinking_styles.items()}

# User's response (replace this with actual input)
user_response = "Well, it will be tough to adapt to the changes. After that, we will change to it, and after that everything will be normal."

# Convert user response to an embedding
user_embedding = model.encode(user_response)

# Calculate similarity (lower cosine distance = more similar)
similarities = {style: 1 - cosine(user_embedding, emb) for style, emb in style_embeddings.items()}

# Normalize similarities to percentages
total = sum(similarities.values())
percentages = {style: round((score / total) * 100, 2) for style, score in similarities.items()}

# Print results
print("Thinking Style Classification (in %):")
for style, score in sorted(percentages.items(), key=lambda x: x[1], reverse=True):
    print(f"{style}: {score}%")
