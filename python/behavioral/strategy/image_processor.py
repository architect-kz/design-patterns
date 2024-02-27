from abc import ABC, abstractmethod

import pytest


# List of strategies
class IImageCompressionStrategy(ABC):
    @abstractmethod
    def compress(self, image: str) -> str:
        pass


class JPEGCompression(IImageCompressionStrategy):
    def compress(self, image: str) -> str:
        return f"Compressing image '{image}' using JPEG format"


class PNGCompression(IImageCompressionStrategy):
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

    def set_compression_strategy(self, compression_strategy: IImageCompressionStrategy):
        self.compression_strategy = compression_strategy
