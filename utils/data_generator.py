from faker import Faker

class TestDataGenerator:
    fake = Faker('en')
    name = fake.first_name()
    surname = fake.last_name()
    password = fake.password()
    short_password = fake.password(length=6)
    incorrect_password = fake.password()



    def __init__(self):
        pass

    def generate_email_with_name_and_surname(self):
        email = f'{self.name}.{self.surname}@{self.fake.domain_name()}'
        return email




