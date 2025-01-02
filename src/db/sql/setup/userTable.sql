CREATE TABLE IF NOT EXISTS userTable (
    userId SERIAL PRIMARY KEY,
    totalPoints BIGINT,
    serverId TEXT
)
