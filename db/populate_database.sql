CREATE TABLE items (
    id SERIAL,
    name VARCHAR(32),
    description VARCHAR(128),
    active BOOLEAN
);

INSERT INTO items (name, description, active)
VALUES
('Item 1', 'Este é o item #1', TRUE),
('Item 2', 'Este é o item #2', TRUE),
('Item 3', 'Este é o item #3', TRUE),
('Item 4', 'Este é o item #4', TRUE),
('Item 5', 'Este é o item #5', TRUE);
