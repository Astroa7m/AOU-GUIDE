import json
def enterTutorData():
    tutorNameEn = input("Enter tutor name in English: ")
    tutorNameAr = input("Enter tutor name in Arabic: ")

    prompts = [
        f"Who is {tutorNameEn}?",
        f"من هو {tutorNameAr}؟",
        f"Tell me more about {tutorNameEn}",
        f"اخبرني المزيد عن {tutorNameAr}؟",
        f"What is doctor {tutorNameEn} email",
        f"ما هو البريد الالكتروني او الايميل الخاص {tutorNameAr}؟",
        f"What is the speciality of {tutorNameEn}",
        f"ما هو تخصص الدكتور {tutorNameAr}؟"
    ]

    for prompt in prompts:
        completion = input(prompt+" ")

        # Open and read the existing JSON file
        with open("retrieval_data/aou_retrieval_data.json", mode="r", encoding="utf8") as f:
            data = json.load(f)

            # New record to append (assuming `prompts` and `completion` are defined)
            new_record = {"prompt": prompt, "completion": completion}

            # Append the new record to the list
            data.append(new_record)

        # Write the updated list back to a new JSON file
        with open('retrieval_data/aou_retrieval_data.json', mode='w', encoding="utf8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)




enterTutorData()

