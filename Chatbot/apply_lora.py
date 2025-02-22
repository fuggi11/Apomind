from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch
from transformers import AutoConfig, AutoModelForSequenceClassification, AutoTokenizer
model_path = "fine_tuned_model_tokenizer"  # Update this path if necessary

# Load model configuration
config = AutoConfig.from_pretrained(model_path)
# Load the model and tokenizer from the local directory
model = AutoModelForSequenceClassification.from_pretrained("fine_tuned_model_tokenizer")
tokenizer = AutoTokenizer.from_pretrained("fine_tuned_model_tokenizer")

# Put the model on the correct device (GPU if available, otherwise CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Prepare a test sentence
test_sentence = "This is a test sentence."

# Tokenize the test sentence
inputs = tokenizer(test_sentence, return_tensors="pt").to(device)

# Get the model’s output
with torch.no_grad():
    outputs = model(**inputs)

# Print the model's predictions
logits = outputs.logits
predictions = torch.argmax(logits, dim=-1)
print(f"Predicted label: {predictions.item()}")

