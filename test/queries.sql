-- 1. Поиск всех книг определенного автора
SELECT b.title, a.name
FROM books AS b
JOIN authors AS a ON b.author_id = a.id
WHERE a.name = 'Лев Толстой';

-- 2. Подсчет количества книг каждого автора
SELECT a.name, COUNT(b.id) AS book_count
FROM authors AS a
LEFT JOIN books AS b ON a.id = b.author_id
GROUP BY a.name;

-- 3. Книги, название которых начинается с буквы "И"
SELECT title FROM books
WHERE title LIKE 'И%';

-- 4. Сортировка по году издания от новых к старым
SELECT title, year FROM books
ORDER BY year DESC;
