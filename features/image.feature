Feature: Image conversion with size change
  As a user, I want to convert images from one format to another and change their size
  so that they meet my requirements for both format and size.

  Scenario Outline: Convert an image from one format to another with size change
    Given I have an image file "<input_format>" with dimensions <input_width>x<input_height>
    When I convert it to "<output_format>" with dimensions <output_width>x<output_height>
    Then the output image should be in "<output_format>" format
    And the output image dimensions should be <output_width>x<output_height>

    Examples:
      | input_format | output_format | input_width | input_height | output_width | output_height |
      | PNG          | GIF           | 200         | 200          | 150          | 150           |
      | JPEG         | PNG           | 300         | 200          | 100          | 100           |
      | BMP          | TIFF          | 200         | 200          | 50           | 50            |
      | GIF          | JPEG          | 250         | 250          | 120          | 80            |
