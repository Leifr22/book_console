import json 

from typing import List,Dict, Optional

DATA_FILE='library.json'

class Book:
    def __init__(self,book_id,title,author,year,status: str ='в наличии'):
        self.id=book_id
        self.title=title
        self.author=author
        self.year=year
        self.status=status
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.year,

        }
    @staticmethod
    def from_dict(data):
        return Book(
            book_id=data['id'],
            title=data['title'],
            author=data['author'],
            year=data['year'],
            status=data['status'],
        )
class Library:
    def __init__(self) :
        self.books: List[Book]=[]
        self.data()
    def data(self):
        try:
            with open(DATA_FILE,'r',encoding='utf-8') as f:
                books_data=json.load(f)
                self.books=[Book.from_dict(b) for b in books_data]
        except (FileNotFoundError,json.JSONDecodeError):
            self.books=[]
    def save(self):
        with open(DATA_FILE, 'w',encoding='utf-8') as f:
            json.dump([book.to_dict() for book in self.books], f, ensure_ascii=False, indent=4)
    def add(self,title, author,year):
        book_id = max([book.id for book in self.books], default=0) + 1
        new_book=Book(book_id,title,author,year)
        self.books.append(new_book)
        self.save()
        def remove_book(self, book_id: int) -> bool:

    
            for book in self.books:
                if book.id == book_id:
                    self.books.remove(book)
                    self.save_data()
                return True
        return False

    def search_books(self, key: str, value: str) -> List[Book]:
        """Ищет книги по ключу (title, author, year)."""
        return [book for book in self.books if str(getattr(book, key, "")).lower() == value.lower()]

    def list_books(self) -> List[Book]:
        """Возвращает список всех книг."""
        return self.books

    def update_status(self, book_id: int, new_status: str) -> bool:
        """Обновляет статус книги."""
        for book in self.books:
            if book.id == book_id:
                if new_status in ["в наличии", "выдана"]:
                    book.status = new_status
                    self.save_data()
                    return True
        return False


def main():
    library = Library()
    print("Добро пожаловать в библиотечный менеджер!")
    
    while True:
        print("\nДоступные действия:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("6. Выйти")
        
        choice = input("Выберите действие (1-6): ").strip()
        
        if choice == "1":
            title = input("Введите название книги: ").strip()
            author = input("Введите автора книги: ").strip()
            try:
                year = int(input("Введите год издания книги: ").strip())
                library.add(title, author, year)
                print("Книга успешно добавлена!")
            except ValueError:
                print("Ошибка: год должен быть числом.")
        
        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: ").strip())
                if library.remove_book(book_id):
                    print("Книга успешно удалена!")
                else:
                    print("Ошибка: книга с таким ID не найдена.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")
        
        elif choice == "3":
            key = input("Искать по (title, author, year): ").strip()
            value = input(f"Введите значение для поиска ({key}): ").strip()
            results = library.search_books(key, value)
            if results:
                print("Найденные книги:")
                for book in results:
                    print(book.to_dict())
            else:
                print("Книг по данному запросу не найдено.")
        
        elif choice == "4":
            books = library.list_books()
            if books:
                print("Список всех книг:")
                for book in books:
                    print(book.to_dict())
            else:
                print("Библиотека пуста.")
        
        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: ").strip())
                new_status = input("Введите новый статус (в наличии/выдана): ").strip()
                if library.update_status(book_id, new_status):
                    print("Статус книги успешно обновлен!")
                else:
                    print("Ошибка: либо книга не найдена, либо статус неверный.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")
        
        elif choice == "6":
            print("Выход из программы. До свидания!")
            break
        
        else:
            print("Ошибка: неверный выбор.")


if __name__ == "__main__":
    main()