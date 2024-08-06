medci_dataset = load_dataset("medci", split="train")


def medci_preprocess_function(examples):
    input_text = (
        "Instruction: " + examples["instruction"] + " Input: " + examples["input"]
    )
    target_text = examples["response"]
    model_input = tokenizer(
        input_text, truncation=True, padding="max_length", max_length=512
    )
    labels = tokenizer(
        target_text, truncation=True, padding="max_length", max_length=512
    )["input_ids"]
    model_input["labels"] = labels
    return model_input


processed_medci_dataset = medci_dataset.map(medci_preprocess_function, batched=True)


training_args = TrainingArguments(
    output_dir="./doc-gpt-medci-model",
    per_device_train_batch_size=2,
    num_train_epochs=5,
    logging_dir="./logs",
    logging_steps=10,
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=processed_medci_dataset,
    tokenizer=tokenizer,
)


trainer.train()
