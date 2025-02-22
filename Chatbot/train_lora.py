# train_lora.py
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, TaskType
from datasets import load_dataset
import torch
import bitsandbytes as bnb

# Load the model in 4-bit (to match Ollama's Mistral Q4_0)
model_name = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    load_in_4bit=True,
    quantization_config=bnb.nn.Linear4bit(),
)

# Load dataset
dataset = load_dataset("json", data_files="data.jsonl", split="train")

# LoRA Configuration
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.05,
    task_type=TaskType.CAUSAL_LM,
)

# Attach LoRA
model = get_peft_model(model, lora_config)

# Training settings
training_args = TrainingArguments(
    output_dir="./lora-output",
    per_device_train_batch_size=1,
    num_train_epochs=3,
    logging_steps=10,
    save_steps=100,
    save_total_limit=2,
    evaluation_strategy="no",
)

trainer = Trainer(
    model=model,
    train_dataset=dataset,
    args=training_args,
)

# Train LoRA
trainer.train()

# Save the LoRA adapter
model.save_pretrained("lora-output")
print("✅ LoRA training complete. Saved to 'lora-output' folder.")
