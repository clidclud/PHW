from data_create import *
def delete_contact():
    print("Какой контакт хотите удалить?")
    contact = search_contact()
    if contact:
        print(contact)
        data = read_file()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact + "\n\n", '')
            data2.write(data)

def change_contact():
    contact = search_contact()
    if contact:
        print(contact)
        new_contact = contact.replace('\n', ' ').split()
        print('\nВарианты замены:\n'
                '1. Имя\n'
                '2. Фамилия\n'
                '3. Отчество\n'
                '4. Номер телефона\n'
                '5. Адресу\n'
                '6. Контакт целеком\n')
        choice = input('Выберите вариант замены: ')
        print('Введите данные для замены')
        if choice != '6':
            i_choice = int(choice) - 1
            change = input('Введите изменяемую часть контакта: ')
            new_contact[i_choice] = change
            # new_contact = ''.join(new_contact[:3]) + '\n' + '\n'.join(new_contact[3:])
            new_contact = f'{new_contact[0]} {new_contact[1]} {new_contact[2]}\n{new_contact[3]}\n{new_contact[4]}'
        else:
            new_contact = input_contact()
        data = read_file()
        with open('Phonebook.txt', 'w', encoding='utf-8') as data2:
            data = data.replace(contact, new_contact)
            data2.write(data)

def input_contact():
    name = name_data()
    surname = surname_data()
    patronymic = patronymic_data()
    phone_number = phone_number_data()
    address = address_data()
    return f'{name} {surname} {patronymic}\n{phone_number}\n{address}'

def add_contact():
    contact = input_contact()
    with open('Phonebook.txt', 'a', encoding='utf-8') as data:
        data.write(contact + '\n\n')

def read_file():
    with open('Phonebook.txt', 'r', encoding='utf-8') as data:
        return data.read()

def print_contact():
    data = read_file()
    print(data)

def search_contact():
    print('\nВарианты поиска:\n'
          '1. По имени\n'
          '2. По фамилии\n'
          '3. По отчеству\n'
          '4. По номеру телефона\n'
          '5. По адресу\n')
    choice = input('Выберите вариант поиска: ')
    i_choice = int(choice) - 1
    search = input('Введите данные для поиска: ')
    data_str = read_file().rstrip()
    if search not in data_str:
        print('Такого контакта нет')
    else:
        data_lst = data_str.split('\n\n')
        for contact_str in data_lst:
            contact_lst = contact_str.replace('\n', ' ').split()
            if search in contact_lst[i_choice]:
                print(f'\n{contact_str}')
                choice_search = input('\nЭтот контакт выискали? 1 - да, 2 - нет: ')
                if choice_search == '1':
                    return contact_str
        print('Контакты закончились.')