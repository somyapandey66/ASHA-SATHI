!pip install gradio groq
from groq import Groq

client = Groq(api_key="your_groq_api_key_here")

print("Groq loaded successfully!")
def translate_for_villager(medical_text, language):
    prompt = f"""
You are helping an ASHA worker in Jharkhand, India.
Convert the following medical instruction into very simple, easy to understand {language} that an uneducated villager can understand.
Use simple everyday words. No medical jargon. Be warm and friendly in tone.

Medical instruction: {medical_text}

Respond ONLY in {language}. Nothing else.
"""
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content
  import gradio as gr

def app(medical_text, language):
    return translate_for_villager(medical_text, language)

interface = gr.Interface(
    fn=app,
    inputs=[
        gr.Textbox(label="Medical Instruction", placeholder="Type medical instruction here..."),
        gr.Dropdown(choices=["Hindi", "Santhali", "Nagpuri"], label="Select Language")
    ],
    outputs=gr.Textbox(label="Simplified Message for Villager"),
    title="🌸 Asha Saathi",
    description="Helping ASHA workers communicate health information in local languages"
)

interface.launch(share=True)
  
