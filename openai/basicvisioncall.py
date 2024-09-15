from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam,ChatCompletionSystemMessageParam,ChatCompletionAssistantMessageParam,ChatCompletionToolMessageParam,ChatCompletionFunctionMessageParam




client = OpenAI(api_key="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")

response= client.chat.completions.create(
    model="gpt-4o-mini",
    messages= [
                {
                    "role":"user",
                    "content":[
                                   {
                                       "type":"text",
                                       "text":"Whats in the image?"
                                   },
                                   {
                                       "type":"image_url",
                                       "image_url":
                                                  {
                                                   "url":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                                                  },
                                   },
                               ],
                }
            ],
    max_tokens=300,
)

print(response.choices[0].message)