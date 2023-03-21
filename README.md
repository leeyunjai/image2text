# image2text
caption generator using lavis, argostranslate.

deploy gradio.

<pre>
pip3 install -r requirements.txt
</pre>

<pre>
python3 main.py
</pre>

If you want to use GPU, Edit main.py
<pre>
# main
cap = captionModel("cpu") ## cuda
trans = translateModel("cpu") ## cuda
demo.launch(share=True) 
</pre>

If you want to change caption model, Edit caption.py
<pre>
# blip 
#model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="large_coco", is_eval=True, device=device)

# blip2 coco_opt2.7b
self.model, self.vis_processors, _ = load_model_and_preprocess(name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=self.device)

# blip2 coco_opt6.7b
self.model, self.vis_processors, _ = load_model_and_preprocess(name="blip2_opt", model_type="caption_coco_opt6.7b", is_eval=True, device=self.device)
</pre>
![bg](bg.png)
