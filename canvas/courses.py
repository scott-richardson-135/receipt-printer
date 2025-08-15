from .api import canvas_get

def get_active_courses():
    return canvas_get("courses", "enrollment_state=active")