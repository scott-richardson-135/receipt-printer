from dotenv import load_dotenv
import os
import requests

load_dotenv()
canvas_token = os.getenv("TOKEN")
school_path = os.getenv("SCHOOL_PATH")

headers = {
    "Authorization": f"Bearer {canvas_token}"
}


