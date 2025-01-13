SELECT name, phone_number FROM contacts WHERE id <= 7 OR city = 'Borispol'
SELECT DISTINCT(name) FROM contacts;

INSERT INTO contacts (name, phone_number) VALUES
('Contact 1', 963557581),
('Contact 2', 963557582),
('Contact 3', 963557583),
('Contact 4', 963557584),
('Contact 5', 963557585);

DELETE FROM contacts WHERE id=1 RETURNING *;

CREATE TABLE IF NOT EXISTS contacts
(
    id serial ,
    name character varying(50) NOT NULL,
    phone_number integer NOT NULL UNIQUE,
    city character varying ,
    state character varying,
    created_at timestamp DEFAULT now(),
    PRIMARY KEY (id),
)
