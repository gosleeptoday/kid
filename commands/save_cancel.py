from aiogram import F, Bot, types
from aiogram.fsm.context import FSMContext
from commands import commands_router
from keyboards import actions, confirm_k
from states import UserActionState
from repository import UserRepository, RecordRepository
from config import ADMIN_IDS
from text import *

@commands_router.callback_query(F.data == "save")
async def ask_name(call: types.Message, state: FSMContext):
    await call.message.answer("Пожалуйста, введите имя ребенка:")
    await state.set_state(UserActionState.AskName)

@commands_router.message(UserActionState.AskName)
async def ask_name(message: types.Message, state: FSMContext):
    user_name = message.text
    await state.update_data(user_name=user_name)
    await message.answer("Имя сохранено. Вы хотите записаться на выбранное занятие?", reply_markup=confirm_k)

@commands_router.callback_query(F.data == "confirm")
async def save_action(call: types.CallbackQuery, state: FSMContext):
    user_id = call.from_user.id
    username = call.from_user.username
    data = await state.get_data()
    program_name = data.get("program_name", "Неизвестная программа")
    user_name = data.get("user_name", "Неизвестное имя")
    parent_name = await UserRepository.get_name(call.from_user.id)
    await call.message.answer("Спасибо за запись!\nВ ближайшее время с Вами свяжутся. Так же вы можете записаться на другие занятия.", reply_markup=actions)
    await RecordRepository.save_record(user_id, parent_name, user_name, program_name)

    for admin_id in ADMIN_IDS:
        await call.bot.send_message(
            admin_id,
            f"Пользователь @{username} (ID: {user_id}) зарегистрировался на программу: {program_name}\nИмя заказчика: {parent_name}\nИмя ребенка: {user_name}"
        )

    await state.set_state(UserActionState.Home)

@commands_router.callback_query(F.data == "cancel")
async def first(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Вы вернулись в главное меню. Вы можете посмотреть информацию или записаться на занятия:", reply_markup=actions)
    await state.set_state(UserActionState.Home)