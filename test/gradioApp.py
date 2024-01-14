import gradio as gr
import json
from src.APIclient import simple_chat_prompt


with gr.Blocks() as demo:
    greet_btn = gr.Button("Ai Analysis")
    output = gr.Textbox(label="Output Box")
    greet_btn.click(fn=simple_chat_prompt, outputs=output, api_name="Ai_Analysis")
   
    

demo.launch()

