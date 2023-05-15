import openai;
import gradio as gr
import warnings
warnings.filterwarnings("ignore")

openai.api_key = "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"

messages = [
    {"role": "system", "content": ""},
]


def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.inputs.Textbox(lines=7, label="Input Symptoms")
outputs = gr.outputs.Textbox(label="Possible Diagnosis")

demo = gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="BioBase Diagnosis: AI Diagnosis",
             theme="compact")

demo.launch(share=True)