import json

def add_student(student_id, name, age, grade):
    """
    Addingg a new student to the records.

    Parameters:
    student_id (int): The ID of the student.
    name (str): The name of the student.
    age (int): The age of the student.
    grade (str): The grade of the student.

    Returns:
    dict: The student record added.
    """
    student = {
        "student_id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }
    with open("student_records.json", "a+") as file:
        json.dump(student, file)
        file.write("\n")
    return student

def search_student(identifier):
    """
    Search for a student by student ID or name.

    Parameters:
    identifier (int / str): The student ID or name to search for.

    Returns:
    dict: The student record found, or None if not found.
    """
    with open("student_records.json", "r") as file:
        for line in file:
            student = json.loads(line)
            if str(student["student_id"]) == str(identifier) or student["name"] == identifier:
                return {"age": student["age"], "grade": student["grade"]}
    return None

def update_student(identifier, key, value):
    """
    Update a student's information by student ID or name.

    Parameters:
    identifier (int/str): The student ID or name to search for.
    key (str): The field to update (age or grade).
    value (int/str): The new value for the field.

    Returns:
    str: Confirmation message.
    """
    records = []
    updated = False
    with open("student_records.json", "r") as file:
        for line in file:
            student = json.loads(line)
            if str(student["student_id"]) == str(identifier) or student["name"] == identifier:
                student[key] = value
                updated = True
            records.append(student)
    if updated:
        with open("student_records.json", "w") as file:
            for student in records:
                json.dump(student, file)
                file.write("\n")
        return "Student information updated successfuly."
    else:
        return "Student not found."


