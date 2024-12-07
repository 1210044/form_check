from tinydb import TinyDB

from src.form_check.schemas import Form


def get_forms_db():
    return TinyDB('src/data/forms.json')


def load_forms(db: TinyDB):
    forms = db.all()
    return [Form(**form) for form in forms]