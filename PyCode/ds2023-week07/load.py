import torch
import torchvision
import torch.nn as nn
#from model import LeNet
import torch.optim as optim
import torchvision.transforms as transforms

#预处理函数
transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# 50000张训练图片
train_set = torchvision.datasets.CIFAR10(root='./data', train=True,
                                        download=True, transform=transform)