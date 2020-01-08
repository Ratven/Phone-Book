class Contact:

    def __init__(self, name, last_name, phone, is_favourite=False, **kwargs):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.is_favourite = is_favourite
        self.attr_dict = {}
        for key, value in kwargs.items():
            self.attr_dict[key] = value

    def __str__(self):
        if self.is_favourite:
            fav = 'Да'
        else:
            fav = 'Нет'
        basic_text = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.last_name}\n'
            f'Телефон: {self.phone}\n'
            f'В избранных: {fav}\n'
        )
        if self.attr_dict:
            basic_text += 'Дополнительная информация:\n'
            for item in self.attr_dict:
                basic_text += (
                    f'    {item}: {self.attr_dict[item]}\n'
                )
        return basic_text


class PhoneBook:
    def __init__(self):
        # self.name = name
        self.contact_list = []

    def print_contacts(self):
        for contact in self.contact_list:
            print(contact)

    def add_contact(self, contact):
        if type(contact) == Contact:
            self.contact_list.append(contact)
            print('Контакт добавлен')
        else:
            print('Ошибка')

    def delete_contact(self, number):
        is_found = 0
        for contact in self.contact_list:
            if contact.phone == number:
                self.contact_list.remove(contact)
                print('Контакт удалён')
                is_found = 1
                break
        if not is_found:
            print('Контакт с таким номером телефона не найден')

    def find_favourites(self):
        list_of_contacts = []
        for contact in self.contact_list:
            if contact.is_favourite:
                list_of_contacts.append(contact)
            return contact
        if not list_of_contacts:
            return 'Избранных номеров нет'

    def find_by_name(self, name, last_name):
        is_found = 0
        for contact in self.contact_list:
            if contact.last_name.lower() == last_name.lower() and contact.name.lower() == name.lower():
                is_found = 1
                return contact
        if not is_found:
            return 'Контактов с такими именем и фамилией нет'


def do_the_command(any_book):
    command = input('Enter the command: ')
    if command.lower() == 'p':
        any_book.print_contacts()
    if command.lower() == 'a':
        cont = input('Введите контакт: ')
        any_book.add_contact(cont)
    if command.lower() == 'd':
        number = input('Введите номер телефона: ')
        any_book.delete_contact(number)
    if command.lower() == 'f':
        print(any_book.find_favourites())
    if command.lower() == 'n':
        name = input('Имя: ')
        surname = input('Фамилия: ')
        print(any_book.find_by_name(name, surname))


if __name__ == '__main__':
    phone_book = PhoneBook()
    jhon = Contact('Jhon', 'Smith', '+71234567809', is_favourite=True, telegram='@jhony', email='jhony@smith.com')
    phone_book.add_contact(jhon)
    do_the_command(phone_book)
