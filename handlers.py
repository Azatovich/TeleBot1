

from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer("Привет! Я помогу узать твое ID, достаточно любого сообщения!")

@router.message()
async def massage_handler(msg: Message):
    await msg.answer(f"Твой ID:{msg.from_user.id}")
