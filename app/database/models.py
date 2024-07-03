# Welcome to the models.py file. This file is where you will define the structure of your database tables.
from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

from config import SQLALCHEMY_URI

engine = create_async_engine(SQLALCHEMY_URI, echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    chat_id = Column(Integer, primary_key=True)

    full_name = Column(String)
    username = Column(String)

    created_at = Column(DateTime, server_default="now()")
    updated_at = Column(DateTime, server_default="now()", onupdate="now()")

    is_admin = Column(Boolean, default=False)

    def __repr__(self):
        return f"<User(id={self.id}, chat_id={self.chat_id}, full_name={self.full_name}, username={self.username})>"

    def __str__(self):
        return self.full_name or self.username


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    name = Column(String, nullable=False)

    created_at = Column(DateTime, server_default="now()")
    updated_at = Column(DateTime, server_default="now()", onupdate="now()")

    products = relationship("Product", back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

    def __str__(self):
        return self.name


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)

    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)

    created_at = Column(DateTime, server_default="now()")
    updated_at = Column(DateTime, server_default="now()", onupdate="now()")

    category_id = Column(BigInteger, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"

    def __str__(self):
        return self.name


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
