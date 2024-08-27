import json
with open("../data/retrieval_data/aou_training_dataset.json", 'rb') as f:
    data = list(json.load(f))
    print(len(data))