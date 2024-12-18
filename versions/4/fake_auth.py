import json

import json

def load_data():
    with open("versions/4/fake_api_data.json", 'r') as f:
        return json.load(f)

def authenticate_user(user_id, password):
    data = load_data()

    # check students
    for student in data["students"]:
        if str(student["info"]["id"]) == user_id.strip() and str(student["info"]["password"]) == password.strip():
            return student["info"]

    # check tutors
    for tutor in data["tutors"]:
        if str(tutor["special_tutor_id"]) == user_id.strip() and str(tutor["password"]) == password.strip():
            return tutor

    return None

