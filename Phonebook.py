# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, номер телефона, описание - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# 5. Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

def work_with_phonebook():
    phone_book = read_txt('phonebook.txt')
    choice = show_menu()
    while (choice != 8):
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Фамилия ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            number = input('Телефон ')
            print(find_by_number(phone_book,number))
        elif choice == 4:
            identifier = input('Введите Фамилию или номер Телефона абонента: ')
            field_to_change = input('Введите поле для изменения (Фамилия, Имя, Телефон, Описание): ')
            new_value = input('Введите новое значение для поля: ')
            print(change_field(phone_book, identifier, field_to_change, new_value))
        elif choice == 5:
            user_data = input('Ведите данные пользователя через запятую (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 6:
            lastname = input('Фамилия ')
            print(delete_by_lastname(phone_book, lastname))
        elif choice == 7:
            finish_work()
            break
        choice = show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить данные абонента\n"
          "5. Добавить абонента в справочник\n"
          "6. Удалить абонента из справочника\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

# Функция для чтения текстового файла
def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

# Функция для печати результата (телефонная книга)
def print_result(phone_book, fields=None):
    if fields is None:
        fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    max_widths = {field: max(len(record[field]) for record in phone_book) for field in fields}
    header_str = ' | '.join(f'{field:<{max_widths[field]}}' for field in fields)
    print(header_str)
    print('-' * len(header_str))
    for record in phone_book:
        record_str = ' | '.join(f'{record[field]:<{(max_widths[field] + 2)}}' for field in fields)
        print(record_str)

# Функция для поиска по фамилии
def find_by_lastname(phone_book, last_name):
    result = []
    for record in phone_book:
        if last_name.lower() in record['Фамилия'].lower():
            result.append(record)
    return result

# Функция для поиска по номеру телефона
def find_by_number(phone_book, number):
    result = []
    for record in phone_book:
        if number in record['Телефон']:
            result.append(record)
    return result

# Функция для изменения любого поля абонента
def change_field(phone_book, identifier, field_to_change, new_value):
    for record in phone_book:
        if record['Фамилия'].lower() == identifier.lower() or record['Телефон'] == identifier:
            if field_to_change in record:
                record[field_to_change] = new_value
                write_txt('phonebook.txt', phone_book)
                return "Поле обновлено"
            else:
                return "Такого поля не существует"
    return "Запись не найдена"

# Функция для добавления нового абонента
def add_user(phone_book, user_data):
    new_record = dict(zip(['Фамилия', 'Имя', 'Телефон', 'Описание'], user_data.split(',')))
    if new_record not in phone_book:
        phone_book.append(new_record)
        write_txt('phonebook.txt', phone_book)
        print('Новый абонент добавлен')
    else:
        print('Такая запись уже существует')

# Функция для запиcи телефонной книги
def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

# Функция для удаления абонента по фамилии
def delete_by_lastname(phone_book, last_name):
    initial_len = len(phone_book)
    phone_book[:] = [record for record in phone_book if last_name.lower() != record['Фамилия'].lower()]
    if len(phone_book) < initial_len:
        write_txt('phonebook.txt', phone_book)
        return "Абонент удален"
    return "Абонент не найден"

# Функция завершения работы с программой
def finish_work():
    print("Работа завершена")

work_with_phonebook()