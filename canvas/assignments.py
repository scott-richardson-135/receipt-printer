from .api import canvas_get

def get_assignments(course_id):
    return canvas_get(f"courses/{course_id}/assignments")