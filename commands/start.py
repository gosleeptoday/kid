from aiogram import F, types
from aiogram.filters.command import CommandStart
from commands import commands_router
from repository import UserRepository
from aiogram.fsm.context import FSMContext
from keyboards import start_k, actions
from states import UserActionState

@commands_router.message(CommandStart())
async def command_start_hendler(message: types.Message, state: FSMContext):
    if not await UserRepository.exists_by_telegram_id(message.from_user.id):
        await message.reply("Добро пожаловать. Для продолжения и записи на занятия предоставьте свой номер, нажав на кнопку ниже.", reply_markup=start_k)
        await state.set_state(UserActionState.Phone)
    else: 
        await message.reply("Используйте кнопки ниже для записи или получения информации", reply_markup=actions)
        await state.set_state(UserActionState.Home)

@commands_router.message(UserActionState.Phone)
async def reg_phone(message: types.Message, state: FSMContext):
    if message.contact:
        phone_number = message.contact.phone_number
        telegram_id = message.from_user.id
        await state.update_data(phone_number=phone_number, telegram_id=telegram_id)
        await message.reply("Теперь введите ваше имя.")
        await state.set_state(UserActionState.Name)
    else:
        await message.reply("Пожалуйста, используйте кнопку для отправки вашего номера телефона.")
        await state.set_state(UserActionState.Phone)

@commands_router.message(UserActionState.Name)
async def reg_name(message: types.Message, state: FSMContext):
    user_name = message.text
    data = await state.get_data()
    phone_number = data.get('phone_number')
    telegram_id = data.get('telegram_id')
    
    await UserRepository.create_user(telegram_id, phone_number, user_name)
    
    await message.reply("Вы успешно зарегистрированы!", reply_markup=actions)
    await state.set_state(UserActionState.Home)