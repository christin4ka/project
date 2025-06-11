from sqlalchemy import BigInteger, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

# Настройка БД
engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

# Модели
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)

class Catalog(Base):
    __tablename__ = 'catalogs'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(25))

class Asset(Base):
    __tablename__ = 'assets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(25))
    description:Mapped[str] = mapped_column(String(120))
    inventory_number:Mapped[int] = mapped_column()
    quantity:Mapped[int] = mapped_column()
    
    catalog_id:Mapped[int] = mapped_column(ForeignKey('catalogs.id'))
    catalog: Mapped[Catalog] = relationship('Catalog')

class AboutUs (Base):
    __tablename__ = 'about_us'
    id: Mapped[int] = mapped_column(primary_key=True)
    description:Mapped[str] = mapped_column(String(120))
    contact_type: Mapped[str] = mapped_column(String(20))
    phone_number:Mapped[int] = mapped_column()
    email:Mapped[int] = mapped_column()

# Создание таблиц
async def async_main():
   async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all(bind=engine))