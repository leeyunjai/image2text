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

![bg](bg.png)
