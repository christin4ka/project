from aiogram.types import (ReplyKeyboardMarkup,ReplyKeyboardRemove,     
                            KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import UserManager

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
    all_catalogs = await UserManager.get_catalogs()
    kb_catalog = InlineKeyboardBuilder()
    for catalog in all_catalogs:
        kb_catalog.add(InlineKeyboardButton(text=catalog.name, callback_data=f'catalog_{catalog.id}'))
    kb_catalog.add(InlineKeyboardButton(text='На главное меню', callback_data='to_main'))
    return kb_catalog.adjust(2).as_markup()

async def assets(catalog_id):
    all_assets = await UserManager.get_catalog_asset(catalog_id)
    kb_catalog = InlineKeyboardBuilder()
    for asset in all_assets:
        kb_catalog.add(InlineKeyboardButton(text=asset.name, callback_data=f'asset_{asset.id}'))
    kb_catalog.add(InlineKeyboardButton(text='На главное меню', callback_data='to_main'))
    return kb_catalog.adjust(2).as_markup()

async def aboutus():
    all_about_us = await UserManager.get_about_us()
    kb_catalog = InlineKeyboardBuilder()
    for about in all_about_us:
        kb_catalog.add(InlineKeyboardButton(text=about.description, callback_data=f'aboutus_{about.description}'))
    kb_catalog.add(InlineKeyboardButton(text='На главное меню', callback_data='to_main'))
    return kb_catalog.adjust(2).as_markup()

