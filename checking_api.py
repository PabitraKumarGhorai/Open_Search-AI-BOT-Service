import openai
import config
openai.api_key = config.api_key

user_input = input("Please give your input: ")


response = openai.chat.completions.create(
model="gpt-3.5-turbo",
messages=[{"role": "user", "content": user_input}]
)
#print(response)

bot_reply = response.choices[0].message.content
print(bot_reply)
        


