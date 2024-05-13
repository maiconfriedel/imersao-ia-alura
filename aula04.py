from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# for model in genai.list_models():
#   if 'generateContent' in model.supported_generation_methods:
#     print(model.name)

generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}

safety_settings = {
  "HARASSMENT": "BLOCK_NONE",
  "HATE" : "BLOCK_NONE",
  "SEXUAL" : "BLOCK_NONE",
  "DANGEROUS": "BLOCK_NONE"
}

model = genai.GenerativeModel(model_name="models/gemini-1.0-pro", 
                              safety_settings=safety_settings, 
                              generation_config=generation_config)

# response = model.generate_content('Vamos aprender conteúdo sobre IA. Me dê sugestões')
# print(response.text)

chat = model.start_chat(history=[])

prompt = input("Esperando prompt: ")

while prompt != "fim":
  response = chat.send_message(prompt)
  print("Resposta: ", response.text, "\n")
  prompt = input("Esperando prompt: ")