import tkinter as tk


class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Hello World")
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row = 0, column = 0)





def main():
    root = tk.Tk()
    root.resizable(False,False)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()