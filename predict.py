# predict.py - PADRÃO COG OFICIAL
import torch
from PIL import Image
import io
from model import ImageGenerator

class Predictor:
    def setup(self):
        self.model = ImageGenerator()
        self.model.eval()
    
    def predict(self, prompt: str = None, width: int = 128, height: int = 128) -> bytes:
        # Gerar imagem dummy
        noise = torch.randn(1, 100)
        with torch.no_grad():
            output = self.model(noise)
        
        # Converter para imagem
        image_data = output.view(28, 28).numpy()
        image = Image.fromarray((image_data * 255).astype('uint8'))
        image = image.resize((width, height))
        
        # Salvar em bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        
        return img_byte_arr.getvalue()