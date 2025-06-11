from aiogram.types import (ReplyKeyboardMarkup,ReplyKeyboardRemove,     
                            KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_catalogs, get_asset, get_about_us

# Клавиатура
get_contact = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Для начала регистрации введите ваш номер телефона', 
                                                            request_contact = True)]],
                                    resize_keyboard= True)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Каталог')],
        [KeyboardButton(text='Имущественная единица')], 
        [KeyboardButton(text='О нас')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите пункт меню...'
)

async def catalogs():
    all_catalogs = await get_catalogs()
    kb_catalog = InlineKeyboardBuilder()
    for catalog in all_catalogs:
        kb_catalog.add(InlineKeyboardButton(text=catalog.name, callback_data=f'catalog_{catalog.id}'))
    kb_catalog.add(InlineKeyboardButton(text='На главное меню', callback_data='to_main'))
    return kb_catalog.adjust(2).as_markup()

async def assets(catalog_id):
    all_property_units = await get_asset(catalog_id)
    kb_catalog = InlineKeyboardBuilder()
    for property_unit in all_property_units:
        kb_catalog.add(InlineKeyboardButton(text=property_unit.name, callback_data=f'asset_{assets.id}'))
    kb_catalog.add(InlineKeyboardButton(text='На главное меню', callback_data='to_main'))
    return kb_catalog.adjust(2).as_markup()

async def about_us():
    all_about_us = await get_about_us()
    kb_catalog = InlineKeyboardBuilder()
    for property_unit in all_about_us:
        kb_catalog.add(InlineKeyboardButton(text=about_us.name, callback_data=f'about_us_{about_us.id}'))
    kb_catalog.add(InlineKeyboardButton(text='На главное меню', callback_data='to_main'))
    return kb_catalog.adjust(2).as_markup()

