from printer.actions import print_custom_message
from canvas.api import canvas_get

if __name__ == "__main__":
    #print_custom_message("Sometimes I wish I was gurt\n")

    courses = canvas_get("courses", "enrollment_state=active")
    
    for course in courses:
        name = course.get("name")
        if name:
            print(name)
