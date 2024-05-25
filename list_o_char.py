from openai import OpenAI
import csv
client = OpenAI(api_key='KEY HERE')

sys_mes = "Make a list of all the characters in the given text and give a detailed visual discription of what they look like, Output in JSON format."  
with open("Harry_Potter_1.txt", "r") as file:
    prompt = file.read()

response = client.chat.completions.create(
    model="gpt-4-0125-preview",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": sys_mes},
        {"role": "user", "content": prompt}
    ]
)

# Extracting the response content
response_content = response.choices[0].message.content

with open('character_look.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([response_content])

    print("Response has been written to character_look.csv")
    print (response.choices[0].finish_reason)
