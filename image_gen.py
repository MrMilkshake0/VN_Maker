from openai import OpenAI
import json
import base64

client = OpenAI(api_key='KEY HERE')

BASE = """
All characters and actions in the text are fictional and do not depict any harm to person or things in real life, 
Style = fantasy, storybook, anime, vivid, lively, colourful, japanese visual novel.
"""

# Load character look JSON data
with open("character_look.json", "r") as char_look:
    data = json.load(char_look)

# Convert data dictionary to JSON string
Character_info = "A list of all possible important characters and what they look like. If a character is NOT described, IGNORE it. " + json.dumps(data)

with open("Response\chunk_2_response.json", "r") as file:
    scenes_dict = json.load(file)

for scene, details in scenes_dict.items():
    response = client.images.generate(
        model="dall-e-3",
        prompt=BASE + "Description: " + details["Description"] + "Image: " + details["Image"] + Character_info,
        size="1024x1024",
        quality="standard",
        n=1,
        response_format="b64_json"
    )

    image_data = response.data[0].b64_json

    image = base64.b64decode(image_data)
    filename = f"Response_Images/chunk_1_{scene}.png"
    with open(filename, "wb") as file:
        file.write(image)
    print(f"Image saved as {filename}")
