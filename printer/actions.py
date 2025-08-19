from .connection import getPrinter
from datetime import datetime, timezone
import pytz

def print_custom_message(message):
    printer = getPrinter()
    printer.set(align="center")
    printer.text(message)
    printer.cut()
    printer.close()


def print_as_receipt(assignment, course_name):
    title = assignment.get("name", "Untitled")
    due = assignment.get("due_at", "No due date")
    if due:
        due = format_due_date(due)
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

def format_due_date(due_at):
    due = datetime.fromisoformat(due_at.replace("Z", "+00:00"))

    mt_time = pytz.timezone("US/Mountain")
    due_mt = due.astimezone(mt_time)

    #format
    return due_mt.strftime("%a, %b %d %Y %I:%M %p")