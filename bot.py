import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage

from tg_bot.config import load_config
from tg_bot.models.db_model import DBInteraction, Base

# from tg_bot.handlers.admin import register_admin
# from tg_bot.handlers.user import register_user


logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")
    config = load_config("bot.ini")

    if config.tg_bot.use_redis:
        storage = RedisStorage()
    else:
        storage = MemoryStorage()

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=storage)

    sqlalchemy_database_uri = f'postgresql://{config.db.user}:{config.db.password}@{config.db.host}/{config.db.db_name}'
    db_interaction = DBInteraction(sqlalchemy_url=sqlalchemy_database_uri, base=Base)

    bot["db"] = db_interaction
    # dp.filters_factory.bind(AdminFilter)

    # register_admin(dp)
    # register_user(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")