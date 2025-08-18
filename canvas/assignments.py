from .api import canvas_get
from datetime import datetime, timedelta, timezone

def get_assignments(course_id):
    return canvas_get(f"courses/{course_id}/assignments")


# takes in a list of all assignments and returns a list of assignments due within a week
def due_within_7_days(assignments):
    now = datetime.now(timezone.utc)
    upcoming_assignments = []

    for assignment in assignments:
        due_at = assignment.get("due_at")
        if due_at:
            #convert from the format that canvas sends it in to the one that timedelta wants
            due = datetime.fromisoformat(due_at.replace("Z", "+00:00"))

            if now <= due <= now + timedelta(days=7):
                upcoming_assignments.append(assignment) 

    return upcoming_assignments

