from abc import ABC, abstractmethod


class IBook(ABC):
    @abstractmethod
    def turn_page(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_page(self) -> int:
        pass


class IEBook(ABC):
    @abstractmethod
    def unlock(self) -> None:
        pass

    @abstractmethod
    def press_next(self) -> None:
        pass

    @abstractmethod
    def get_page(self) -> list[int]:
        pass


class Kindle(IEBook):
    def __init__(self):
        self._page = 1
        self._total_pages = 100

    def press_next(self) -> None:
        self._page += 1

    def get_page(self) -> list[int]:
        return [self._page, self._total_pages]

    def unlock(self) -> None:
        pass


class EBookAdapter(IBook):
    def __init__(self, ebook: IEBook):
        self._ebook = ebook

    def turn_page(self) -> None:
        self._ebook.press_next()

    def open(self) -> None:
        self._ebook.unlock()

    def get_page(self) -> list[int]:
        return self._ebook.get_page()


class PapersBook(IBook):
    def __init__(self):
        self._page = 1

    def open(self) -> None:
        self._page = 1

    def turn_page(self) -> None:
        self._page += 1

    def get_page(self) -> int:
        return self._page


# Client code
def read_book(book: IBook) -> None:
    book.open()
    print("Current Page:", book.get_page())
    book.turn_page()
    print("Next Page:", book.get_page())


if __name__ == "__main__":
    papers_book = PapersBook()
    kindle = Kindle()
    ebook_adapter = EBookAdapter(kindle)

    print("Reading Paper Book:")
    read_book(papers_book)

    print("\nReading EBook (Kindle):")
    read_book(ebook_adapter)
