-- INSERT INTO  books (id, title, pages, author_id) VALUES (1, 'title', 30, 2);

-- SELECT * FROM books;
-- SELECT * FROM authors;

-- SELECT * FROM books JOIN authors ON author_id=authors.id;
-- SELECT * FROM books LEFT JOIN authors ON author_id=authors.id;
-- SELECT * FROM books RIGHT JOIN authors ON author_id=authors.id;
-- SELECT * FROM books FULL JOIN authors ON author_id=authors.id;
-- SELECT * FROM books  JOIN authors ON author_id=authors.id;
-- SELECT * FROM books CROSS JOIN authors;
-- EXPLAIN ()
-- EXPLAIN ANALYSE SELECT AVG(pages) FROM books JOIN authors ON author_id=authors.id WHERE authors.birth_date >= DATE('1950-01-01')

SELECT author_id, COUNT(*) as books_amount
FROM books
GROUP BY author_id
HAVING COUNT(*) > 2
ORDER BY author_id DESC;


SELECT
    COUNT(*) FILTER ( WHERE views > 0) as book_with_views,
    COUNT(*) FILTER (where views = 0) as books_no_views
FROM books;





-- CREATE TRIGGER my_trigger AFTER INSERT ON authors EXECUTE  FUNCTION


-- CREATE OR REPLACE FUNCTION get_current_time()
-- RETURNS timestamp AS $$
-- BEGIN
--    RETURN CURRENT_TIMESTAMP;
-- END;
-- $$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_sum(i integer ,j integer)
RETURNS integer AS $$
BEGIN

   RETURN i - j;
END;
$$ LANGUAGE plpgsql;


SELECT get_sum(10,5)