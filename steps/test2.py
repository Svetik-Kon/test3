import os
from behave import given, when, then
from PIL import Image
from converter import ImageConverter, create_test_image


def get_file_size(path):
    """Вспомогательная функция для получения размера файла."""
    return os.path.getsize(path) if os.path.exists(path) else 0


@given('I have an image file "{input_format}" with dimensions {input_width}x{input_height}')
def step_given_image_file_with_dimensions(context, input_format, input_width, input_height):
    # Создаем путь к входному файлу изображения и сохраняем формат и размер
    context.input_path = f'test_image.{input_format.lower()}'
    context.input_format = input_format
    context.input_size = (int(input_width), int(input_height))
    create_test_image(context.input_path, format=input_format, size=context.input_size)
    context.initial_file_size = get_file_size(context.input_path)


@when('I convert it to "{output_format}" with dimensions {output_width}x{output_height}')
def step_when_convert_image(context, output_format, output_width, output_height):
    # Определяем путь и формат выходного файла
    context.output_path = f'test_output.{output_format.lower()}'
    context.output_format = output_format
    context.output_size = (int(output_width), int(output_height))

    converter = ImageConverter(output_format=output_format, size=context.output_size)
    converter.convert(context.input_path, context.output_path)


@then('the output image should be in "{output_format}" format')
def step_then_output_format(context, output_format):
    # Проверяем, что выходное изображение имеет правильный формат
    with Image.open(context.output_path) as img:
        assert img.format == output_format, f"Expected format {output_format}, but got {img.format}"


@then('the output image dimensions should be {output_width}x{output_height}')
def step_then_output_dimensions(context, output_width, output_height):
    # Проверяем, что выходное изображение имеет правильные размеры
    with Image.open(context.output_path) as img:
        expected_size = (int(output_width), int(output_height))
        assert img.size == expected_size, f"Expected size {expected_size}, but got {img.size}"


# Очистка файлов после теста
def after_scenario(context, scenario):
    # Удаляем созданные файлы после выполнения сценария
    for file_path in [context.input_path, context.output_path]:
        if os.path.exists(file_path):
            os.remove(file_path)
