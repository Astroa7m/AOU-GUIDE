import json

from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from tqdm import tqdm

# Initialize ChatGROQ client
chat = ChatGroq(model="Llama3-8b-8192")


def generate_expanded_completion_and_rejected_responses(prompt, completion):
    expand_messages = [
        SystemMessage(
            content="You are an AI assistant that elaborates on short completions while maintaining the original context. Respond ONLY with the expanded completion, without any introduction or conclusion."
        ),
        HumanMessage(content=f"""Given this prompt and short completion, expand on the completion while preserving the original information:
            Prompt: {prompt}
            Short Completion: {completion}
            The expanded response should:
            1. Maintain the original context and information
            2. Add more detail without introducing any new or incorrect information
            3. Ensure the elaboration is natural and provides more clarity
            4. If the completion is empty then elaborate and say I don't have any record or information of this etc.
            5. If the prompt and completion are in Arabic, REPLY in Arabic; if they are in English, REPLY in English. Do not mix languages.

            Respond ONLY with the expanded completion:""")
    ]

    print(f"Generating expanded completion for completion: {completion[:50]}...")  # Log the current prompt
    expanded_completion = chat.invoke(expand_messages)
    expanded_value = expanded_completion.content.strip()
    print("expanded completion response generated successfully.")
    completion = expanded_value
    print(f"{expanded_value[:50]}...")

    reject_messages = [
        SystemMessage(
            content="You are an AI assistant that generates incorrect or suboptimal responses. Respond ONLY with the rejected answer, without any introduction or conclusion."),
        HumanMessage(content=f"""Given this prompt and correct completion, generate ONLY an incorrect or suboptimal response:
                    Prompt: {prompt}
                    Correct Completion: {completion}
                    The incorrect response should:
                    1. Be related to the topic
                    2. Contain plausible but incorrect information
                    3. Possibly ignore part of the instructions
                    4. Be of similar length to the correct completion
                    5. If the prompt and completion are in Arabic REPLY in Arabic if they are in English REPLY in English Do Not Mix things up
                    Respond ONLY with the incorrect answer:""")
    ]

    print(f"Generating rejected response for prompt: {prompt[:50]}...")  # Log the current prompt
    rejected_response = chat.invoke(reject_messages)
    rejected_value = rejected_response.content.strip()
    print("Rejected response generated successfully.")
    print(f"{rejected_value[:50]}...")

    return (expanded_value, rejected_value)


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

        expanded_completion, rejected = generate_expanded_completion_and_rejected_responses(prompt, completion)

        # orpo_item = {
        #     "prompt": prompt,
        #     "chosen": [
        #         {"content": prompt, "role": "user"},
        #         {"content": completion, "role": "assistant"}
        #     ],
        #     "rejected": [
        #         {"content": prompt, "role": "user"},
        #         {"content": rejected, "role": "assistant"}
        #     ]
        # }

        orpo_item = {
            "prompt": prompt,
            "chosen": expanded_completion,
            "rejected": rejected
        }

        orpo_data.append(orpo_item)
        print(f"Item {index + 1} processed and added to ORPO data.")

    print(f"All items processed. Writing ORPO formatted data to {output_file}")
    with open(output_file, 'w', encoding="utf-8") as f:
        json.dump(orpo_data, f, indent=2)

    print(f"Conversion complete. ORPO formatted data saved to {output_file}")


# Usage
input_file = "./training_data/orpo_dataset.json"  # Replace with your input file name
output_file = "converted_orpo_dataset2.json"  # Replace with your desired output file name

# convert_to_orpo_format(input_file, output_file)




# Function to convert to the detailed format
def convert_format_back():

    input_data = []

    with open("converted_orpo_dataset2.json", 'r', encoding="utf-8") as f:
        input_data = json.load(f)

    converted_data = []

    for index, item in enumerate(tqdm(input_data, desc="Converting pcj to ORPO format")):
        # Structure for chosen completion
        chosen = [
            {
                "content": item["prompt"],
                "role": "user"
            },
            {
                "content": item["chosen"],
                "role": "assistant"
            }
        ]

        # Structure for rejected completion
        rejected = [
            {
                "content": item["prompt"],
                "role": "user"
            },
            {
                "content": item["rejected"],
                "role": "assistant"
            }
        ]

        # Append the new structured data
        converted_data.append({
            "prompt": item["prompt"],
            "chosen": chosen,
            "rejected": rejected
        })

    # Output the converted data to a new JSON file
    with open("orpo_dataset.json", "w") as f:
        json.dump(converted_data, f, indent=4)

    print("Conversion completed! Data saved to orpo_dataset.json")


# Convert the data
convert_format_back()


