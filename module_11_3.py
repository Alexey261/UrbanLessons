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
    inf={}
    if hasattr(obj, '__name__'):
        inf['name'] = obj.__name__
    inf['type'] = obj.__class__.__name__
    inf['module'] = obj.__class__.__module__
    inf['attributes'] = list(vars(obj).keys())
    inf['methods'] = inspect.getmembers(obj, inspect.ismethod)

    return inf

alex = Account(1,'alex1999', 'Al1999@#!', 'Alexey', 'Ivanoff', '+79998881122', 'alex1999@mail.ru')

pprint(introspection_info(alex))