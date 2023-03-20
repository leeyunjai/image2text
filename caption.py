from PIL import Image
from lavis.models import load_model_and_preprocess

class Model:
  def __init__(self, device="cpu"):
    self.device = device
    # this also loads the associated image processors
    #model, vis_processors, _ = load_model_and_preprocess(name="blip_caption", model_type="large_coco", is_eval=True, device=device)
    self.model, self.vis_processors, _ = load_model_and_preprocess(name="blip2_opt", model_type="caption_coco_opt2.7b", is_eval=True, device=self.device)

  def predict(self, image, num_captions=3):
    #raw_image = Image.open("image.jpg").convert("RGB")
    raw_image = image.convert("RGB")
    # vis_processors stores image transforms for "train" and "eval" (validation / testing / inference)
    image = self.vis_processors["eval"](raw_image).unsqueeze(0).to(self.device)
    # generate caption
    res = self.model.generate({"image": image}, use_nucleus_sampling=True, num_captions=num_captions)
    return res