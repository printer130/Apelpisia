
from open_ai import msg_from_openai

'''   model="text-davinci-003",
  prompt=prompt_text,
  temperature=0.7,
  max_tokens=96,
  top_p=1,
  engine="davinci",
  frequency_penalty=0,
  presence_penalty=0.3,
  stop=["\n"], '''

# openai.Model.list()
def client(prompt_text):
  response = msg_from_openai(prompt_text)
  print("[*]")
  print(response)
  print("[*]")
  story = response['choices'][0]['text']
  return str(story)