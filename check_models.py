import google.generativeai as genai

genai.configure(api_key="AIzaSyDPjCNMwCaG-A__JLoY-DjfpQUUtRS8ZrM")

print("Available models that support content generation:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")