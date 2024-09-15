import base64
import requests

api_key=""

def encode_image(image_path):
    with open(image_path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

image_path= "/openai/sampleAPIcalls/IMG_6729.JPG"
base64_image=encode_image(image_path)

headers={
    "Content_Type":"application/json",
    "Authorization":f"Bearer {api_key}"
}


payload={
    "model":"gpt-4o-mini",
    "messages":[
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":"Whats in the image?"
                },
                {
                    "type":"image_url",
                    "image_url":{
                        "url":f"data:image/jpeg;base64,{base64_image}",
                        "detail":"low"
                     }
                }
            ]
        }
    ],
    "max_tokens":300
}

response= requests.post("https://api.openai.com/v1/chat/completions",headers=headers,json=payload)

#print(response)
print(response.json())

# Chat Compeltion Object with high
"""{'id': 'chatcmpl-A7m8P4W9UlvG5HEIxBUsO5o8JZijy',
 'object': 'chat.completion', 
 'created': 1726416689, 
 'model': 'gpt-4o-mini-2024-07-18',
  'choices': [{
            'index': 0,
             'message': {
                    'role': 'assistant', 
                    'content': 'The image shows a computer screen displaying a segment of Python code in a text editor. The code appears to define functions related to handling exceptions and making API requests. Key elements include:\n\n1. **Function Definitions**: There are functions for handling exceptions (`exception_handler`), getting assessment responses (`get_elevate_assessment_response`), and validating responses (`validate_response`).\n\n2. **Environment Variables**: The code retrieves configuration values from environment variables.\n\n3. **Requests Library**: It uses the `requests` library to manage HTTP session and requests.\n\n4. **Error Handling**: There are mechanisms for catching and raising exceptions.\n\n5. **Comments**: Some lines may include comments explaining parts of the code.\n\nIf you need any specific information or assistance with this code, feel free to ask!',
                     'refusal': None
                     }, 
                     'logprobs': None, 'finish_reason': 'stop'
                     }
             ], 
  'usage': {
        'prompt_tokens': 25513,
        'completion_tokens': 162, 
        'total_tokens': 25675, 
        'completion_tokens_details': {
                                    'reasoning_tokens': 0
                                    }
        },
  'system_fingerprint': 'fp_54e2f484be'}"""

# Chat Completion object with low
{'id': 'chatcmpl-A7mFroCtCYUZtY9S5GSxzCc0HJj1F',
 'object': 'chat.completion',
 'created': 1726417151,
 'model': 'gpt-4o-mini-2024-07-18',
 'choices': [{'index': 0,
              'message': {'role': 'assistant',
                          'content': 'The image shows a computer screen displaying code, likely from a Python script. It includes text related to error handling and API service functionality, particularly focusing on session handling, connection errors, and response validation. The code features elements like function definitions, exception handling, and possibly HTTP requests. If you have any specific questions about the code, feel free to ask!',
                          'refusal': None},
              'logprobs': None,
              'finish_reason': 'stop'}],
 'usage': {'prompt_tokens': 2845,
           'completion_tokens': 71,
           'total_tokens': 2916,
           'completion_tokens_details': {'reasoning_tokens': 0}
           },
 'system_fingerprint': 'fp_54e2f484be'
 }

#print(response.json()["choices"][0]["message"]["content"])

#{'index': 0,
# 'message':
# {'role': 'assistant',
# 'content': 'The image shows a screenshot of code from a Python script.
# It appears to be part of an API service related to handling exceptions and making requests. Key elements include:\n\n- Definition of an `exception_handler` function.\n- Use of the `requests` library to create a session and make HTTP requests.\n- Handling specific exception types, such as `TimeoutError` and `ConnectionError`.\n- Validation of responses from an API, including checks for `None` or empty responses.\n\nOverall, it looks like a snippet focusing on managing API interactions and error handling in Python.', 'refusal': None}, 'logprobs': None, 'finish_reason': 'stop'}