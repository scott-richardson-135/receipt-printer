from printer.actions import print_custom_message, print_as_receipt
from canvas.courses import get_active_courses
from canvas.assignments import get_assignments, due_within_7_days

if __name__ == "__main__":

    courses = get_active_courses()
    
    for course in courses:
        name = course.get("name")
        course_id = course.get("id")
        if name:
            print(name)
        print(course_id)
        assignments = get_assignments(course_id)
        filtered_assignments = due_within_7_days(assignments)


        for assignment in assignments[:2]:
            print_as_receipt(assignment, name)

