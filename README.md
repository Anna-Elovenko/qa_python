# qa_python
тест test_add_new_book_name_has_valid_len проверяет, что в словарь добавляется книга, у которой в названии меньше 40 символов

тест test_add_new_book_invalid_len_name_not_added проверяет, что в словарь не добавляется книга, у которой в названии больше 40 символов или 0

тест test_add_new_book_twice_not_added проверяет, что в словарь нельзя добавить дважды одну и ту же книгу 
        collector = BooksCollector()

тест test_set_book_genre_success проверяет, что жанр книги устанавливается, если книга есть в словаре и ее жанр входит в список

тест test_get_book_genre_success проверяет, что жанр книги выводится по ее имени 

тест test_get_books_with_specific_genre_success проверяет, что список книг с определенным жанром выводится 

тест test_get_books_genre_success проверяется, что выводится словарь с названием книги и ее жанром 

тест test_get_books_for_children_valid_genre проверяет, что выводится список книг, подходящим детям, без возрастного рейтинга

тест test_get_books_for_children_invalid_genre проверяет, что в списке книг для детей отсутствуют книги с возрастным рейтингом

тест test_add_book_in_favorites_twice_not_added проверяет, что в избранное нельзя добавить дважды одну и ту же книгу 

тест test_delete_book_from_favorites_success проверяет, что книга удаляется из избранного 

тест test_delete_book_from_favorites_which_not_in_favorites проверяет, что нельзя удалить книгу из избранного, которой там нет

тест test_get_list_of_favorites_books_success проверяет, что можно получить список избранных книг 