from nameplate import Printer
from namelist import Namelist

# Change config here
name_font = ("arial.ttf", 600)  # Fonts for the Name
contact_font = ("arial.ttf", 300)  # Fonts for contact info
template = "x.png"  # Name of nameplate template file
data_file = "x.csv"  # List file

printer = Printer(template, name_font, contact_font, 300)

process = Namelist(printer, data_file, prefix="x")

print(f"formatter is ready to use.\n data file: {data_file}\n font for name: {name_font} \n font for contact: {contact_font}\n template file: {template}")


while True:
    u_i = input("press any key to continue\n")
    match u_i:
        case "dbg" | "debug":
            process.dbg()
        case "exit" | "quit":
            break
        case _:
            process.start()
            break
