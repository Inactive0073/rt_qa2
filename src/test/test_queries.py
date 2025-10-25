import psycopg2
import allure
from src.utils.sql_logger import execute_and_log


@allure.feature("SQL Queries")
@allure.story("Получение книг по автору")
def test_books_by_author(cursor: psycopg2.extensions.cursor):
    """Проверяем, что книги Толстого находятся корректно"""
    query = """
        SELECT title FROM books
        WHERE author_id = (SELECT id FROM authors WHERE name LIKE '%Толстой%');
    """
    result = execute_and_log(cursor, query)
    assert len(result) > 0, "Нет книг этого автора"


@allure.feature("SQL Queries")
@allure.story("Количество книг у авторов")
def test_books_count_per_author(cursor: psycopg2.extensions.cursor):
    """Каждый автор должен иметь >= 1 книги"""
    query = """
        SELECT a.name, COUNT(b.id)
        FROM authors a
        LEFT JOIN books b ON a.id = b.author_id
        GROUP BY a.name;
    """
    result = execute_and_log(cursor, query)
    for author, count in result:
        assert count >= 1, f"У автора {author} нет книг"


@allure.feature("SQL Queries")
@allure.story("Получение книг по первой букве")
def test_books_start_with_letter(cursor: psycopg2.extensions.cursor):
    """Названия на 'И' должны быть только 'Идиот'"""
    query = """
        SELECT title FROM books
        WHERE title LIKE 'И%';
    """
    result = execute_and_log(cursor, query)
    titles = [r[0] for r in result]
    assert titles == ["Идиот"], f"Неверные книги: {titles}"


@allure.feature("SQL Queries")
@allure.story("Сортировка книг по году")
def test_books_order_by_year(cursor: psycopg2.extensions.cursor):
    """Сортировка по году должна идти от новых к старым"""
    query = """
        SELECT year FROM books ORDER BY year DESC;
    """
    result = execute_and_log(cursor, query)
    years = [r[0] for r in result]
    assert years == sorted(years, reverse=True), f"Годы не отсортированы: {years}"
