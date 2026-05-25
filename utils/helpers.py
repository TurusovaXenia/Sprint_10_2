import os
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_email():
    random_email = generate_random_string(7) + '@gmail.com'
    return random_email


def generate_new_user_data():
    email = generate_random_email()
    password = generate_random_string(10)

    payload = {
        "email": email,
        "password": password
    }
    return payload


def get_upload_file_path(filename):
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(current_dir, "tests", "resources", filename)


def get_cleaned_response(res_json, payload):
    return {
        key: str(res_json[key])
        for key in payload
        if key in res_json
    }
