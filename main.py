from GUI.Global_control import root,frame,file_path,img
from GUI.Menu import set_menu
from GUI.Main_Gui import Main_Gui
if __name__ == '__main__':
    set_menu()
    Main_Gui().show()
    root.mainloop()