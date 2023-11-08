import torch
import torchvision
import torch.nn as nn
from C12T7 import LeNet
import torch.optim as optim
import torchvision.transforms as transforms
from torchvision import transforms, datasets, utils
import matplotlib.pyplot as plt
import numpy as np


#device : GPU or CPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)


transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])

# 50000张训练图片
train_set = torchvision.datasets.CIFAR10(root='./data', train=True,
                                         download=False, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=36,
                                           shuffle=False, num_workers=0)

# 10000张验证图片
val_set = torchvision.datasets.CIFAR10(root='./data', train=False,
                                       download=False, transform=transform)
val_loader = torch.utils.data.DataLoader(val_set, batch_size=4,
                                         shuffle=False, num_workers=0)
val_data_iter = iter(val_loader)
val_image, val_label = next(val_data_iter)
print(val_image.size())
print(train_set.class_to_idx)
classes = ('plane', 'car', 'bird', 'cat',
          'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


#显示图像，之前需把validate_loader中batch_size改为4
aaa = train_set.class_to_idx
cla_dict = dict((val, key) for key, val in aaa.items())
def imshow(img):
    img = img / 2 + 0.5  # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

print(' '.join('%5s' % cla_dict[val_label[j].item()] for j in range(4)))
imshow(utils.make_grid(val_image))
