import openai, config, subprocess
openai.api_key = config.OPENAI_KEY

# Setting up the assistant and initial messages collector
ai_personality = "You are helpful assistant. Be specific and thorough with your answers"
messages=[{ "role": "system", "content": ai_personality}]

def askjarvis(user_input, ai_talk=False):
  """
  *** ai_talk makes the computer (Mac) say whatever the AI response is
  """
  global messages # Becase we want messages to be in scope of the function

  messages.append({"role": "user", "content": user_input}) # appending data to maintain conversation context
  completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
  
  api_reposnse = completion["choices"][0]["message"] 
  assistant_response = api_reposnse.get("content")
  messages.append(api_reposnse) # appending data to maintain conversation context

  print("\n🔮 Answer:")
  print(assistant_response)

  if ai_talk:
    subprocess.call(["say", assistant_response])
  return True

while True:
  user_input = input("\n🤖 Ask me anything...\n")
  if user_input.lower() == "exit":
      break
  else:
    askjarvis(user_input, ai_talk=False)