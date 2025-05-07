import requests
import os
import sys

PHOTOS_DIRECTORY = r"C:\Users\felix\OneDrive - Dawson College\Pictures\miniDawsHacks.25"
MODEL_NAME = "llava"

def grade_photo(image_path, model_name):
    prompt = f"""grade this photo at path: {image_path}. Grade based on photo quality, coloring, subjects, etc... This photo was taken a the DawsHacks event you attended. We are trying to find the best photos, by asking you to grade them, for our website. PLEASE ONLY output a percentage grade, nothing else in your output. Your output should look like this: \"XX.X%\" where the Xs are the grade you rate this photo based on your background in photography."""
    
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.6,
        "top_p": 1.0,
        "top_k": 40,
        "repetition_penalty": 1.0,
    }
    
    response = requests.post(url, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        
        if "response" in result:
            grade = result["response"].strip()
        elif "text" in result:
            grade = result["text"].strip()
        else:
            print("Warning: Unexpected response format")
            print(result)
            return None
        
        return grade
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
        return None

def append_to_file(image_path, grade):
    filename = os.path.basename(image_path)
    with open("photo_grades.txt", "a") as file:
        file.write(f"{filename}: {grade}\n")

def is_image_file(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']
    file_ext = os.path.splitext(filename)[1].lower()
    return file_ext in image_extensions

if not os.path.isdir(PHOTOS_DIRECTORY):
    print(f"Error: Directory '{PHOTOS_DIRECTORY}' not found")
    sys.exit(1)

for filename in os.listdir(PHOTOS_DIRECTORY):
    if is_image_file(filename):
        image_path = os.path.join(PHOTOS_DIRECTORY, filename)
        print(f"Processing: {filename}")
        
        grade = grade_photo(image_path, MODEL_NAME)
        
        if grade:
            append_to_file(image_path, grade)
            print(f"Photo graded: {filename} - {grade}")
        else:
            print(f"Failed to grade: {filename}")