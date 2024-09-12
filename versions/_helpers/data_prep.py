import json
import csv

# Load the JSON data
input_file = r"C:\Users\ahmed\PycharmProjects\AOU Guide\data\retrieval_data\retrieval_data.json" # Replace with the path to your input JSON file
output_file = 'output.csv'  # Replace with the desired output CSV file name

with open(input_file, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Define the system message
system_message = {"from": "system", "value": "You are an AOU assistant for students."}

# Open the output CSV file in write mode
with open(output_file, 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out)

    # Write the header
    writer.writerow(['conversation', 'source', 'score'])

    # Process each prompt-completion pair
    for item in data:
        user_message = {"from": "user", "value": item["prompt"]}
        assistant_message = {"from": "assistant", "value": item["completion"]}

        # Combine the messages into a single list
        conversation = [system_message, user_message, assistant_message]

        # Write the conversation, source, and score as a single row in the CSV
        writer.writerow([json.dumps(conversation, ensure_ascii=False, ), 'nothing', '1'])

print("Conversion complete!")
