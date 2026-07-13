import aiosqlite


DATABASE_PATH = "data/library.db"


async def create_database():
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                full_name TEXT
            )
            """
        )

        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                date TEXT NOT NULL,
                time TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(id),
                UNIQUE(date, time)
            )
            """
        )

        await db.commit()


async def create_booking(
        user_id: int,
        date: str,
        time: str
) -> bool:
    try:
        async with aiosqlite.connect(DATABASE_PATH) as db:
            await db.execute(
                """
                INSERT INTO bookings
                (user_id, date, time)
                VALUES (?, ?, ?)
                """,
                (
                    user_id,
                    date,
                    time
                )
            )

            await db.commit()

        return True

    except aiosqlite.IntegrityError:
        return False


async def get_user_bookings(
        user_id: int
):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        cursor = await db.execute(
            """
            SELECT id, date, time
            FROM bookings
            WHERE user_id = ?
            ORDER BY date, time
            """,
            (user_id,)
        )

        return await cursor.fetchall()


async def cancel_booking(
        booking_id: int,
        user_id: int
):
    async with aiosqlite.connect(DATABASE_PATH) as db:
        await db.execute(
            """
            DELETE FROM bookings
            WHERE id = ?
            AND user_id = ?
            """,
            (
                booking_id,
                user_id
            )
        )

        await db.commit()