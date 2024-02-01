from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler
import torch

class Model:
    def __init__(self):
        model_id = "stabilityai/stable-diffusion-2-1-base"
        scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
        self.pipe = self.pipe.to("cuda")

    def generate_image(self, prompt):
        image = self.pipe(prompt).images[0]
        image.save("res/generation.png")
