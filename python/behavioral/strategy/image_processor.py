from abc import ABC, abstractmethod

import pytest


# List of strategies
class IImageCompressionStrategy(ABC):
    @abstractmethod
    def compress(self, image: str) -> str:
        pass


class JPEGCompression(IImageCompressionStrategy):
    @abstractmethod
    def compress(self, image: str) -> str:
        return f"Compressing image '{image}' using JPEG format"


class PNGCompression(IImageCompressionStrategy):
    @abstractmethod
    def compress(self, image: str) -> str:
        return f"Compressing image '{image}' using PNG format"


class WebPCompression(IImageCompressionStrategy):
    def compress(self, image: str) -> str:
        return f"Compressing image '{image}' using WebP format"


# Context
class ImageProcessor:
    def __init__(self, compression_strategy: IImageCompressionStrategy):
        self.compression_strategy: IImageCompressionStrategy = compression_strategy

    def process_image(self, image: str) -> str:
        return self.compression_strategy.compress(image)


# Тесты
@pytest.mark.parametrize("image, expected_result", [
    ("image1.jpg", "Compressing image 'image1.jpg' using JPEG format"),
    ("image2.png", "Compressing image 'image2.png' using PNG format"),
    ("image3.webp", "Compressing image 'image3.webp' using WebP format"),
])
def test_image_processor(image, expected_result):
    jpeg_processor = ImageProcessor(JPEGCompression())
    png_processor = ImageProcessor(PNGCompression())
    webp_processor = ImageProcessor(WebPCompression())

    assert jpeg_processor.process_image(image) == expected_result
    assert png_processor.process_image(image) == expected_result
    assert webp_processor.process_image(image) == expected_result


if __name__ == "__main__":
    pytest.main()
