from importlib.metadata import distribution
import tkinter as tk
import json
import time
import pyautogui
import pyperclip


class MainWindow:
    def __init__(self, master):
        # Window design
        self.master = master
        self.master.title("Massend")
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row = 0, column = 0, padx=10)
        self.group_options = self.init_groups_menu()
        self.dist_groups = self.init_distirbution_groups_menu()
        self.webdriver_path = r'Massend\drivers\chromedriver.exe'

        self.group_name_label = tk.Label(self.top_frame, text="Group Name ")
        self.group_name_label.grid(row = 0, column = 0)

        self.group_name_option_default = tk.StringVar(self.master)
        self.group_name_option_default.set(self.group_options[0])
        self.group_name_menu = tk.OptionMenu(self.top_frame , self.group_name_option_default,*self.group_options, command=print(self.group_name_option_default))
        self.group_name_menu.grid(row=1, column=0)

        self.distribution_group_label = tk.Label(self.top_frame, text="Distribution Group")
        self.distribution_group_label.grid(row = 0, column = 1)

        self.dist_group_option_default = tk.StringVar(self.master)
        self.dist_group_option_default.set(self.dist_groups[0])
        self.dist_group_menu = tk.OptionMenu(self.top_frame , self.dist_group_option_default, *self.dist_groups)
        self.dist_group_menu.grid(row=1, column=1)

        self.random_test_button = tk.Button(self.top_frame, text="click me! test (soon to be add groups/dist_groups option)", command=self.init_groups_menu)
        self.random_test_button.grid(row= 0, column = 2)

        self.message_text = tk.Text(self.top_frame, width=40, height=10, bd=5)
        self.message_text.grid(row=2, column=0, columnspan=2, pady=10)

        self.send_message_button = tk.Button(self.top_frame, text="Send message", fg="white", bg="red", command=self.send_message)
        self.send_message_button.grid(row=3, column=0, pady=5, columnspan=2)

    @staticmethod
    def init_groups_menu():
        group_options = ['SELECT A GROUP']
        with open("Massend\\data.json", mode="r+", encoding='utf-8') as j:
            print("hello")
            json_file = json.load(j)
            groups = json_file['groups']
            for group in groups:
                group = group.encode("utf-8").decode("UTF-8", errors="replace")
                group_options.append(group)
        return  group_options

    @staticmethod
    def init_distirbution_groups_menu():
        distribution_groups_list = ['SELECT A DISTIRBUTION GROUP']
        with open("Massend\\data.json", mode="r+", encoding='utf-8') as j:
            json_file = json.load(j)
            distribution_groups = json_file['distribution_groups']
            for dist_group in distribution_groups.keys():
                distribution_groups_list.append(dist_group)
        return distribution_groups_list

    def get_dist_list(self):
        dist_group = self.dist_group_option_default.get()
        if  dist_group != "SELECT A DISTIRBUTION GROUP":
            with open("Massend\\data.json", mode="r+", encoding='utf-8') as j:
                json_file = json.load(j)
                distribution_group = json_file['distribution_groups'][dist_group]
            return distribution_group
        else:
             return ''

    def send_message(self):
        # values init
        group_search  = self.group_name_option_default.get()
        distribution_group_list = self.get_dist_list() # Will be implemented soon
        text_to_send = self.message_text.get("1.0",'end-1c')
        screenWidth, screenHeight = pyautogui.size()
        #mouse and keyboard actions
        #search for group and wait for loading
        pyautogui.moveTo(200,400, duration=0.1)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press("backspace")
        pyperclip.copy(group_search)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        #move to chat and write text
        pyautogui.moveTo(screenHeight * 0.06, screenHeight * 0.3, duration=0.5)
        pyautogui.click()
        pyautogui.moveTo(2000, screenHeight*0.92, duration=0.3)
        if distribution_group_list != '':
            for name in distribution_group_list:
                tagged_name = "@" + name + ""
                pyperclip.copy(tagged_name)  
                pyautogui.hotkey('ctrl', 'v')
                time.sleep(0.2)
                pyautogui.press("enter")
        pyperclip.copy(text_to_send)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(3)
        pyautogui.press('enter')

def main():
    root = tk.Tk()
    root.resizable(False,False)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()