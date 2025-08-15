from printer.actions import print_custom_message
from canvas.courses import get_active_courses

if __name__ == "__main__":
    #print_custom_message("Sometimes I wish I was gurt\n")

    courses = get_active_courses()
    
    for course in courses:
        name = course.get("name")
        if name:
            print_custom_message(name)
