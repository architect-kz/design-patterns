import pytest
from behavioral.strategy.image_processor import ImageProcessor, JPEGCompression, PNGCompression, WebPCompression


@pytest.mark.parametrize("image, expected_result, strategy", [
    ("image1.jpg", "Compressing image 'image1.jpg' using JPEG format", JPEGCompression),
    ("image2.png", "Compressing image 'image2.png' using PNG format", PNGCompression),
    ("image3.webp", "Compressing image 'image3.webp' using WebP format", WebPCompression),
])
def test_image_processor(image, expected_result, strategy):
    image_processor = ImageProcessor(strategy())

    assert image_processor.process_image(image) == expected_result


if __name__ == "__main__":
    pytest.main()
