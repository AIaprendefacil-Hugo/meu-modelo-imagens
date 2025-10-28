# model.py
import torch
import torch.nn as nn

class ImageGenerator(nn.Module):
    def __init__(self):
        super().__init__()
        # Arquitetura simples para exemplo
        self.layers = nn.Sequential(
            nn.Linear(100, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(), 
            nn.Linear(512, 784),  # 28x28 image
            nn.Tanh()
        )
    
    def forward(self, x):
        return self.layers(x)

# Teste basico
if __name__ == "__main__":
    model = ImageGenerator()
    print("Modelo criado com sucesso!")