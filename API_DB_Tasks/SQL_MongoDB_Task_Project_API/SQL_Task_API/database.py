import os
import uuid

from sqlalchemy import UUID as PostgresUUID, Column, ForeignKey, Integer, Numeric, String, Text

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

class Project(Base):
    __tablename__ = "projects"

    id = Column(PostgresUUID(as_uuid=True), primary_key=True,default=uuid4)
    name = Column(String)
    description = Column(Text)

    tasks = relationship(
        "Task",
        back_populates="project"
    )
class Task(Base):
    __tablename__ = "tasks"

    id = Column(PostgresUUID(as_uuid=True), primary_key=True,default=uuid4)
    project_id = Column(
        PostgresUUID(as_uuid=True),
        ForeignKey("projects.id")
    )

    title = Column(String)
    description = Column(Text)

    priority = Column(String)
    status = Column(String)

    assigned_to = Column(String)

    project = relationship(
        "Project",
        back_populates="tasks"
    )

