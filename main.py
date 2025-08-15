from printer.actions import print_custom_message
from canvas.courses import get_active_courses
from canvas.assignments import get_assignments

if __name__ == "__main__":
    #print_custom_message("Sometimes I wish I was gurt\n")

    courses = get_active_courses()
    
    for course in courses:
        name = course.get("name")
        course_id = course.get("id")
        if name:
            print(name)

        course_id = course.get("id")
        assignments = get_assignments(course_id)
        for assignment in assignments:
            assignment_name = assignment.get("name")
            if assignment_name:
                print(assignment_name)

