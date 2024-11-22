import unittest
import os
from image_converter import ImageConverter
from PIL import Image


class TestImageConverter(unittest.TestCase):

    def setUp(self):
        self.output_path = 'test_output'

    def create_image(self, path, format, size=(200, 200), color='red'):
        """Вспомогательный метод для создания тестового изображения."""
        with Image.new('RGB', size, color=color) as img:
            img.save(path, format=format)
        return path


    def test_png_to_gif(self):
        # Создаем исходный PNG файл
        input_path = self.create_image('test_image.png', 'PNG')
        converter = ImageConverter(output_format='GIF', size=(150, 150))
        converter.convert(input_path, f'{self.output_path}.gif')

        self.assertTrue(os.path.exists(f'{self.output_path}.gif'))
        with Image.open(f'{self.output_path}.gif') as img:
            self.assertEqual(img.format, 'GIF')
            self.assertEqual(img.size, (150, 150))

    def test_jpeg_to_png(self):
        converter = ImageConverter(output_format='PNG', size=(100, 100))
        converter.convert('eminem.jpg', f'{self.output_path}.png')

        # Проверяем, что файл был создан и что его формат и размер корректны
        self.assertTrue(os.path.exists(f'{self.output_path}.png'))
        with Image.open(f'{self.output_path}.png') as img:
            self.assertEqual(img.format, 'PNG')
            self.assertEqual(img.size, (100, 100))

    def test_bmp_to_tiff(self):
        # Создаем исходный BMP файл
        input_path = self.create_image('test_image.bmp', 'BMP')
        converter = ImageConverter(output_format='TIFF', size=(50, 50))
        converter.convert(input_path, f'{self.output_path}.tiff')

        self.assertTrue(os.path.exists(f'{self.output_path}.tiff'))
        with Image.open(f'{self.output_path}.tiff') as img:
            self.assertEqual(img.format, 'TIFF')
            self.assertEqual(img.size, (50, 50))

    def test_gif_to_jpeg(self):
        # Создаем исходный GIF файл
        input_path = self.create_image('test_image.gif', 'GIF')
        converter = ImageConverter(output_format='JPEG', size=(120, 80))
        converter.convert(input_path, f'{self.output_path}.jpg')

        self.assertTrue(os.path.exists(f'{self.output_path}.jpg'))
        with Image.open(f'{self.output_path}.jpg') as img:
            self.assertEqual(img.format, 'JPEG')
            self.assertEqual(img.size, (120, 80))

    def tearDown(self):
        # Удаляем созданные файлы после каждого теста
        for extension in ['jpg', 'png', 'gif', 'bmp', 'tiff']:
            input_file = f'test_image.{extension}'
            output_file = f'{self.output_path}.{extension}'
            if os.path.exists(input_file):
                os.remove(input_file)
            if os.path.exists(output_file):
                os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
