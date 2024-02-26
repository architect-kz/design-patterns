import pytest

from structural.adapter.ebook import *


class TestBook:
    # write tests here
    def test_paper_book(self):
        book: IBook = PapersBook()
        book.open()
        book.turn_page()

        assert book.get_page() == 2

    def test_ebook_adapter(self) -> None:
        kindle: IEBook = Kindle()
        book: IBook = EBookAdapter(kindle)
        book.open()
        book.turn_page()

        assert book.get_page() == [2, 100]
