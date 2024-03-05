from transformers import AutoTokenizer, DataCollatorWithPadding, AutoModelForSequenceClassification, TrainingArguments, Trainer
import json
import evaluate
import numpy as np
import torch

# Cargar el conjunto de datos
with open('/home/raulbreton/proyecto_modular/openhire/bert/data/bert_df.json', 'r') as json_file:
    dataset = json.load(json_file)

# Separar las descripciones y las etiquetas
descriptions = [item["description"] for item in dataset]
labels = [item["label"] for item in dataset]

tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")

# Preprocess each example individually
tokenized_dataset = tokenizer(descriptions, truncation=True, padding=True)

data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

# Convert the tokenized dataset to a PyTorch Dataset
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: val[idx] for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

train_dataset = CustomDataset(tokenized_dataset, labels)

accuracy = evaluate.load("accuracy")

def compute_metrics(eval_pred):
    predictions, labels = eval_pred
    predictions = np.argmax(predictions, axis=1)
    return accuracy.compute(predictions=predictions, references=labels)

id2label = {0: "NEGATIVE", 1: "POSITIVE"}
label2id = {"NEGATIVE": 0, "POSITIVE": 1}

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert/distilbert-base-uncased", num_labels=2, id2label=id2label, label2id=label2id
)

training_args = TrainingArguments(
    output_dir="bert_classifier",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=train_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics,
)

trainer.train()