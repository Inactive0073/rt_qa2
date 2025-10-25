import psycopg2


def test_books_by_author(cursor: psycopg2.extensions.cursor):
    """Проверяем, что книги Толстого находятся корректно"""
    cursor.execute("""
        SELECT title FROM books
        JOIN authors a ON books.author_id = a.id
        WHERE a.name = 'Лев Толстой';
    """)
    result = [r[0] for r in cursor.fetchall()]
    assert set(result) == {"Война и мир", "Анна Каренина"}


def test_books_count_per_author(cursor: psycopg2.extensions.cursor):
    """Каждый автор должен иметь >= 1 книги"""
    cursor.execute("""
        SELECT a.name, COUNT(b.id)
        FROM authors a
        LEFT JOIN books b ON a.id = b.author_id
        GROUP BY a.name;
    """)
    data = cursor.fetchall()
    for author, count in data:
        assert count >= 1, f"У автора {author} нет книг"


def test_books_start_with_letter(cursor: psycopg2.extensions.cursor):
    """Названия на 'И' должны быть только 'Идиот'"""
    cursor.execute("""
        SELECT title FROM books
        WHERE title LIKE 'И%';
    """)
    result = [r[0] for r in cursor.fetchall()]
    assert result == ["Идиот"]


def test_books_order_by_year(cursor: psycopg2.extensions.cursor):
    """Сортировка по году должна идти от новых к старым"""
    cursor.execute("""
        SELECT year FROM books ORDER BY year DESC;
    """)
    years = [r[0] for r in cursor.fetchall()]
    assert years == sorted(years, reverse=True)
