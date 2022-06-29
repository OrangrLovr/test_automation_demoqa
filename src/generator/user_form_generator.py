from random import randint as r

from src.schemas.user_form import UserForm
from faker import Faker

faker_en = Faker('En')


def generated_person():
    return UserForm(
        first_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        email=faker_en.email(),
        mobile=faker_en.random_int(min=1000000000, max=9000000000),
        date_of_birth=faker_en.date(),
        current_address=faker_en.address()
    )


def generated_file():
    path = rf"E:\IdeaProjects\test_automation_demoqa\src\upload_files\user_form{r(10, 100)}.txt"
    file = open(path, 'w')
    file.write(f'Test{r(23, 100)}')
    file.close()
    return path
