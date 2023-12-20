from tkinter import Tk,Frame
global root,frame,file_path,img
root=Tk()
root.geometry('800x600')
root.title("图片处理工具箱")
frame=Frame(root,bg='#FFFFFF')  
frame.place(relx=0,rely=0,relwidth=1,relheight=1)
file_path=None
save_path=None
img=None
#删除所有控件
def clear():
    for widget in frame.winfo_children():
        widget.destroy()
def set_file_path(path):
    global file_path
    file_path=path

def get_file_path():
    return file_path

def set_save_path(path):
    global save_path
    save_path=path

def get_save_path():
    return save_path