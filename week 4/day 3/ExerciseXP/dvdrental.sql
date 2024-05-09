/*CREATE TABLE language (
    language_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- Insert languages
INSERT INTO language (name) VALUES 
('English'),
('French'),
('Spanish'),
('German'),
('Korean'),
('Mandarin'),
('Russian'),
('Arabic'),
('Portuguese'),
('Bangali'),
('Hindi');*/

--SELECT *
--FROM language;

/*CREATE TABLE film (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT
);

INSERT INTO film (title, description) VALUES 
('Harry Potter and the Prisoner of Azkaban', 'Fantasy/Adventure'),
('Spiderman 1', 'Action/Sci-fi'),
('Spiderman 2', 'Action/Sci-fi'),
('La La Land', 'Musical/Romance'),
('Litte Women', 'Romance/Drama'),
('IT', 'Horror/Mystery'),
('Mr&Mme Smith', 'Action/Romance');*/


SELECT f.title, f.description, COALESCE(l.name, 'No language') AS language_name
FROM language l
LEFT JOIN film f ON l.name = f.language_name;



