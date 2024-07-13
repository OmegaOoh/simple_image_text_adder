import os
from PIL import Image, ImageDraw, ImageFont

class Printer:
    def __init__(self, file: str, name_font: tuple, contact_font: tuple, frame: int = 100):
        self.image = Image.open(file)
        self.name_font = ImageFont.truetype(*name_font)
        self.contact_font = ImageFont.truetype(*contact_font)
        self.color = (255, 255, 255)
        self.outline = 100
        self.frame = frame

    def text_on_pics(self, name: str, platform: str = None, user: str = None) -> None:
        os.getcwd()
        try:
            os.chdir("image")
        except FileNotFoundError:
            os.mkdir("image")
            os.chdir("image")
        img = self.image.copy()
        draw = ImageDraw.Draw(img)

        # add name
        _, _, text_width, text_height = draw.textbbox((0, 0), name, font=self.name_font)
        center = (self.image.size[0] - text_width) / 2, (self.image.size[1] - text_height ) /2
        draw.text(center, name, fill=self.color, font=self.name_font)

        # add contact
        if platform is not None and user is not None:
            contact = "{}: {}".format(platform, user)
            _, _, text_width, text_height = draw.textbbox((0, 0), contact, font=self.contact_font)
            center = (self.image.size[0] - text_width) / 2, (self.image.size[1] - text_height) / 2
            draw.text((center[0], img.height - text_height - self.frame), contact, fill=self.color, font=self.contact_font)

        if os.path.exists(name + ".png"):
            i = 0
            while os.path.exists(name + ".png"):
                i += 1
                name = name + "({})".format(i)

        print("saved {}.png".format(name))
        img.save(name + ".png")
        os.chdir('..')
