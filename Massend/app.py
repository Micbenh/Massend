import tkinter as tk


class MainWindow:
    def __init__(self, master):
        # Window design
        self.master = master
        self.master.title("Hello World")
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row = 0, column = 0, padx=10)

        self.group_name = tk.Label(self.top_frame, text="Group Name ")
        self.group_name.grid(row = 0, column = 0)

        self.distribution_group = tk.Label(self.top_frame, text="Distribution Group")
        self.distribution_group.grid(row = 0, column = 1)



        




def main():
    root = tk.Tk()
    root.resizable(False,False)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()