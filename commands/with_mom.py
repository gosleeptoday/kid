from aiogram import F, types
from aiogram.filters.command import CommandStart
from commands import commands_router
from repository import UserRepository
from aiogram.fsm.context import FSMContext
from keyboards import save_cancel_k
from states import UserActionState
from text import *

@commands_router.callback_query(UserActionState.Mom)
async def with_mom_buttons(call: types.CallbackQuery, state: FSMContext):
    program_name = ''
    match call.data:
        case "montessori":
            program_name = 'Монтессори вместе с мамой'
            await call.message.answer(ABOUT_MOONTESSORI, reply_markup=save_cancel_k)
        case "music":
            program_name = 'Музыкальные занятия Звучалки'
            await call.message.answer(ABOUT_MUSIC, reply_markup=save_cancel_k)
        case "nido":
            program_name = 'Младенческий класс NIDO'
            await call.message.answer(ABOUT_NIDO, reply_markup=save_cancel_k)

    await state.update_data(program_name=program_name)
    await state.set_state(UserActionState.Write)

    

