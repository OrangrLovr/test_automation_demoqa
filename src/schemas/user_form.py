from dataclasses import dataclass


@dataclass
class UserForm:
    first_name: str = None
    last_name: str = None
    email: str = None
    mobile: str = None
    date_of_birth: int = None
    current_address: str = None
