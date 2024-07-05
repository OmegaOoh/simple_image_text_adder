import pandas as pd
from nameplate import Printer

class Namelist:
    def __init__(self, printer_cls: Printer, list_file: str, prefix: str = ""):
        self.printer = printer_cls
        self.prefix = prefix
        # Read CSV
        self.df = pd.read_csv(list_file)

    def start(self):
        print("Starting...")
        for i, r in self.df.iterrows():
            name = self.prefix + r["Nickname (English)"].capitalize().strip()
            if r["Do you want contract information on your nameplate?"] == "Yes":
                platform = r["Platforms"]
                user = r["Username"]
                self.printer.text_on_pics(name, platform, user)
            else:
                self.printer.text_on_pics(name)

        print("\nProcess is finished")

    def dbg(self):
        print("Database")
        for i, r in self.df.iterrows():
            print(i, r)