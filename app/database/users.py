import aiosqlite

DATABASE_PATH = "data/library.db"


async def add_user(telegram_id: int, username: str | None, full_name: str):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """
            INSERT OR IGNORE INTO users
            (telegram_id, username, full_name)
            VALUES (?, ?, ?)
            """,
            (telegram_id, username, full_name)
        )

        await db.commit()