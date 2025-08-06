import tkinter as tk
import time
import Pages.home as Home
import json

#---------------------------jsonLoading------------------
class StyleClass:
    def __init__(self, jsonFile_path):
        with open(jsonFile_path, encoding='utf-8') as file:
            self.jsonFile = json.load(file)

        self.globalSettings = self.jsonFile["globalSettings"]
        self.account = self.jsonFile["account"]
        self.windowConfig = self.jsonFile["windowConfig"]
        self.color = self.jsonFile["color"]
        self.font = self.jsonFile["font"]

        jsonFileKeys = []
        def getJsonFileTopKeys(jsonFile): #Get the top keys of the JSON file
            for key in jsonFile:
                jsonFileKeys.append(key)

        getJsonFileTopKeys(self.jsonFile) #Put top keys into the JSONFILEKEYS list

        for keys in jsonFileKeys:
            if keys not in self.jsonFile:
                print(f"⚠️ '{keys}' 不存在於 JSON 檔案中！實際資料是：")
                print(self.jsonFile)

        if self.jsonFile == {}:
            print("⚠️ json not working.")

style = StyleClass("Styles/styles.json") #Configure the style is in StyleClass
#---------------------------jsonLoading------------------

class Login_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Fix: assign controller to self.controller
        #title
        self.Title = tk.Label(self,
                              text="Login",
                              font=(style.font["family"], style.font["size"]),
                              bg=style.color["bg"],
                              fg=style.color["text"],
                              anchor="center")
        self.Title.pack(side="top", pady=30)

        #UserName Part
        user_frame = tk.Frame(self, bg=style.color["bg"])
        user_frame.pack(pady=10)
        self.nameEntryLabel = tk.Label(user_frame,
                                     text="UserName : ",
                                     font=(style.font["family"], style.font["size"]),
                                     bg=style.color["bg"],
                                     fg=style.color["text"])
        self.nameEntryLabel.pack(side="left")

        self.UsernameEntry = tk.Entry(user_frame,
                                     font=(style.font["family"], style.font["size"]),
                                     bg=style.color["bg"],
                                     fg=style.color["text"])
        self.UsernameEntry.pack(side="left")

        #Password Part
        password_frame = tk.Frame(self, bg=style.color["bg"])
        password_frame.pack(pady=10)
        self.passwordEntryLabel = tk.Label(password_frame,
                                           text="Password : ",
                                           font=(style.font["family"], style.font["size"]),
                                           bg=style.color["bg"],
                                           fg=style.color["text"])
        self.passwordEntryLabel.pack(side="left")

        self.PasswordEntry = tk.Entry(password_frame,
                                    font=(style.font["family"], style.font["size"]),
                                    bg=style.color["bg"],
                                    fg=style.color["text"],)
        self.PasswordEntry.pack(side="left", pady=10)

        self.errorLabel = tk.Label(self,
                                   text="",
                                   font=(style.font["family"], style.font["size"]-5),
                                   fg=style.color["error"])
        self.errorLabel.pack(side="top", pady=10)

        #Login Button
        self.LoginButton = tk.Button(self,
                                     text="Login",
                                     command=self.login_process,
                                     font=(style.font["family"], style.font["size"]),
                                     bg=style.color["btnBg"],
                                     fg=style.color["error"])
        self.LoginButton.pack(side="top", pady=20)

    def login_process(self):
        InputUserName = self.UsernameEntry.get()
        InputPassword = self.PasswordEntry.get()

        if InputUserName == style.account["Name"] and InputPassword == style.account["PassWord"]:
            # Switch to Home_Page
            self.controller.show_frame(Home.Home_Page)
            print("Login successful")
        else:
            print("Login failed")
            self.errorLabel.config(text="Invalid username or password.")
            time.sleep(1)  #delay some time
            self.errorLabel.config(text="")
