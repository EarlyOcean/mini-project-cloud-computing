CREATE TABLE instances (
    id SERIAL PRIMARY KEY,
    container_name TEXT,
    port INTEGER,
    db_user TEXT,
    db_password TEXT,
    db_name TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    action TEXT,
    container_name TEXT,
    port INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);