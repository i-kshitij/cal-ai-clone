import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

import base64


# 1. open the image file in binary mode ("rb"), read its bytes
with open("test.jpg", "rb") as image_file:
    image_bytes = image_file.read()
# 2. base64.b64encode(the_bytes) then .decode("utf-8") to turn it into a string
encoded_image = base64.b64encode(image_bytes).decode("utf-8")

# 3. build the messages list with two content blocks:
#    - {"type": "text", "text": "What food is this? Estimate calories and macros."}
#    - {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_string}"}}
messages=[
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "What food is this? Estimate calories and macros."},
            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}}
        ]
    }
]
# 4. send it via client.chat.completions.create(...) same as before

response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=messages
)
print(response.choices[0].message.content)