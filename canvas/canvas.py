from dotenv import load_dotenv
import os
import requests

load_dotenv()
canvas_token = os.getenv("TOKEN")
school_path = os.getenv("SCHOOL_PATH")

courses_url = school_path + "api/v1/courses"
auth_header = "Bearer " + canvas_token
headers = {
    'Authorization': auth_header
}

response = requests.get(courses_url, headers=headers)

print(response.status_code)
print(response.json())
