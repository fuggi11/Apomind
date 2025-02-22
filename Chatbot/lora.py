import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model
from safetensors.torch import save_file
from datasets import load_dataset

# Ensure we're using GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"

# Model name (distilGPT2 in this case)
model_name = "distilbert/distilgpt2"
print(model_name)
# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)

# 4-bit Quantization Configuration
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
)

# ✅ Auto device map + allow CPU offloading
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=quantization_config,
    torch_dtype=torch.float16,
    device_map="auto",  # Automatically distributes across GPU & CPU
    offload_state_dict=True,  # ✅ Offloads excess weights to CPU if needed
)

# Load dataset for fine-tuning
dataset = load_dataset('json', data_files='codata.jsonl')

# Modify LoRA configuration to match available attention layers
lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["c_attn", "c_proj"],  # Apply LoRA to specific Linear layers
    lora_dropout=0.1
)


# Apply LoRA to the model
peft_model = get_peft_model(model, lora_config)

import torch
from torch.utils.data import DataLoader

import torch
from torch.utils.data import DataLoader

def fine_tune_model(model, tokenizer, dataset):
    model.train()

    # Check if pad_token is set, if not set it to eos_token
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    def tokenize_fn(examples):
        # Tokenizing the dataset with padding and truncation
        encoding = tokenizer(examples['prompt'], padding=True, truncation=True, return_tensors="pt")
        
        # For language models, labels are usually the same as the input_ids
        encoding['labels'] = encoding['input_ids'].clone()  # Copy input_ids as labels for language modeling tasks
        
        return encoding

    # Tokenize the dataset
    tokenized_dataset = dataset.map(tokenize_fn, batched=True)

    train_dataset = tokenized_dataset["train"]

    # DataLoader for batching
    train_dataloader = DataLoader(train_dataset, batch_size=8)

    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)  # Ensure the model is moved to the device (GPU or CPU)

    # Training loop
    for epoch in range(3):  # Example: 3 epochs
        for batch in train_dataloader:
            optimizer.zero_grad()

            # The batch now includes both 'input_ids' and 'labels'
            input_ids = torch.cat(batch["input_ids"]).to(device)
            labels = torch.cat(batch["labels"]).to(device)

            # Forward pass
            outputs = model(input_ids=input_ids, labels=labels)
            loss = outputs.loss
            loss.backward()

            optimizer.step()

        print(f"Epoch {epoch + 1}: Loss {loss.item()}")

# Fine-tune the model
fine_tune_model(peft_model, tokenizer, dataset)
from safetensors.torch import save_model

# After training is complete
save_model(peft_model, "fine_tuned_model.safetensors")

# Optionally, save the tokenizer as well
tokenizer.save_pretrained("fine_tuned_model_tokenizer")


# Check where the model is loaded
print(peft_model.hf_device_map)
