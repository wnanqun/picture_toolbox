import torch
def run(text):
    pipe=torch.load('models/Stable_Diffusion.pth')
    #pipe=torch.load('D:/迅雷下载/11/1.pth')
    try :
        device=torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        pipe.to(device)
        image = pipe(text,num_inference_steps=5).images[0]
    except:
        device=torch.device( "cpu")
        pipe.to(device)
        image = pipe(text,num_inference_steps=5).images[0]
    return image
