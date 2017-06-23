import whatsapp_dp
from tkinter import Tk, BOTH
from tkinter.ttk import Frame

class Window(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Wasp")
        self.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    root.geometry("400x400+400+400")
    window = Window(root)
    window.mainloop() 

if __name__ == '__main__':
    main()