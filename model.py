import torch
import torch.nn as nn
import torch.nn.functional as F

class LSTM(nn.Module):

    def __init__(self):
        
        self.layer1 = nn.LSTM(15, 10, num_layers = 5, bias = True, dropout = 0.05)
        self.layer2 = nn.Linear(10, 1)

    def forward(self, x):

        x = self.layer1(x)
        x = self.lauer2(x)

        return x


