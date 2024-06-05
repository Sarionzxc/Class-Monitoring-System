
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8

from tkinter import Frame, Tk, Canvas, Entry, Text, Button, PhotoImage

from build.main_window.class_f.view_class.gui5 import ViewClass
from build.main_window.class_f.update_class.gui4 import UpdateClass
from build.main_window.class_f.add_class.gui3 import AddClass






OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def classRoom():
    ClassRoom()
    

class ClassRoom(Frame):
     def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.selected_rid = None
        self.configure(bg="#FFFFFF")
        #self.product_data = db_controller.get_product()
          # Insert data
        
        self.windows = {
            "add": AddClass(self),
            "view": ViewClass(self),
            "update": UpdateClass(self)
       
        }
        
        self.current_window = self.windows["add"]
        self.current_window.place(x=0, y=0, width=692, height=500)
    
        self.current_window.tkraise()

     def navigate(self, name):
        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Show the screen of the button pressed
        self.windows[name].place(x=0, y=0, width=692, height=500)
