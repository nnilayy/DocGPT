from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments


tokenizer = AutoTokenizer.from_pretrained("Biomistral")
model = AutoModelForCausalLM.from_pretrained("Biomistral")


academic_papers = load_dataset("scientific_papers", "pubmed")
medical_books = load_dataset("medical_books", split="train")


combined_dataset = datasets.concatenate_datasets(
    [academic_papers["train"], medical_books]
)


def preprocess_function(examples):
    return tokenizer(
        examples["text"], truncation=True, padding="max_length", max_length=512
    )


processed_dataset = combined_dataset.map(preprocess_function, batched=True)


training_args = TrainingArguments(
    output_dir="./doc-gpt-knowledge-model",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    logging_dir="./logs",
    logging_steps=10,
)


trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=processed_dataset,
    tokenizer=tokenizer,
)


trainer.train()
