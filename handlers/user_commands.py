from aiogram import Router,types
from aiogram.filters import CommandStart


from aiogram.fsm.context import FSMContext


router = Router()



@router.message(CommandStart())
async def start(message:types.Message, state: FSMContext):
    await state.clear()
    await message.reply('Hello')