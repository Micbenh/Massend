import tkinter as tk
import json
import time
import pyautogui
import pyperclip
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


from config import CHROME_PROFILE_PATH
import os 

class MainWindow:
    def __init__(self, master):
        # Window design
        self.master = master
        self.master.title("Massend")
        self.top_frame = tk.Frame(self.master)
        self.top_frame.grid(row = 0, column = 0, padx=10)
        self.webdriver_path = r'Massend\drivers\chromedriver.exe'
        
        self.contact_search_label = tk.Label(self.top_frame, text="Contact name")
        self.contact_search_label.grid(row = 0, column = 0)

        self.contact_search_input = tk.Entry(self.top_frame, width = 35 )
        self.contact_search_input.grid(row = 0, column = 1)

        self.message_text = tk.Text(self.top_frame, width=40, height=10, bd=5)
        self.message_text.grid(row=2, column=0, columnspan=2, pady=10)

        self.send_message_button = tk.Button(self.top_frame, text="Send message", fg="white", bg="red", command=self.selenium_send_messag)
        self.send_message_button.grid(row=3, column=0, pady=5, columnspan=2)

        self.message_amount_var = tk.IntVar()
        self.message_amount_toggle = tk.Spinbox(self.top_frame, from_=1.0, to=1000000, textvariable=self.message_amount_var)
        self.message_amount_toggle.grid(row=3, column=2)

    def selenium_send_messag(self):
        group_search  = self.contact_search_input.get()
        #distribution_group_list = self.get_dist_list() # Will be implemented soon
        text_to_send = self.message_text.get("1.0",'end-1c')
        amount_of_meesages = self.message_amount_var.get()

        options = webdriver.ChromeOptions()
        options.add_argument(CHROME_PROFILE_PATH)
        chrome_webdriver_path = r"Massend\drivers\chromedriver.exe"
        driver = webdriver.Chrome(chrome_webdriver_path,options=options)
        driver.get("http://web.whatsapp.com/")

        driver.maximize_window()
        #wait and search for contact
        input_xpath_contact = "//*[@id='side']/div[1]/div/label/div/div[2]"
        input_xpath_contact_search = WebDriverWait(driver, 50).until(lambda driver: driver.find_element(By.XPATH, input_xpath_contact))
        if input_xpath_contact_search:
            pass
        else: 
            input("press enter after the scan")
        
        input_xpath_contact_search.click()
        input_xpath_contact_search.send_keys(group_search)
        time.sleep(2)
        #find, click contact, click message input, enter message and send
        contact_xpath = '//*[@id="pane-side"]/div[1]/div/div/div[12]/div'
        contact_xpath_class_name = "matched-text i0jNr"
        #driver.find_element(By.XPATH, contact_xpath)
        contact_xpath_job = WebDriverWait(driver, 50).until(lambda driver:  driver.find_element(By.XPATH, contact_xpath))
        #contact_xpath_job = driver.find_element_by_class_name("matched-text i0jNr")
        time.sleep(2)
        contact_xpath_job.click()
        time.sleep(1)
        pyperclip.copy(text_to_send)
        text_message_input_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]'
        text_message_driver = driver.find_element(By.XPATH, text_message_input_xpath)
        text_message_driver.click()
        time.sleep(1)
        for i in range(amount_of_meesages):
            text_message_driver.send_keys(text_to_send)
            time.sleep(0.3)
            text_message_driver.send_keys(Keys.ENTER)
            time.sleep(0.2)
        time.sleep(2)

        
def main():
    root = tk.Tk()
    root.resizable(False,False)
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()