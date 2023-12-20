import cv2
import torch
import torchvision
import torchvision.transforms as transforms
def run(path):
    img=cv2.imread(path) #读入原图片
    img=cv2.resize(img,(224,224))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    transform = transforms.Compose(
        [transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
    img=transform(img)
    img=img.unsqueeze(0)
    #resnet = torchvision.models.alexnet(pretrained=True)
    # 模型类必须在此之前被定义
    model = torch.load('models/alexnet.pth')
    model.eval()
    outputs = model(img)
    value,id =torch.max(outputs,1)
    f=open('data/labels.txt','r',encoding='utf-8')
    l=f.readlines()
    f.close()
    return l[id].split(',')[0]
