from dotenv import load_dotenv
import os
import openai

load_dotenv()
model = "text-davinci-003"
openai.api_key = os.environ.get('OPENAI_KEY')
openai.organization = os.environ.get("OPENAI_ORG")

def msg_from_openai(prompt_text):
  return openai.Completion.create(
      model=model,
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=1000,
    )