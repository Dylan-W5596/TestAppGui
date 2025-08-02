import tkinter as tk
import Pages.home as Home
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

class Home_Page(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.Label = tk.Label(self,
                              text="Home",
                              font=(style.font["family"], style.font["size"]),
                              bg=style.color["background"],
                              fg=style.color["text"])
        self.Label.pack(pady=20)

        self.SettingsButton = tk.Button(self,
                                       text="Go to Settings",
                                       command=lambda: parent.show_frame(Settings.Settings_Page),
                                       font=(style.font["family"], style.font["size"]),
                                       bg=style.color["btnBg"],
                                       fg=style.color["text"])
        self.SettingsButton.pack(pady=10)