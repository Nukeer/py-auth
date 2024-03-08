import uuid

from sqlalchemy import Column, UUID, String, Boolean

from src.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(120), unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
