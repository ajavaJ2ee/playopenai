import base64

from openai import OpenAI

client= OpenAI(api_key="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")

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