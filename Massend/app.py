from importlib.metadata import distribution
import tkinter as tk
import json

class MainWindow:
    def __init__(self, master):
        # Window design
        self.master = master
        self.master.title("Hello World")
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row = 0, column = 0, padx=10)
        self.group_options = self.init_groups_menu()
        self.dist_groups = self.init_distirbution_groups_menu()

        self.group_name_label = tk.Label(self.top_frame, text="Group Name ")
        self.group_name_label.grid(row = 0, column = 0)

        self.group_name_option_default = tk.StringVar(self.master)
        self.group_name_option_default.set(self.group_options[0])
        self.group_name_menu = tk.OptionMenu(self.top_frame , self.group_name_option_default,*self.group_options)
        self.group_name_menu.grid(row=1, column=0)

        self.distribution_group_label = tk.Label(self.top_frame, text="Distribution Group")
        self.distribution_group_label.grid(row = 0, column = 1)

        self.dist_group_option_default = tk.StringVar(self.master)
        self.dist_group_option_default.set(self.dist_groups[0])
        self.dist_group_menu = tk.OptionMenu(self.top_frame , self.dist_group_option_default, *self.dist_groups)
        self.dist_group_menu.grid(row=1, column=1)

        self.random_test_button = tk.Button(self.top_frame, text="click me! test", command=self.init_groups_menu)
        self.random_test_button.grid(row= 0, column = 2)


    def init_groups_menu(self):
        group_options = ['SELECT A GROUP']
        with open("Massend\\data.json", mode="r+", encoding='utf-8') as j:
            print("hello")
            json_file = json.load(j)
            groups = json_file['groups']
            for group in groups:
                group = group.encode("utf-8").decode("UTF-8", errors="replace")
                group_options.append(group)
        return  group_options

    def init_distirbution_groups_menu(self):
        distribution_groups_list = ['SELECT A DISTIRBUTION GROUP']
        with open("Massend\\data.json", mode="r+", encoding='utf-8') as j:
            json_file = json.load(j)
            distribution_groups = json_file['distribution_groups']
            for dist_group in distribution_groups.keys():
                distribution_groups_list.append(dist_group)
        return distribution_groups_list


            


        
def main():
    root = tk.Tk()
    root.resizable(False,False)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()