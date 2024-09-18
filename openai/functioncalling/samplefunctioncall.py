import json

from openai import OpenAI

client= ""



def get_delivery_date(order_id: str):
    print(f"Order Id passed is :{order_id}")


# function definition
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_delivery_date",
            "description": "Get the delivery date for a customer's order. Call this whenever you need to know the delivery date, for example when a customer asks 'Where is my package'",
            "parameters": {
                "type": "object",
                "properties": {
                    "order_id": {
                        "type": "string",
                        "description": "The customer's order ID.",
                    },
                },
                "required": ["order_id"],
                "additionalProperties": False,
            },
        }
    }
]

messages=[
    {"role":"system","content":"You are a helpful customer support assistant. Use the supplied tools to assist the user."},
    {"role":"user","content":"Hi, can you tell me the delivery date for my order?"},
    {"role":"assistant","content":"Hi there! I can help with that. Can you please provide your order ID?"},
    {"role":"user","content":"i think it is order_12345"}
]
#print(response.choices[0].message)
#ChatCompletionMessage(content=None, refusal=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_GYlBPWKu7atCIjFkOUgvVtu6', function=Function(arguments='{"order_id":"order_12345"}', name='get_delivery_date'), type='function')])

response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools
)

#tool_call=response.choices[0].message.tool_calls[0]
#print(tool_call)
#ChatCompletionMessageToolCall(id='call_eVKMhIzv8OEXgOiyqT5vO3bN', function=Function(arguments='{"order_id":"order_12345"}', name='get_delivery_date'), type='function')

tool_call = response.choices[0].message.tool_calls[0]
#arguments = json.loads(tool_call['function']['arguments'])
arguments = json.loads(tool_call.function.arguments)
order_id=arguments.get('order_id')
delivery_date=get_delivery_date(order_id)

#print(response.choices[0].message)





