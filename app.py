import requests
from pages.book_pages import AllBooksPage

# For extracting data from single page of a Website
page_content = requests.get("http://books.toscrape.com/index.html").content

page = AllBooksPage(page_content)
books = page.books

# Far extracting data from multiple pages of a Website
for p_num in range(1, page.totalpages): #To Extract data from first 10 pages
    url = f"http://books.toscrape.com/catalogue/page-{p_num+1}.html"
    page_content = requests.get(url).content

    page = AllBooksPage(page_content)
    books.extend(page.books)

USER_CHOICE ="""Enter the choice accordingly:-

- "b" for printing BEST BOOKS
- "c" for printing CHEAPEST BOOKS
- "o" for printing ALL BOOKS CONTENT
- "q" for EXIT

Enter your choice:"""

def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]  # Top 10 highest rated books
    for book in best_books:
        print(book)

def print_cheapest_books():
    cheap_books = sorted(books, key=lambda x: x.price)[:10]  # Top 10 least price books
    for book in cheap_books:
        print(book)

def overall_content():
    for book in books:
        print(book)

user_choices = {
    "b": print_best_books,
    "c": print_cheapest_books,
    "o": overall_content
}

def menu():
    user_input = input(USER_CHOICE).strip()
    while user_input!="q":
        if user_input in ("b", "c", "o"):
            user_choices[user_input]()
        else:
            print("<Wrong Input: Please! Enter correct choice>")
        user_input = input(USER_CHOICE)

#Driver Function
if __name__ == "__main__":
    menu()