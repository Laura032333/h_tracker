# services/employees.py
from typing import List, Optional
from sqlalchemy.orm import Session

from models.employees import Employees
from schemas.employees import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, employee_in: EmployeeCreate) -> Employees:
    """
    Crea un nuevo empleado.
    """
    db_employee = Employees(**employee_in.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_employees(db: Session) -> List[Employees]:
    """
    Devuelve todos los empleados.
    """
    return db.query(Employees).all()


def get_employee(db: Session, id_employee: int) -> Optional[Employees]:
    """
    Devuelve un empleado por su ID.
    """
    return (
        db.query(Employees)
        .filter(Employees.id_employee == id_employee)
        .first()
    )


def update_employee(
    db: Session,
    id_employee: int,
    employee_in: EmployeeUpdate,
) -> Optional[Employees]:
    """
    Actualiza parcialmente un empleado.
    """
    db_employee = get_employee(db, id_employee)
    if not db_employee:
        return None

    data = employee_in.dict(exclude_unset=True)
    for field, value in data.items():
        setattr(db_employee, field, value)

    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, id_employee: int) -> bool:
    """
    Elimina un empleado por ID.
    """
    db_employee = get_employee(db, id_employee)
    if not db_employee:
        return False

    db.delete(db_employee)
    db.commit()
    return True
