CREATE TABLE IF NOT EXISTS createdCards (
    cardId SERIAL PRIMARY KEY,
    humanName TEXT NOT NULL,
    cardType TEXT NOT NULL,
    whoOwnId TEXT NOT NULL
)
