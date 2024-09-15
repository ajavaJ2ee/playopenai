from openai import OpenAI
from openai.types.chat import ChatCompletionSystemMessageParam

client = OpenAI(api_key="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")
response= client.chat.completions.create(model= "gpt-4o-mini",
                               messages=[{"content":"Best puzzle suggestions for 3 year old kids",
                                         "role":"user"}])


print(response.choices[0].message.content)

# Chat Completion Object
"""{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-4o-mini",
  "system_fingerprint": "fp_44709d6fcb",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "logprobs": null,
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
"""