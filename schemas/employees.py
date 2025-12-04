# schemas/employees.py
from pydantic import BaseModel, EmailStr
from typing import Optional


class EmployeeBase(BaseModel):
    employee_name: str
    employee_email: EmailStr
    home_state: Optional[str] = None
    home_country: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    # Si quisieras permitir setear el id manualmente, podrías agregarlo aquí como opcional,
    # pero lo normal es que lo genere la BD.
    pass


class EmployeeUpdate(BaseModel):
    employee_name: Optional[str] = None
    employee_email: Optional[EmailStr] = None
    home_state: Optional[str] = None
    home_country: Optional[str] = None


class EmployeeOut(EmployeeBase):
    id_employee: int

    class Config:
        from_attributes = True  # Pydantic v2 (equivale a orm_mode=True en v1)
