import pytest

from main import BooksCollector


class TestBooksCollector:
    def test_add_new_book_name_has_valid_len(self):
        collector = BooksCollector()

        collector.add_new_book("Опасная игра бабули")

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name_book', ["Опасная игра бабули - Опасная игра бабули ", ""])
    def test_add_new_book_invalid_len_name_not_added(self, name_book):
        collector = BooksCollector()

        collector.add_new_book(name_book)

        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_twice_not_added(self):
        collector = BooksCollector()

        collector.add_new_book("Оно")
        collector.add_new_book("Оно")

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_book_genre("Оно") == "Ужасы"

    @pytest.mark.parametrize('name_book, genre_book', [["Опасная игра бабули", "Детективы"], ["Оно", "Ужасы"], ["Гарри Поттер", "Фантастика"]])
    def test_get_book_genre_success(self, name_book, genre_book):
        collector = BooksCollector()

        collector.add_new_book(name_book)
        collector.set_book_genre(name_book, genre_book)

        assert collector.get_book_genre(name_book) == genre_book

    def test_get_books_with_specific_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        result = collector.get_books_with_specific_genre("Ужасы")
        assert result == ["Оно"]

    def test_get_books_with_specific_genre_unsuccess(self):
        collector = BooksCollector()

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', "Ужасы")

        result = collector.get_books_with_specific_genre('Комедии')
        assert result == []

    def test_get_books_genre_success(self):
        collector = BooksCollector()

        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_books_genre() == {'Оно': 'Ужасы'}

    def test_get_books_for_children_valid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Простоквашино")
        collector.set_book_genre("Простоквашино", "Мультфильмы")

        assert collector.get_books_for_children() == ['Простоквашино']

    def test_get_books_for_children_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book("Оно")
        collector.set_book_genre("Оно", "Ужасы")

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_twice_not_added(self):
        collector = BooksCollector()

        collector.add_new_book("Простоквашино")
        collector.add_book_in_favorites("Простоквашино")
        collector.add_book_in_favorites("Простоквашино")

        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_success(self):
        collector = BooksCollector()

        collector.add_new_book("Простоквашино")
        collector.add_book_in_favorites("Простоквашино")
        collector.delete_book_from_favorites("Простоквашино")

        assert len(collector.favorites) == 0

    def test_delete_book_from_favorites_which_not_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book("Простоквашино")
        collector.add_new_book("Оно")
        collector.add_book_in_favorites("Простоквашино")
        collector.delete_book_from_favorites("Оно")

        assert len(collector.favorites) == 1


    def test_get_list_of_favorites_books_success(self):
        collector = BooksCollector()

        collector.add_new_book("Простоквашино")
        collector.add_new_book("Оно")
        collector.add_book_in_favorites("Простоквашино")
        collector.add_book_in_favorites("Оно")

        result = collector.get_list_of_favorites_books()
        assert result == ["Простоквашино", "Оно"]

