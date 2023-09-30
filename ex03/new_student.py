import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id() -> str"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """Student class"""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """called after class instantiated"""
        self.login = self.name[0] + self.surname.lower()
        self.id = generate_id()
