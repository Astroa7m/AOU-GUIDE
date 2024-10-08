import csv
import enum
import json

from deep_translator import GoogleTranslator

id_column_name = "\ufeffid"


def translate_to_arabic(text):
    try:
        if text:
            translator = GoogleTranslator(source='auto', target='ar')
            return translator.translate(text)
        return ""
    except Exception as ex:
        print(f"Failed with at\n{text}")
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)


# todo: Make sure of the prompts in helpers before use
# todo: Make sure of the modes of appending and writing of the data
class AcademicStaffDataHelpers:

    @staticmethod
    def create_academic_staff_prompts_and_completion_from_csv():
        prompts_and_completion = []

        with open("aou_data/csv/AcademicStaff.csv", 'r', newline='', encoding='utf-8') as f:
            reader = (csv.DictReader(f))

            academic_staff = {}

            for row in reader:
                academic_staff[row['name']] = row

            for name, info in academic_staff.items():
                print(f"Creating English prompts for {name}")
                prompts_en_with_completion = [
                    (f"Who is {name}?", info["position"]),
                    (f"Can you tell me more about {name}?", info["biography"]),
                    (f"Tell me about {name}?", info["biography"]),
                    (f"Do you know who is {name}?", info["biography"]),
                    (f"What is the specialization of {name}?", info["specialization"]),
                    (f"What is the Major of {name}?", info["specialization"]),
                    (f"What does {name} specialize in?", info["specialization"]),
                    (f"What is the position(title, post) of {name}?", info["position"]),
                    (f"What does {name} teach?", info["teaches"]),
                    (f"What modules does {name} teach?", info["teaches"]),
                    (f"What is the profile url of {name}?", "Here " + info["link"]),
                    (f"What is the profile link of {name}?", "Here " + info["link"]),
                    (f"Where can I know more about {name}?", "Here " + info["link"])
                ]
                print(f"Creating Arabic prompts for {name}")
                prompts_ar_with_completion = [(translate_to_arabic(p), translate_to_arabic(c)) for p, c in
                                              prompts_en_with_completion]

                prompts_and_completion.append(prompts_en_with_completion + prompts_ar_with_completion)

        GenericDataHelpers.write_prompts_to_training_data(prompts_and_completion)

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


class MajorDataHelpers:

    @staticmethod
    def create_major_prompts_and_completion_from_csv():

        with open("aou_data/csv/Major.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            prompts_and_completion = []

            majors = {}

            for row in reader:
                majors[row['name']] = row

            for major_name, info in majors.items():
                print(f"Creating English prompts for {major_name}")
                prompts_en_with_completion = [
                    (f"What is {major_name} program?", info['description']),
                    (f"Tell me more about {major_name} program?", info['description']),
                    (f"Can you tell me about the {major_name} program?", info['description']),
                    (f"What am I going to study and learn in the {major_name} program?", info['description']),
                    (f"What is the study plan of {major_name} program?", info['studyPlan']),
                    (f"What faculty offers the {major_name} program?",
                     GenericDataHelpers.get_faculty_name_from_id(info["offeredByFaculty"])),
                    (f"What is the degree level of {major_name} program?", info['degreeLevel']),
                    (f"How many credits are included within the {major_name} program?", info['requiredCredits']),
                    (f"What faculty is {major_name} part of?",
                     GenericDataHelpers.get_faculty_name_from_id(info["offeredByFaculty"]))
                ]
                print(f"Creating Arabic prompts for {major_name}")
                prompts_ar_with_completion = [(translate_to_arabic(p), translate_to_arabic(c)) for p, c in
                                              prompts_en_with_completion]

                prompts_and_completion.append(prompts_en_with_completion + prompts_ar_with_completion)

        GenericDataHelpers.write_prompts_to_training_data(prompts_and_completion)

    @staticmethod
    def write_major_data_to_csv():
        # Function to get user input and translate Arabic fields
        def get_user_input():
            id = input("Enter id: ")
            name = input("Enter name: ")
            name_ar = GoogleTranslator(source='auto', target='ar').translate(text=name)
            required_credit = int(input("Enter required credit: "))
            degree_level = "Undergraduate" if int(
                input("Enter degree level (1-Undergraduate, else-Postgraduate): ")) == 1 else "Postgraduate"
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


class ModulesDataHelpers:

    @staticmethod
    def write_modules_csv_from_scrapped_data(in_file, out_file, faculty):
        # reading existing data from the output file to check if modules to be added already exist
        existing_data = {}
        try:
            with open(out_file, 'r', newline='', encoding='utf-8') as outfile:
                reader = csv.DictReader(outfile)
                for row in reader:
                    existing_data[row["code"]] = row
        except FileNotFoundError:
            # if the file doesn't exist, we'll create it later
            pass

        with open(in_file, 'r', newline='', encoding='utf-8') as infile, \
                open(out_file, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.DictReader(infile)

            fieldnames = ['id', 'name', 'nameArabic', 'code', 'creditsHours', 'description', 'descriptionArabic',
                          'objectives', 'objectivesArabic', 'outcomes', 'outcomesArabic', 'prerequisite',
                          'offeredByFaculty']

            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()

            # keeping track of number of conflicts
            conflictCount = 0

            # to properly order the ids after adding
            # new data
            rowsCount = 0

            for i, row in enumerate(reader):
                rowsCount += 1
                id = f"T{(rowsCount):04d}"
                # checking if modules to be written from in_file are already within out_file
                # writing the common rows
                if row['course_code'] in existing_data.keys():
                    conflictCount += 1
                    targetRow = existing_data[row['course_code']]
                    # updating the ids so we have old and new modules sorted in place by ids
                    targetRow['id'] = id
                    targetRow['offeredByFaculty'] = targetRow['offeredByFaculty'] + f', {faculty}'
                    writer.writerow(targetRow)

                    # removing the common row from the existing data of the outputfile
                    # to write the remaining data
                    del existing_data[row['course_code']]
                else:
                    # writing uncommon rows
                    new_row = {
                        'id': id,
                        'name': row['course_title'],
                        'nameArabic': translate_to_arabic(row['course_title']),
                        'code': row['course_code'],
                        'creditsHours': row['credit_hours'],
                        'description': row['course_desc'],
                        'descriptionArabic': translate_to_arabic(row['course_desc']),
                        'objectives': row['course_objectives'],
                        'objectivesArabic': translate_to_arabic(row['course_objectives']),
                        'outcomes': row['course_outcomes'],
                        'outcomesArabic': translate_to_arabic(row['course_outcomes']),
                        'prerequisite': row['pre-requisite'],
                        # change according to the faculty
                        'offeredByFaculty': faculty
                    }
                    writer.writerow(new_row)
                print(f"Wrote {row['course_code']} module")

            print("Done writing new data and solving conflicts")
            print("writing existing data")

            # writing the remaining rows from existing data
            for i, row in enumerate(existing_data.values()):
                row["id"] = f"T{(i + rowsCount + 1):04d}"
                writer.writerow(row)
                print(f"Wrote {row['code']} module")

            print("Done writing to file")
            print(f"Solved {conflictCount} conflicted rows")

    @staticmethod
    def create_modules_prompts_and_completion_from_csv():
        with open("aou_data/csv/Module.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            prompts_and_completion = []

            modules = {}

            for row in reader:
                modules[row['name']] = row

            for module_name, info in modules.items():
                print(f"Creating English prompts for {module_name}")
                prompts_en_with_completion = [
                    (f"What is {module_name} module?", info["description"]),
                    (f"What is {info['code']} module?", info["description"]),
                    (f"Can you tell me about {module_name}?", info["description"]),
                    (f"Can you tell me about {info['code']}?", info["description"]),
                    (f"What am I going to learn in {module_name} course?", info["description"]),
                    (f"What am I going to learn in {info['code']} course?", info["description"]),
                    (f"What is the {module_name} course name in Arabic?", info["nameArabic"]),
                    (f"What is the {info['code']} course name in Arabic?", info["nameArabic"]),
                    (f"What is the benefit of studying {module_name}?", info["objectives"]),
                    (f"What is the benefit of studying {info['code']}?", info["objectives"]),
                    (f"What is the benefit of studying {module_name}?", info["outcomes"]),
                    (f"What is the benefit of studying {info['code']}?", info["outcomes"]),
                    (f"What am I going to learn in {module_name}? module", info["objectives"]),
                    (f"What am I going to learn in {info['code']}? module", info["objectives"]),
                    (f"What am I going to learn in {module_name}? module", info["outcomes"]),
                    (f"What am I going to learn in {info['code']}? module", info["outcomes"]),
                    (f"What are the outcomes I am going to get after taking {module_name}? course", info["outcomes"]),
                    (f"What are the outcomes I am going to get after taking {info['code']}? course", info["outcomes"]),
                    (f"What is the objective of taking the {module_name}? course", info["objectives"]),
                    (f"What are the objectives of taking the {module_name}? course", info["objectives"]),
                    (f"What is the objective of taking the {info['code']}? course", info["objectives"]),
                    (f"What are the objectives of taking the {info['code']}? course", info["objectives"]),
                    (f"What is the module code of {module_name}?", info["code"]),
                    (f"What is the code of {module_name}?", info["code"]),
                    (f"What is the id of {module_name}?", info["code"]),
                    (f"What is {info['code']} module?", info["name"]),
                    (f"What is {info['code']}?", info["name"]),
                    (f"How many credits does the {info['code']}? have", info["creditsHours"]),
                    (f"How many hours does the {info['code']}? have", info["creditsHours"]),
                    (f"How many hours does the {info['name']}? have", info["creditsHours"]),
                    (f"How many credits does the {info['name']}? have", info["creditsHours"]),
                    (f"By which faculty is {info['name']} offered by?",
                     GenericDataHelpers.get_faculty_name_from_id(info["offeredByFaculty"])),
                    (f"By which faculty is {info['code']} offered by?",
                     GenericDataHelpers.get_faculty_name_from_id(info["offeredByFaculty"])),
                    (f"What is the name of the faculty that {info['name']} is offered by?",
                     GenericDataHelpers.get_faculty_name_from_id(info["offeredByFaculty"])),
                    (f"What are the prerequisite of the {info['name']}?", info["prerequisite"]),
                    (f"What are the prerequisite of the {info['code']}?", info["prerequisite"]),
                ]
                print(f"Creating Arabic prompts for {module_name}")
                prompts_ar_with_completion = [(translate_to_arabic(p), translate_to_arabic(c)) for p, c in
                                              prompts_en_with_completion]

                prompts_and_completion.append(prompts_en_with_completion + prompts_ar_with_completion)
        GenericDataHelpers.write_prompts_to_training_data(prompts_and_completion)


class RequirementDataHelpers:
    @staticmethod
    def write_requirement_data_to_csv():
        file = "aou_data/csv/Requirement.csv"
        field_names = ['id', 'requiredFor', 'requiredForArabic', 'requirement', 'requirementArabic']

        with open(file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=field_names)

            writer.writeheader()

            i = 1
            while True:
                requiredFor = input("Enter required for (-1 to stop): ")
                requirement = input("Enter requirement (-1 to stop): ")

                if any([requiredFor, requiredFor]) == "-1":
                    break

                item = {
                    "id": f"T{(i):02d}",
                    "requiredFor": requiredFor,
                    "requiredForArabic": translate_to_arabic(requiredFor),
                    "requirement": requirement,
                    "requirementArabic": translate_to_arabic(requirement),
                }
                i += 1
                writer.writerow(item)

    @staticmethod
    def create_requirement_prompts_and_completion_from_csv():
        with open("aou_data/csv/Requirement.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            prompts_and_completion = []

            requirements = {}

            for row in reader:
                requirements[row['requiredFor']] = row

            for name, info in requirements.items():
                print(f"Creating English prompts for {name}")

                prompts_en_with_completion = [
                    (f"What are the requirements for {name} program?", info['requirement']),
                    (f"What are the requirements for {name}?", info['requirement']),
                    (f"What do I need to specialize in {name}?", info['requirement']),
                    (f"What do I need to specialize in {name} at AOU?", info['requirement']),
                    (f"What do I need to specialize in {name} at Arab Open University?", info['requirement']),
                    (f"What do I need to specialize in {name} at the university?", info['requirement']),
                    (f"For {name} major, what do I need to qualify for it", info['requirement']),
                    (
                    f"I will choose {name} as my major in Arab Open University (AOU), what requirements should I fulfill?",
                    info['requirement']),
                    (f"Anything I should know before apply for {name} major? ", info['requirement']),
                ]

                print(f"Creating Arabic prompts for {name}")
                prompts_ar_with_completion = [(translate_to_arabic(p), translate_to_arabic(c)) for p, c in
                                              prompts_en_with_completion]

                prompts_and_completion.append(prompts_en_with_completion + prompts_ar_with_completion)
            GenericDataHelpers.write_prompts_to_training_data(prompts_and_completion)


class FeeDataHelpers:

    @staticmethod
    def write_fee_data_to_csv(file, field_names):
        with open(file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=field_names)

            writer.writeheader()

            while True:
                value = input(f"Enter {field_names[0]}: ")
                value_translated = translate_to_arabic(value)
                amount = float(input("Enter amount: "))

                row = {
                    field_names[0]: value,
                    field_names[1]: value_translated,
                    field_names[2]: amount
                }

                writer.writerow(row)

                # no need for break statement I will just terminate




    @staticmethod
    def create_fee_prompts_and_completion_from_csv():
        prompts_en_with_completion = [
            ("What are the nonrefundable fees?", "The nonrefundable fees are the fees that you pay when you are enrolling to the university, these fees include\nApplication of Admission - 19.3 R.O\nPlacement Test (Arabic) which is optional 5.8 R.O\nPlacement Test (English) which is also optional - 5.8 R.O\nPlacement Test (Math) which is also optional - 5.8 R.O\nPlacement Test (IT) which is also optional - 5.8 R.O\nRegistration Fees of new student - 27 R.O\nWith a total of 69.500 Omani rials"),
            ("What are the fees required for enrollment at the university?","The fees that are required for enrolling to the university are:\nApplication of Admission - 19.3 R.O\nPlacement Test (Arabic) which is optional 5.8 R.O\nPlacement Test (English) which is also optional - 5.8 R.O\nPlacement Test (Math) which is also optional - 5.8 R.O\nPlacement Test (IT) which is also optional - 5.8 R.O\nRegistration Fees of new student - 27 R.O\nWith a total of 69.500 Omani rials"),
            ("What are the fees required for enrollment at AOU?","The fees that are required for enrolling to the university are:\nApplication of Admission - 19.3 R.O\nPlacement Test (Arabic) which is optional 5.8 R.O\nPlacement Test (English) which is also optional - 5.8 R.O\nPlacement Test (Math) which is also optional - 5.8 R.O\nPlacement Test (IT) which is also optional - 5.8 R.O\nRegistration Fees of new student - 27 R.O\nWith a total of 69.500 Omani rials"),
            ("What are the fees required for enrollment at Arab Open University?","The fees that are required for enrolling to the university are:\nApplication of Admission - 19.3 R.O\nPlacement Test (Arabic) which is optional 5.8 R.O\nPlacement Test (English) which is also optional - 5.8 R.O\nPlacement Test (Math) which is also optional - 5.8 R.O\nPlacement Test (IT) which is also optional - 5.8 R.O\nRegistration Fees of new student - 27 R.O\nWith a total of 69.500 Omani rials"),
            ("What is the total cost of enrolling at the university?", "The total cost is 69.500 R.O"),
            ("What is the total cost of enrolling at the AOU?", "The total cost is 69.500 Oman rials"),
            ("What is the total fees of enrolling at the Arab Open University?", "The total fees are 69.500 Oman rials"),
            (f"What is the cost for Application of Admission?", f"It is 19.3 R.O"),
            (f"What is the cost for Placement Test (Arabic)", f"It is 5.8 R.O"),
            (f"What is the cost for Placement Test (English)", f"It is 5.8 R.O"),
            (f"What is the cost for Placement Test (Math)", f"It is 5.8 R.O"),
            (f"What is the cost for Placement Test (IT)", f"It is 5.8 R.O"),
            (f"What is the cost for Registration Fees of new student", f"It is 27 R.O"),
            ("How much is the foundation program?", f"for Full Time Learning it is 2289 R.O while for Opening learning it costs 2040 R.O"),
            (f"I am a full time student, how much would I pay for the foundation program?", f"for full time, you'll pay 2289 R.O"),
            (f"I am a opening learning student, how much would I pay for the foundation program?", f"for full time, you'll pay 2040 R.O"),
            (f"What is the difference between foundation program as a full time student an as open learning student?", f"The fees for the foundation program for full time learning students are expensive more than the open learning by 240 R.O"),
            (f"What are the fees for Diploma Information Technology & Computing for an Opening learning student?", f"it is 2590 R.O"),
            (f"What are the fees for Diploma in Business Study for an Opening learning student?", f"it is 2715 R.O"),
            (f"What are the fees for BA Hons in Business Studies for an Opening learning student?", f"it is 5600 R.O"),
            (f"What are the fees for BA Hons in Bachelor in Law for an Opening learning student?", f"it is 7100 R.O"),
            (f"What are the fees for BA Hons in Bachelor in Law for a full time learning student?", f"it is 9400 R.O"),
            (f"What are the fees for BSc Hons in Information Technology and Computing for a full time learning student?", f"it is 9610 R.O"),
            (f"What are the fees for BSc Hons in Information Technology and Computing for an Opening learning student?", f"it is 5750 R.O"),
            (f"What are the fees for BA Hons in Business Studies for a full time learning student?", f"it is 9450 R.O"),
            (f"What are the fees for Diploma in Business Study for a full time student?", f"it is 4380 R.O"),
            (f"What are the fees for Diploma Information Technology & Computing for a full time learning student?", f"it is 4177 R.O"),
            (f"How much I am going to pay if I am choosing Diploma Information Technology & Computing while I am an open learning student?",f"You'll pay 2590 R.O"),
            (f"How much I am going to pay if I am choosing Diploma in Business Study while I am an open learning student?",f"You'll pay 2715 R.O"),
            (f"How much I am going to pay if I am choosing BA Hons in Business Studies while I am an open learning student?",f"You'll pay 5600 R.O"),
            (f"How much I am going to pay if I am choosing BSc Hons in Information Technology and Computing while I am an open learning student?",f"You'll pay 5750 R.O"),
            (f"How much I am going to pay if I am choosing Bachelor in Law while I am an open learning student?",f"You'll pay 7100 R.O"),
            (f"How much I am going to pay if I am choosing Bachelor in Law while I am a full time student?",f"You'll pay 9400 R.O"),
            (f"How much I am going to pay if I am choosing BSc Hons in Information Technology and Computing while I am a full time student?",f"You'll pay 9610 R.O"),
            (f"How much I am going to pay if I am choosing BA Hons in Business Studies while I am a full time student?",f"You'll pay 9450 R.O"),
            (f"How much I am going to pay if I am choosing Diploma in Business Study while I am a full time student?",f"You'll pay 4380 R.O"),
            (f"How much I am going to pay if I am choosing Diploma Information Technology & Computing while I am a full time student?",f"You'll pay 4177 R.O"),
            (f"What is the difference between Open Learning and Full time learning for the fees?",f"Full time is extra expensive compared to Open Learning programs, you have to be eligible to study as full time student, some criteria may be imposed by the university depending on your chosen major"),
            ("What is the difference between open learning and full time learning?", "Open learning, often referred to as distance or online learning, allows students to study at their own pace and from any location, offering flexibility and accessibility. This mode of learning typically involves online lectures, self-study modules, and virtual exams. In contrast, full-time learning requires students to attend scheduled classes in person, usually on a campus, and follow a more structured timetable. Full-time learning provides a traditional classroom experience with direct interaction with instructors and peers, which can enhance engagement and immediate feedback.")
        ]
        print(f"Creating Arabic prompts")
        prompts_ar_with_completion = [(translate_to_arabic(p), translate_to_arabic(c)) for p, c in
                                      prompts_en_with_completion]

        prompts_and_completion = prompts_en_with_completion + prompts_ar_with_completion

        with open("training_data/aou_training_dataset.json", mode='r', encoding="utf8") as f:
            data = json.load(f)

            print("Adding prompts to training data")
            for pc in prompts_and_completion:
                data.append(
                    {
                        "prompt": pc[0],
                        "completion": pc[1]
                    }
                )
        with open("training_data/aou_training_dataset.json", mode='w', encoding='utf8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

class GenericDataHelpers:

    @staticmethod
    def write_faq_to_csv():
        i = 1
        with open("aou_data/csv/FAQ.csv", 'w', newline='', encoding='utf-8') as f:
            field_names = ["id", "question", "questionArabic", "answer", "answerArabic"]
            writer = csv.DictWriter(f, fieldnames=field_names)
            writer.writeheader()
            while True:
                q = input("Enter question: ")
                q_ar = translate_to_arabic(q)
                a = input("Enter answer: ")
                a_ar = translate_to_arabic(a)

                row = {
                    "id": f"T{(i):01d}",
                    field_names[1]: q,
                    field_names[2]: q_ar,
                    field_names[3]: a,
                    field_names[4]: a_ar,
                }

                writer.writerow(row)
                i += 1

    @staticmethod
    def create_prompts_and_completion_from_input_with_translations():
        prompts_en_with_completion = []

        count = int(input("How many prompts and completion pairs? "))

        for i in range(count):
            q = input("Enter prompt: ")
            a = input("Enter completion: ")
            prompts_en_with_completion.append((q, a))

        prompts_ar_with_completion = [(translate_to_arabic(p), translate_to_arabic(c)) for p, c in prompts_en_with_completion]

        prompts_with_completion = prompts_en_with_completion + prompts_ar_with_completion

        with open("training_data/aou_training_dataset.json", mode='r', encoding="utf8") as f:
            data = json.load(f)

            for p,c in prompts_with_completion:
                pc = {
                    "prompt": p,
                    "completion": c
                }
                data.append(pc)

        print("Adding prompts to training data")
        with open("training_data/aou_training_dataset.json", mode='w', encoding='utf8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print(f"Created total {count*2} prompts with {count} English and {count} Arabic translated pairs")
    @staticmethod
    def create_faq_prompts_and_completion_from_csv():
        with open("aou_data/csv/FAQ.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            with open("training_data/aou_training_dataset.json", mode='r', encoding="utf8") as f:
                data = json.load(f)

                for row in reader:
                    question_ar, answer_ar = translate_to_arabic(row['question']), translate_to_arabic(row['answer'])
                    pc_en = {
                        "prompt": row['question'],
                        "completion": row['answer']
                    }
                    pc_ar = {
                        "prompt": question_ar,
                        "completion": answer_ar
                    }
                    data.append(pc_en)
                    data.append(pc_ar)

                print("Adding prompts to training data")
            with open("training_data/aou_training_dataset.json", mode='w', encoding='utf8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)


    @staticmethod
    def write_prompts_to_training_data(prompts_and_completion):
        with open("training_data/aou_training_dataset.json", mode='r', encoding="utf8") as f:
            data = json.load(f)

            print("Adding prompts to training data")
            for tutor_pc in prompts_and_completion:
                for pc in tutor_pc:
                    data.append(
                        {
                            "prompt": pc[0],
                            "completion": pc[1]
                        }
                    )
        with open("training_data/aou_training_dataset.json", mode='w', encoding='utf8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def get_faculty_name_from_id(faculty_id):
        with open("aou_data/csv/Faculty.csv", "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row[id_column_name] == faculty_id:
                    return row['name']


class PassedTutorHelpers:
    @staticmethod
    def write_passed_tutor_data_to_csv():
        field_names = ["id", "name", "nameArabic", "email", "moduleTaught", "major"]

        openingMode = input("writing(w) or appending(a)?")

        with open("aou_data/csv/PassedTutor.csv", openingMode, newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=field_names)

            if openingMode == 'w':
                writer.writeheader()

            # change it for the latest id in the file
            i = 1
            while True:
                name = input("Enter passed tutor name: ")
                name_ar = translate_to_arabic(name)
                email = input("Enter passed tutor email: ")
                modules_taught = input("Enter passed tutor taught modules codes (separated by commas): ")
                major = input("Enter passed tutor major id: ")

                row = {
                    field_names[0]: f"T{(i):02d}",
                    field_names[1]: name,
                    field_names[2]: name_ar,
                    field_names[3]: email,
                    field_names[4]: modules_taught,
                    field_names[5]: major
                }

                writer.writerow(row)
                i += 1


if __name__ == '__main__':
    GenericDataHelpers.create_prompts_and_completion_from_input_with_translations()
