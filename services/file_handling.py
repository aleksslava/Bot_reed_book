import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks = ',.!:;?'

    text = text[start:]

    if len(text) <= size:
        return text, len(text)

    for index in range(size-1, -1, -1):

        if text[index] in marks and text[index+1] not in marks:
            text = text[:index+1]
            break
    return text, len(text)




def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as file:
        text = file.read()
        start = 0
        page = 1

        while True:
            if start >= len(text):
                break
            segment = _get_part_text(text, start, PAGE_SIZE)
            start = start + segment[1]
            book[page] = segment[0].lstrip()
            page += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))


