import json
import csv
from deep_translator import GoogleTranslator

# todo: Make sure of the prompts in helpers before use
class AcademicStaffHelper:

    @staticmethod
    def enter_academic_staff_data():
        academicStaffNameEn = input("Enter academic staff name in English: ")
        academicStaffNameAr = input("Enter academic staff name in Arabic: ")

        prompts = [
            f"Who is {academicStaffNameEn}?",
            f"من هو {academicStaffNameAr}؟",
            f"Tell me more about {academicStaffNameEn}",
            f"اخبرني المزيد عن {academicStaffNameAr}؟",
            f"What is doctor {academicStaffNameEn} email",
            f"ما هو البريد الالكتروني او الايميل الخاص {academicStaffNameAr}؟",
            f"What is the speciality of {academicStaffNameEn}",
            f"ما هو تخصص الدكتور {academicStaffNameAr}؟"
        ]

        for prompt in prompts:
            completion = input(prompt + " ")

            # Open and read the existing JSON file
            with open("retrieval_data/aou_training_dataset.json", mode="r", encoding="utf8") as f:
                data = json.load(f)

                # New record to append (assuming `prompts` and `completion` are defined)
                new_record = {"prompt": prompt, "completion": completion}

                # Append the new record to the list
                data.append(new_record)

            # Write the updated list back to a new JSON file
            with open('retrieval_data/aou_training_dataset.json', mode='w', encoding="utf8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

    @staticmethod
    def enter_academic_staff_data_from_csv():
        import csv
        import json

        # Path to your CSV and JSON files
        csv_file_path = 'path_to_your_csv_file.csv'
        json_file_path = 'path_to_your_json_file.json'

        # Read the last row of the CSV file
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            last_row = None
            for row in reader:
                last_row = row

        # Open and read the existing JSON file
        with open(json_file_path, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        # Append the last row from CSV as a new record in JSON format
        if last_row:
            new_record = {"prompt": last_row["prompt_column_name"], "completion": last_row["completion_column_name"]}
            data.append(new_record)

        # Write the updated list back to the JSON file
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    @staticmethod
    def write_academic_staff_data_to_csv():

        # Function to get user input and translate Arabic fields
        def get_user_input():
            id = input("Enter id: ")
            name = input("Enter name: ")
            name_ar = GoogleTranslator(source='auto', target='ar').translate(text=name)
            title = input("Enter title: ")
            title_ar = GoogleTranslator(source='auto', target='ar').translate(text=title)
            email = input("Enter email: ")
            specialization = input("Enter specialization: ")
            specialization_ar = GoogleTranslator(source='auto', target='ar').translate(text=specialization)
            bio = input("Enter biography: ")
            bio_ar = GoogleTranslator(source='auto', target='ar').translate(text=bio)
            office_hours = input("Enter office hours: ")
            link = input("Enter link: ")
            position = input("Enter position: ")
            position_ar = GoogleTranslator(source='auto', target='ar').translate(text=position)

            return {
                "id": id,
                "name": name,
                "nameArabic": name_ar,
                "title": title,
                "titleArabic": title_ar,
                "email": email,
                "Biography": bio,
                "BiographyArabic": bio_ar,
                "office_hours": office_hours,
                "specialization": specialization,
                "specializationArabic": specialization_ar,
                "position": position,
                "positionArabic": position_ar,
                "link": link,
            }

        # Data to be written to CSV
        data = []

        # Add rows based on user input
        data.append(get_user_input())

        # Define the CSV file path
        csv_file_path = r'/data/aou_data/csv/AcademicStaff.csv'

        # Writing to CSV file
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            # Define fieldnames (column headers)
            fieldnames = ["id", "name", "nameArabic", "title", "titleArabic", "email", "Biography", "BiographyArabic",
                          "office_hours", "specialization", "specializationArabic", "position", "positionArabic",
                          "link"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the data
            for row in data:
                writer.writerow(row)


class MajorHelpers:

    @staticmethod
    def write_major_prompts():
        # add arabic prompt and completion for each prompt
        faculty = ""

        programs = []

        programs_prompts = []

        for program in programs:
            programs_prompts.append(
                f"What is BA Hons in {program}?",
            )

            programs_prompts.append(
                f"Can you tell me more about {program} program?"
            )

            programs_prompts.append(
                f"Where can I find the academic plan for {programs}"
            )

            programs_prompts.append(
                f"I want the academic plan for {programs} program"
            )

        prompts = [
            f"What is the Faculty of {faculty} in AOU?"
            f"What is the Faculty of {faculty} at the university?",
            f"What are the offered courses by the {faculty} in AOU?",
            f"What programs are offered by {faculty}?"
            f"If I chose {faculty} to study in, what programs are offered by it?"
        ]

    @staticmethod
    def write_major_data_to_csv():

        # Function to get user input and translate Arabic fields
        def get_user_input():
            id = input("Enter id: ")
            name = input("Enter name: ")
            name_ar = GoogleTranslator(source='auto', target='ar').translate(text=name)
            required_credit = int(input("Enter required credit: "))
            degree_level = "Undergraduate" if int(input("Enter degree level (1-Undergraduate, else-Postgraduate): ")) == 1 else "Postgraduate"
            degree_level_ar = GoogleTranslator(source='auto', target='ar').translate(text=degree_level)
            description = input("Enter description: ")
            description_ar = GoogleTranslator(source='auto', target='ar').translate(text=description)
            study_plan = input("Enter study plan link: ")


            return {
                "id": id,
                "name": name,
                "nameArabic": name_ar,
                "requiredCredit": required_credit,
                "degreeLevel": degree_level,
                "degreeLevelArabic": degree_level_ar,
                "description": description,
                "descriptionAr": description_ar,
                "studyPlan": study_plan,
            }

        # Data to be written to CSV
        data = []

        # Add rows based on user input
        data.append(get_user_input())

        # Define the CSV file path
        csv_file_path = r'C:\Users\ahmed\PycharmProjects\AOU Guide\data\aou_data\csv\Major.csv'

        # Writing to CSV file
        with open(csv_file_path, mode='a', newline='', encoding='utf-8') as file:
            # Define fieldnames (column headers)
            fieldnames = ["id", "name", "nameArabic", "requiredCredit", "degreeLevel", "degreeLevelArabic",
                          "description", "descriptionAr", "studyPlan"]

            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write the data
            for row in data:
                writer.writerow(row)


MajorHelpers.write_major_data_to_csv()
