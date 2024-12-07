from typing import Any, Callable, Dict, List, Union
from re import match
from enum import StrEnum
from datetime import datetime
from email_validator import validate_email, EmailNotValidError


class FieldType(StrEnum):
    DATE = 'date'
    PHONE = 'phone'
    EMAIL = 'email'
    TEXT = 'text'


def validate_date(value: str) -> Union[str, None]:
    date_formats = ('%d.%m.%Y', '%Y-%m-%d')
    for date_format in date_formats:
        try:
            datetime.strptime(value, date_format)
            return FieldType.DATE
        except ValueError:
            continue


def validate_phone(value: str) -> Union[str, None]:
        if match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
            return FieldType.PHONE


def validate_email_adress(value: str) -> Union[str, None]:
    try:
        validate_email(value)
        return FieldType.EMAIL
    except EmailNotValidError as e:
        return None


class Validator:
    def __init__(self):
        self._validators: List[Callable] = []

    def add_validator(self, validator: Callable):
        self._validators.append(validator)

    def validate_fields(self, fields: Dict[str, Any]) -> Dict[str, Any]:
        validated_fields = {}
        for f_name, f_value in fields.items():
            for validator in self._validators:
                f_type = validator(f_value)
                if f_type:
                    validated_fields[f_name] = f_type
                    break
            else:
                validated_fields[f_name] = FieldType.TEXT
        return validated_fields


validator = Validator()
validator.add_validator(validate_date)
validator.add_validator(validate_phone)
validator.add_validator(validate_email_adress)