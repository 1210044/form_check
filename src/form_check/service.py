from typing import Any, Dict

from src.db import TinyDB, load_forms


def find_matching_form(db: TinyDB, fields: Dict[str, Any]) -> str:
    forms = load_forms(db)
    for form in forms:
        if form.fields.keys() <= fields.keys():
            if all(form.fields[key] == fields[key] for key in form.fields.keys()):
                return form.name
    return None