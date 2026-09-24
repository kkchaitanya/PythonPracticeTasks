import os
import uuid

from sqlalchemy import UUID as PostgresUUID, Column, ForeignKey, Integer, Numeric, String

from config import settings
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base, relationship,selectinload
# ---------------------------------------------------------
# DATABASE CONFIGURATION & CONNECTION
# ---------------------------------------------------------
DATABASE_URL = settings.ASYNC_DATABASE_URL

engine = create_async_engine(DATABASE_URL, echo=True, future=True)
# async_sessionmaker is the standard async factory in SQLAlchemy 2.0+
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

# Dependency to yield database sessions to API routes
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
def uuid4():
    """Generate a random UUID."""
    return uuid.UUID(bytes=os.urandom(16), version=4)

class User(Base):
    __tablename__ = "users"

    id = Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String)
    email = Column(String, unique=True)

    orders = relationship(
        "Order",
        back_populates="user"
    )

class Product(Base):
    __tablename__ = "products"

    id =  Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid4)

    name = Column(String)
    price = Column(Numeric)

    inventory_count = Column(Integer)

    order_items = relationship(
        "OrderItem",
        back_populates="product"
    )

class Order(Base):
    __tablename__ = "orders"

    id =  Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid4)

    user_id = Column(PostgresUUID,
                     ForeignKey("users.id"))

    total_amount = Column(Numeric)

    status = Column(String)

    user = relationship(
        "User",
        back_populates="orders"
    )

    items = relationship(
        "OrderItem",
        back_populates="order"
    )

class OrderItem(Base):
    __tablename__ = "order_items"

    id =  Column(PostgresUUID(as_uuid=True), primary_key=True, default=uuid4)

    order_id = Column(
        PostgresUUID,
        ForeignKey("orders.id")
    )

    product_id = Column(
        PostgresUUID,
        ForeignKey("products.id")
    )

    quantity = Column(Integer)

    unit_price = Column(Numeric)

    item_total = Column(Numeric)

    order = relationship(
        "Order",
        back_populates="items"
    )

    product = relationship(
        "Product",
        back_populates="order_items"
    )