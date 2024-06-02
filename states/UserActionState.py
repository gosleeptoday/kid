from aiogram.fsm.state import State, StatesGroup


class UserActionState(StatesGroup):
    Phone = State()  
    Home = State()
    Select = State()
    Mom = State()
    HolBirth = State()
    Birth = State()
    Write = State()
    AskName = State()
    Name =  State()