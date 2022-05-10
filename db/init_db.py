import aiosqlite
import asyncio

async def init():
	async with aiosqlite.connect("url.db") as db:
		with open("db/init_db.sqlite") as f:
			await db.executescript(f.read())
		await db.commit()

asyncio.run(init())
