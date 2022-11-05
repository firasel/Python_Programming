import keyboard


class Book:
    def __init__(self, bookContent) -> None:
        self.pages = bookContent.split("--")
        self.currentPage = -1

    def pageResize(self):
        if self.currentPage >= len(self.pages):
            self.currentPage -= len(self.pages)
            self.pageResize()
        elif self.currentPage < 0:
            self.currentPage = 0

    def next(self, page=False):
        if page == False:
            self.currentPage += 1
            self.pageResize()
            print(self.pages[self.currentPage])
        else:
            self.currentPage += page
            self.pageResize()
            print(self.pages[self.currentPage])
        print("[enter - read more, press q to quit]")

    def openBook(self):
        self.next()
        typedKey = ""
        while True:
            tempKey = keyboard.read_event()
            if tempKey.event_type == keyboard.KEY_UP:
                if tempKey.name == 'q' and len(typedKey) == 0:
                    break
                elif tempKey.name == 'enter':
                    self.next(len(typedKey) != 0 and int(typedKey))
                    typedKey = ""
                else:
                    if tempKey.name in "0123456789":
                        typedKey += tempKey.name
                    elif tempKey.name in "-":
                        typedKey = tempKey.name + typedKey


with open('sample.txt', 'r') as file:
    lines = file.readlines()
    bookStr = "--".join(lines)
    myBook = Book(bookStr)
    myBook.openBook()
