import inspect
from pprint import pprint
from dataclasses import dataclass


@dataclass
class Account:
    id: int
    login: str
    password: str
    first_name: str
    last_name: str
    phone_number: str
    email: str
    is_admin: bool = False


def introspection_info(obj):
    inf = {}
    if hasattr(obj, '__name__'):
        inf['name'] = obj.__name__
    inf['type'] = obj.__class__.__name__
    inf['module'] = obj.__class__.__module__
    if hasattr(obj, '__dict__'):
        inf['attributes'] = list(vars(obj).keys())
    else:
        attributes = inspect.getmembers(obj, lambda a: not (inspect.isroutine(a)))
        inf['attributes'] = [a for a in attributes if not (a[0].startswith("__") and a[0].endswith("__"))]

    inf['methods'] = inspect.getmembers(obj, inspect.ismethod)

    return inf


alex = Account(1, 'alex1999', 'Al1999@#!', 'Alexey', 'Ivanoff', '+79998881122', 'alex1999@mail.ru')

pprint(introspection_info(alex))
