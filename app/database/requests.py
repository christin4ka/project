from database.models import async_session
from database.models import User, Catalog, Asset, AboutUs
from sqlalchemy import select


async def set_user(tg_id): 
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_catalogs():
    async with async_session() as session:
        result = await session.scalars(select(Catalog))
        return result.all()
        
async def get_catalog_asset(catalog_id):
    async with async_session() as session:
        result = await session.scalars(select(Asset).where(Asset.catalog_id == catalog_id))
    return result.all()

async def get_asset(asset_id):
    async with async_session() as session:
        return await session.scalar(select(Asset).where(Asset.id == asset_id))
    
async def get_about_us():
    async with async_session() as session:
        result = await session.scalar(select(AboutUs))
    return result.all()