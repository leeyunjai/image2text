from PIL import Image, ImageDraw
import gradio as gr
import os,uvicorn,requests,json,base64
from caption import Model as captionModel
from translate import Model as translateModel

def inference(image):
  items = cap.predict(image)
  res = []
  for item in items:
    res.append({"en":item, "ko":trans.predict(item)+"."})
  
  return res

with gr.Blocks() as demo:
  with gr.Row():
    with gr.Column():
      with gr.Tab("Image"):
        image_input = gr.Image(source="upload", type="pil")
        image_button = gr.Button("Run")

    with gr.Column():
      with gr.Tab("Caption"):
        text_output = gr.JSON()

  image_button.click(inference, inputs=[image_input], outputs=[text_output])

# main
cap = captionModel("cpu")
trans = translateModel("cpu")
demo.launch(share=True)
