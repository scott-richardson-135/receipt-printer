from printer.actions import print_custom_message
from canvas.courses import get_active_courses
from canvas.assignments import get_assignments, due_within_7_days

if __name__ == "__main__":
    #print_custom_message("Sometimes I wish I was gurt\n")

    courses = get_active_courses()
    
    for course in courses:
        name = course.get("name")
        course_id = course.get("id")
        if name:
            print(name)

        assignments = get_assignments(course_id)
        filtered_assignments = due_within_7_days(assignments)
        for assignment in filtered_assignments:
            assignment_name = assignment.get("name")
            if assignment_name:
                print(assignment_name)

