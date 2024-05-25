from openai import OpenAI
import json
import os

system_message = """
Output in json format. You are a system that takes an input of a large text and split it into picture scenes. You will do until the text is fully processed. There can and will be up to 50 scenes in the text. You must make a scene for every relatively small event in the text.

Example of json output:
{
    "Scene 1": {
        "Description": "Uncle Vernon holding a rifle, shouting to warn the intruders. A giant of a man appearing in the doorway, towering over the Dursleys. Hagrid squeezing his way into the hut, fixing the door effortlessly. Hagrid greeting Dudley and presenting Harry with a birthday cake.",
        "Image": "Tense moment in the hut as Uncle Vernon brandishes a rifle and a giant man breaks in. Hagrid's imposing presence and friendly demeanor towards Harry."
    },
    "Scene 2": {
        "Description": "Hagrid explaining Hogwarts and magic to Harry, revealing Harry's wizarding heritage. Hagrid attempting to make tea in the hut, creating a warm and cozy atmosphere. Hagrid sharing the story of Harry's parents and hinting at dark magic related to Voldemort.",
        "Image": "Magical revelations in the hut as Hagrid introduces Harry to the world of wizards and Hogwarts. Cozy setting with the smell of sausages sizzling on the fire."
    },
    "Scene 3": {
        "Description": "Hagrid showing Harry the Hogwarts acceptance letter. Hagrid sending a message to Dumbledore with an owl. Uncle Vernon's resistance to Harry attending Hogwarts and Hagrid's magical intervention resulting in Dudley's tail.",
        "Image": "Excitement and tension as Hagrid reveals the Hogwarts letter and sends a message with the owl. Magical mishap as Dudley sprouts a pig's tail."
    },
    ...
}
"""

def sceneaify(prompt, output_file):
    client = OpenAI(api_key="KEY HERE")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    response_content = response.choices[0].message.content
    
    response_dict = json.loads(response_content)
    # Writing the response to a JSON file with proper formatting
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(response_dict, json_file, indent=4)

    print(f"Response has been written to {output_file}")
    print(response.choices[0].finish_reason)

# Directory containing the chunks
directory = "Chunks"

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):  # Ensure it's a text file
        filepath = os.path.join(directory, filename)
        output_file = f"Response/{os.path.splitext(filename)[0]}_response.json"
        with open(filepath, "r") as text_chunk:
            prompt = text_chunk.read()
            sceneaify(prompt, output_file)
