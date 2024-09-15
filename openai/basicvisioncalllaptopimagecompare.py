import base64

from openai import OpenAI

client= ""

def encode_image(image_path):
    with open(image_path,"rb") as file_path:
        return base64.b64encode(file_path.read()).decode('utf-8')

image_path = "/Users/abhidesktop/Documents/Python/SampleProjects/openai/IMG_6729.JPG"
image_file=encode_image(image_path)


response= client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":"What are in these images? Is there any difference between them?"
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/jpeg;base64,{image_file}"
                    }
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/jpeg;base64,{image_file}"
                    }
                }
            ]
        }
    ],
    max_tokens=100
)

print(response.choices[0].message.content)