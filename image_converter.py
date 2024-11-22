
from PIL import Image
import os


class ImageConverter:
    def __init__(self, output_format='JPEG', size=None):
        self.output_format = output_format
        self.size = size

    def convert(self, input_path, output_path):
        if not os.path.exists(input_path):
            raise FileNotFoundError("Input file does not exist.")

        with Image.open(input_path) as img:
            if self.size:
                img = img.resize(self.size)
            img = img.convert("RGB")
            img.save(output_path, self.output_format)