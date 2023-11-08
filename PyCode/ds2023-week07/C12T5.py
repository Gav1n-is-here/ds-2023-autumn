import torchvision.transforms as transforms
from PIL import Image

img = Image.open('D:\Code\PyCode\ds2023-week07\pic\pic_color.png')
gray_img = transforms.Grayscale()(img)
gray_img = transforms.Resize((400,600))(gray_img)
gray_img.save('D:\Code\PyCode\ds2023-week07\pic\gray_image.jpg')


img=Image.open('D:\Code\PyCode\ds2023-week07\pic\gray_image.jpg')
img.show()