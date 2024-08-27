import json
with open("../data/retrieval_data/aou_retrieval_data.json", 'rb') as f:
    data = list(json.load(f))
    print(len(data))