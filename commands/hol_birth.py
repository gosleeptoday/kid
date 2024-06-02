from aiogram import F, types
from aiogram.filters.command import CommandStart
from commands import commands_router
from repository import UserRepository
from aiogram.fsm.context import FSMContext
from keyboards import save_cancel_k, birth_k
from states import UserActionState
from text import *

@commands_router.callback_query(UserActionState.HolBirth)
async def with_mom_buttons(call: types.CallbackQuery, state: FSMContext):
    program_name = ''
    match call.data:
        case "events":
            program_name = 'День рождения Королевский прием'
            await call.message.answer(ABOUT_HOL, reply_markup=save_cancel_k)
            await state.set_state(UserActionState.Write)
            await state.update_data(program_name=program_name)
        case "birthday":
            await call.message.answer("Выберите программу проведения Дня рождения:", reply_markup=birth_k)
            await state.set_state(UserActionState.Birth)

@commands_router.callback_query(UserActionState.Birth)
async def with_mom_buttons(call: types.CallbackQuery, state: FSMContext):
    program_name = ''
    match call.data:
        case "karavai":
            program_name = 'День рождения Каравай-Каравай'
            await call.message.answer(ABOUT_KARAVAI, reply_markup=save_cancel_k)
        case "priem":
            program_name = 'День рождения Королевский прием'
            await call.message.answer(ABOUT_KING, reply_markup=save_cancel_k)
    await state.set_state(UserActionState.Write)
    await state.update_data(program_name=program_name)

