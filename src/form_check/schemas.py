from typing import Any, Dict
from pydantic import BaseModel

from src.form_check.validators import FieldType


class FormName(BaseModel):
    name: str


class Form(FormName):
    fields: Dict[str, Any]


class FormFields(BaseModel):
    fields: Dict[str, FieldType]