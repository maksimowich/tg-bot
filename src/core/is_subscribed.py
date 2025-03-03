from aiogram import Bot
from aiogram.enums import ChatMemberStatus
from loguru import logger

from src.core.config import app_settings


async def is_subscribed(
        bot: Bot,
        user_id: int,
) -> bool:
    try:
        chat_member = await bot.get_chat_member(
            chat_id=app_settings.tg.channel_id,
            user_id=user_id,
        )
        logger.info(chat_member)
        logger.info(chat_member.status)
        return chat_member.status in [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.CREATOR,
        ]
    except Exception as e:
        logger.info(str(e))
        return False
