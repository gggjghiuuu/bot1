from diffusers import StableDiffusionPipeline
import torch

print("🔄 Загружаю Stable Diffusion v1-5...")
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Генерация
prompt = "Обезьяна на башне с красными шортами"
image = pipe(prompt).images[0]
image.save("image.png")
print("✅ Реалистичное изображение готово!")