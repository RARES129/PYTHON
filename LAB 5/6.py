class LibraryItem:
    def __init__(self, title, author, item_id, checked_out):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = checked_out

    def check_out(self):
        if self.checked_out:
            print("Item is already checked out.")
        else:
            self.checked_out = True
            print("Item checked out successfully.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print("Item returned successfully.")
        else:
            print("Item is already in the library.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        print(f"Checked Out: {self.checked_out}")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, checked_out, num_pages):
        super().__init__(title, author, item_id, checked_out)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.num_pages}")


class DVD(LibraryItem):
    def __init__(self, title, author, item_id, checked_out, runtime):
        super().__init__(title, author, item_id, checked_out)
        self.runtime = runtime

    def display_info(self):
        super().display_info()
        print(f"Runtime: {self.runtime}")


class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, checked_out, issue_num):
        super().__init__(title, author, item_id, checked_out)
        self.issue_num = issue_num

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_num}")


def main():
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1, False, 180)
    dvd1 = DVD("The Godfather", "Francis Ford Coppola", 2, False, 175)
    mag1 = Magazine("National Geographic", "Various", 3, False, 2021)

    book1.check_out()
    dvd1.check_out()
    mag1.check_out()

    book1.display_info()
    dvd1.display_info()
    mag1.display_info()

    book1.return_item()
    dvd1.return_item()
    mag1.return_item()

    book1.display_info()
    dvd1.display_info()
    mag1.display_info()


main()
