CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY,
    points INT,
    duplicates INT,
    achievements SMALLINT
);

CREATE TABLE IF NOT EXISTS cards (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    type card_type NOT NULL,
    owner_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE
);
