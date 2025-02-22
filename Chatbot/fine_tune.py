import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset


model_path = "mistral"  # If using HF
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Load dataset (Modify this for your dataset)
dataset = load_dataset("json", data_files="corrected_data.jsonl") # Example dataset

# Load model in FP16 for fine-tuning
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Configure LoRA
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    lora_dropout=0.1,
    target_modules=["q_proj", "v_proj"],  # Targeting attention layers
    bias="none",
    task_type="CAUSAL_LM",
)

# Apply LoRA
model = prepare_model_for_kbit_training(model)
model = get_peft_model(model, lora_config)

# Training Arguments
training_args = TrainingArguments(
    output_dir="./lora_adapter",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=16,
    evaluation_strategy="steps",
    save_strategy="steps",
    save_steps=100,
    logging_steps=50,
    learning_rate=2e-4,
    weight_decay=0.01,
    fp16=True,
    push_to_hub=False,
    report_to="none"
)

# Train Model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
)

trainer.train()

# Save LoRA adapter (not full model)
model.save_pretrained("./lora_adapter")
tokenizer.save_pretrained("./lora_adapter")

print("✅ Fine-tuning complete! LoRA adapter saved.")
