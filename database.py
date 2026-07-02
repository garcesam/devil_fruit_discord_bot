import aiosqlite

DB_PATH = "leveling.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS user_info (
    user_id INTEGER,
    guild_id INTEGER, 
    xp INTEGER DEFAULT 0,
    UNIQUE(user_id, guild_id)
);
"""

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(SCHEMA)
        await db.commit()