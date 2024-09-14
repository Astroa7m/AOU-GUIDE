import json

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from tqdm import tqdm

# Initialize ChatGROQ client
chat = ChatGroq(model="Llama3-8b-8192")

def generate_rejected_response(prompt, completion):
    print(f"Generating rejected response for prompt: {prompt[:50]}...")  # Log the current prompt

    messages = [
        SystemMessage(content="You are an AI assistant that generates incorrect or suboptimal responses. Respond ONLY with the rejected answer, without any introduction or conclusion."),
        HumanMessage(content=f"""Given this prompt and correct completion, generate ONLY an incorrect or suboptimal response:
        Prompt: {prompt}
        Correct Completion: {completion}
        The incorrect response should:
        1. Be related to the topic
        2. Contain plausible but incorrect information
        3. Possibly ignore part of the instructions
        4. Be of similar length to the correct completion
        Respond ONLY with the incorrect answer:""")
    ]

    try:
        response = chat.invoke(messages)
        rejected_response = response.content.strip()
        print("Rejected response generated successfully.")
        print(f"{rejected_response[:50]}...")
        return rejected_response
    except Exception as e:
        print(f"Error occurred while generating rejected response: {str(e)}")
        return "Error: Unable to generate rejected response."

def convert_to_orpo_format(input_file, output_file):
    print(f"Starting conversion process. Reading input file: {input_file}")
    with open(input_file, 'r', encoding="utf-8") as f:
        data = json.load(f)

    orpo_data = []
    total_items = len(data)

    for index, item in enumerate(tqdm(data, desc="Converting to ORPO format")):
        print(f"\nProcessing item {index + 1} of {total_items}")
        prompt = item['prompt']
        completion = item['completion']

        rejected = generate_rejected_response(prompt, completion)

        orpo_item = {
            "prompt": prompt,
            "chosen": [
                {"content": prompt, "role": "user"},
                {"content": completion, "role": "assistant"}
            ],
            "rejected": [
                {"content": prompt, "role": "user"},
                {"content": rejected, "role": "assistant"}
            ]
        }

        orpo_data.append(orpo_item)
        print(f"Item {index + 1} processed and added to ORPO data.")

    print(f"All items processed. Writing ORPO formatted data to {output_file}")
    with open(output_file, 'w', encoding="utf-8") as f:
        json.dump(orpo_data, f, indent=2)

    print(f"Conversion complete. ORPO formatted data saved to {output_file}")


# Usage
input_file = "./training_data/orpo_dataset.json"  # Replace with your input file name
output_file = "converted_orpo_dataset.json"  # Replace with your desired output file name

convert_to_orpo_format(input_file, output_file)