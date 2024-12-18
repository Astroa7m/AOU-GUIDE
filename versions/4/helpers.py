def convert_dict_to_formatted_string(the_dict):
    the_string = ""
    for key, value in the_dict.items():

        # print(type(value))
        if isinstance(value, type(dict)):
            the_string += str(key) + ":\n"
            the_string += convert_dict_to_formatted_string(value)

        else:
            the_string += str(key) + ": " + str(value) + "\n"

    return the_string


dict = {

        "id": 200304,
        "title": "",
        "name": "Ahmed Samir",
        "password": "200304",
        "GPA": 3.87,
        "academic_performance": {
          "M110 - Python Programming": {
            "midterm": "20/30",
            "tutor_marked_assessment(TMA)": "15/15",
            "attendance": "5/5",
            "final": "45/50",
            "total_mark": "85/100",
            "grade": "B"
          },
          "TM105 - Java Programming": {
            "midterm": "27/30",
            "tutor_marked_assessment(TMA)": "15/15",
            "attendance": "4.75/5",
            "final": "46.25/50",
            "total_mark": "93/100",
            "grade": "A"
          },
          "TM354 - Software Engineering": {
            "midterm": "26.5/30",
            "tutor_marked_assessment(TMA)": "13.25/15",
            "attendance": "4/5",
            "final": "48/50",
            "total_mark": "91.75/100",
            "grade": "A"
          },
          "AR113 - Arabic Communication Skills": {
            "midterm": "22/30",
            "tutor_marked_assessment(TMA)": "11/15",
            "attendance": "5/5",
            "final": "39/50",
            "total_mark": "77/100",
            "grade": "C"
          }
        }
      }
print(convert_dict_to_formatted_string(dict))