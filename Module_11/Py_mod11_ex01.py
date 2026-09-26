#Mod11_ex1

class Publication:
    def __init__(self, name):
        self.name = name


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print("Name:", self.name)
        print("Author:", self.author)
        print("Pages:", self.page_count)


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        print("Name:", self.name)
        print("Chief editor:", self.chief_editor)

magazine = Magazine("Donald Duck", "Aki Hyypää")
book = Book("Compartment No. 6", "Rosa Liksom", 192)

magazine.print_information()
print()
book.print_information()
print()