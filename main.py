from printer.actions import print_custom_message, print_as_receipt
from canvas.courses import get_active_courses
from canvas.assignments import get_assignments, due_within_7_days
from printer.printed_tracker import load_printed, save_printed_ids

if __name__ == "__main__":

    courses = get_active_courses()
    printed_ids = load_printed()

    
    for course in courses:
        name = course.get("name")
        course_id = course.get("id")

        assignments = get_assignments(course_id)
        filtered_assignments = due_within_7_days(assignments)


        for assignment in filtered_assignments:
            aid = assignment.get("id")
            if aid not in printed_ids:
                print_as_receipt(assignment, name)
                printed_ids.add(aid)


    save_printed_ids(printed_ids)

