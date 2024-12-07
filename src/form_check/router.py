from typing import Union
from fastapi import APIRouter, Request, Depends
from tinydb import TinyDB

from src.form_check.schemas import FormName, FormFields
from src.db import get_forms_db
from src.form_check.validators import validator
from src.form_check.service import find_matching_form


router = APIRouter()


@router.post("/get_form", response_model=Union[FormName, FormFields])
async def get_form(request: Request, db: TinyDB = Depends(get_forms_db)):
    form_fields = dict(request.query_params)
    validated_fields = validator.validate_fields(form_fields)
    form_name = find_matching_form(db, validated_fields)

    if form_name:
        return FormName(name=form_name)
    return FormFields(fields=validated_fields)