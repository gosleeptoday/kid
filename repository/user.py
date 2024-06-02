from datetime import datetime
from database.models import User, Record


class UserRepository(object):
    @staticmethod
    async def exists_by_id(user_id: int) -> bool:
        return await User.exists(id=user_id)

    @staticmethod
    async def exists_by_telegram_id(telegram_id: int) -> bool:
        return await User.exists(telegram_id=telegram_id)

    @staticmethod
    async def create_user(telegram_id: int, phone: str, name: str):
        if not name:
            raise ValueError("name cannot be null or empty")
        await User.create(telegram_id=telegram_id, phone=phone, name=name)

    @staticmethod
    async def user_count() -> int:
        return len(await User.all())

    @staticmethod
    async def get_all_users() -> list[User]:
        return await User.all()
    
    @staticmethod
    async def get_name(telegram_id: int) -> str:
        res = await User.get(telegram_id=telegram_id)
        return res.name

class RecordRepository(object):  
    @staticmethod
    async def save_record(user_id: int, name: str, kidname:str, society:str) -> None:
        await Record.create(user=user_id,  name=name, kidname=kidname, society=society)
