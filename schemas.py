from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

# ---------- Users ----------
class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    pass


class UserRegister(UserBase):
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)


class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ---------- Projects ----------
class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectOut(ProjectBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# ---------- Tasks ----------
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: str = "todo"
    priority: str = "medium"
    user_id: Optional[int] = None
    project_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskOut(TaskBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    user_id: Optional[int] = None
    project_id: Optional[int] = None