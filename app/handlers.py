from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from app import keyboards as kb
import app.database.requests as rq

router = Router()

#FSM-состояния
class Registration(StatesGroup):
    contact = State()


# Обработчики
@router.message(CommandStart())
async def cmd_start(message: Message):
    await rq.UserManager.set_user(message.from_user.id)
    await message.answer('Добро пожаловать в систему управления имущественным фондом предприятия!\n'
                         'Пожалуйста, зарегистрируйтесь для продолжения\n'
                         '/registration - команда, с помощью которой вы сможете зарегистрироваться',reply_markup=kb.get_contact)

@router.message(Command('registration'))
async def registration_start(message: Message, state: FSMContext):
    await message.answer('Для регистрации введите ваш номер телефона:',reply_markup=kb.main)
    await state.set_state(Registration.contact)

@router.message(F.text & ~F.command & ~F.contact)
async def registration_text(message: Message, state: FSMContext):
    user_input = message.text.strip()
    await state.update_data(contact=user_input)

    data = await state.get_data()
    await message.answer(f'Ваши данные:\nКонтакт: {data['contact']}')
    await state.clear()

@router.message(F.contact)
async def registration_contact(message: Message, state: FSMContext):
    contact_number = message.contact.phone_number
    await state.update_data(contact=contact_number)
    
    data = await state.get_data()
    await message.answer(f"Ваши данные\nКонтакт: {data['contact']}")
    await state.clear()

@router.message(F.text =='Каталог')
async def catalog (message: Message):
    await message.answer('Выберите категорию имущества', reply_markup= await kb.catalogs())

@router.callback_query(F.data.startswith('catalog_'))
async def catalog(callback: CallbackQuery):
    catalog_id = int(callback.data.split('_')[1])
    await callback.answer(f'Вы выбрали категорию {catalog_id}')
    await callback.message.answer('Выберите имущественную единицу из каталога',
        reply_markup=await kb.assets(catalog_id))
    
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Помощь')

@router.message(Command('aboutus'))
async def about_command(message: Message):
    description = await rq.UserManager.get_about_us()
    text = "\n\n".join([
    f"{about.description}\n{about.contact_type}: {about.phone_number} / {about.email}"
    for about in description
])
    await message.answer(f'О нас:\n{text}')
