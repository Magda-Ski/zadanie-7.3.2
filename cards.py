from faker import Faker
fake = Faker("pl_PL")


class Card:
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}"

    def __repr__(self):
        return f"Card(first_name={self.first_name} last_name={self.last_name}, email_address={self.address})"

    def contact(self):
        return f"Kontaktujesz sie z {self.first_name} {self.last_name} {self.address} "

    @property
    def count_letters(self):
        return sum([len(self.first_name), len(self.last_name)])


contacts = Card(first_name=fake.first_name(), last_name=fake.last_name(), address=fake.address())
print(contacts.contact())
print(contacts.count_letters)


class BusinessContact(Card):
    def __init__(self, phone_number, *args, **kwargs):
        super().__init__(*args, *kwargs)
        self.phone_number = phone_number



    def contact(self):
        return f"Kontaktujesz sie z {self.first_name} {self.last_name} pod numerem {self.phone_number} "


business = BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(),
                           address=fake.address(), phone_number=fake.phone_number())
print(business.contact())

