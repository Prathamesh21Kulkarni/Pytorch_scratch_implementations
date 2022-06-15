import torch
import torch.nn as nn
import torch.nn.functional as F

# Input size: 1*32*32

class LeNet(nn.Module):
    def __init__(self):
        super(LeNet, self).__init__()
        self.pool = nn.AvgPool2d(kernel_size=(2, 2), stride=(2, 2))
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=(5, 5), stride=(1, 1), padding=(1, 1))
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=(5, 5), stride=(1, 1), padding=(1, 1))
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=20, kernel_size=(5, 5), stride=(1, 1), padding=(1, 1))
        self.linear1 = nn.Linear(120, 84)
        self.linear2 = nn.Linear(84, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = x.reshape(x.shape[0], -1)
        x = F.relu(self.linear1(x))
        x = self.linear2(x)
        return x
        
if __name__ == "__main__":
    x = torch.rand(64, 1, 32, 32)
    model = LeNet()
    model(x)
