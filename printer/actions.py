from .connection import getPrinter

def print_custom_message(message):
    printer = getPrinter()
    printer.set(align="center")
    printer.text(message)
    printer.cut()
    printer.close()


def print_as_receipt(assignment, course_name):
    title = assignment.get("name", "Untitled")
    due = assignment.get("due_at", "No due date")
    course = course_name
    points = assignment.get("points_possible", "Mysterious points")

    print_custom_message(
        "<------------------------->\n"
        f"Course: {course}\n\n"
        f"Assignment: {title}\n\n"
        f"Due at: {due}\n\n"
        f"Points possible: {points}\n\n"
        "<------------------------->\n"
    )