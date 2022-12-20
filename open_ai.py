from dotenv import load_dotenv
import os
import openai

load_dotenv()
model = "text-davinci-003"
#openai.api_key = os.environ.get('OPENAI_KEY')
#openai.organization = os.environ.get("OPENAI_ORG")
openai.api_key = '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'
openai.organization = 'org-GM55GnAr7nrRtA2p4TA8npK8'

def msg_from_openai(prompt_text):
  return openai.Completion.create(
      model=model,
      prompt=prompt_text,
      temperature=0.7,
      max_tokens=1000,
    )