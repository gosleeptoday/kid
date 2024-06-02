from aiogram import F, Bot, types
from aiogram.fsm.context import FSMContext
from commands import commands_router
from keyboards import save_cancel_k, first_actions, cancel_k, with_mom_k, holiday_k
from states import UserActionState
from text import *

@commands_router.message(UserActionState.Home)
async def user_actions_buttons(message: types.Message, state: FSMContext):
    if message.text == "📝Запись":
        await message.answer("Ниже вы можете выбрать интересующее вас занятие, нажав на кнопку.", reply_markup=types.ReplyKeyboardRemove())
        await message.reply("Какие занятия вас интересуют?", reply_markup=first_actions)
        await state.set_state(UserActionState.Select)
    else:
        await message.answer("Данный бот предназначен для удобной записи на пробные занятия в студию детских открытий «Дело в детях».\nКонтакт для связи:\nКристина Tg: @Kristina_delovdetyah Телефон: +79168103627", reply_markup=cancel_k)

@commands_router.callback_query(UserActionState.Select)
async def user_actions_buttons(call: types.CallbackQuery, state: FSMContext):
    program_name = ''
    match call.data:
        case "mini_sad":
            program_name = 'Мини сад'
            await call.message.answer(ABOUT_MINI_SAD, reply_markup=save_cancel_k)
            await state.set_state(UserActionState.Write)
            await state.update_data(program_name=program_name)
        case "full_day_sad":
            program_name = 'Сад полного дня'
            await call.message.answer(ABOUT_FULLDAY, reply_markup=save_cancel_k)
            await state.set_state(UserActionState.Write)
            await state.update_data(program_name=program_name)
        case "with_mom":
            await call.message.answer("Варианты занятий вместе с мамой:", reply_markup=with_mom_k)
            await state.set_state(UserActionState.Mom)
        case "holidays_birthday":
            await call.message.answer("Выберите Меропрития или День рождения:", reply_markup=holiday_k)
            await state.set_state(UserActionState.HolBirth)

