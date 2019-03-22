#!/usr/bin/env python3
import pyocr
from PIL import Image


def test(image):
    tools = pyocr.get_available_tools()
    tool = tools[0]
    print("Using {}".format(tool.get_name()))

    return tool.image_to_string(image, "eng")

print(test(Image.open("test.png")))