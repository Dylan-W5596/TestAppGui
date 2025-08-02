import tkinter as tk
import Pages.login as Login
import Pages.settings as Settings
import json

#---------------------------jsonLoading------------------
class StyleClass:
    def __init__(self, jsonFile_path):
        with open(jsonFile_path, encoding='utf-8') as file:
            self.jsonFile = json.load(file)

        self.globalSettings = self.jsonFile["globalSettings"]
        self.account = self.jsonFile["account"]
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
print(style.globalSettings["version"]) #Version
#---------------------------jsonLoading------------------

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("App")
        self.geometry("800x600")
        self.configure(bg="lightgray")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.Frame = {}

        # Initialize frames
        for F in (Login.Login_Page, Settings.Settings_Page):
            getFrames = F(container, self)
            self.Frame[F] = getFrames
            getFrames.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Login.Login_Page)

    def show_frame(self, page_class):
        frame = self.Frame[page_class]
        frame.tkraise()