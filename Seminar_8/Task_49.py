# Задача №49. 
# Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

def ask_data():
    s_name = input('Введите фамилию: ')
    f_name = input('Введите имя: ')
    m_name = input('Введите отчество: ')
    number = input('Введите номер телефона: ')
    contact = {'second_name': s_name,
               'first_name': f_name,
               'middle_name': m_name,
               'phone_number': number} 
    print("Контакт добавлен.")           
    return contact

def add_new_contact():
    contact = ask_data()
    with open('phonebook.txt', 'a', encoding='utf-8') as file:
        for value in contact.values():
            file.write(value + "; ")
        print('\n')

def open_phonbook():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        file = file.read().split('\n')
        print('       ---   Телефонная книга   ---       ')
        for n, contact in enumerate(file, 1):
            print(n, contact)
        
def find_contact():
    print("Найти по: \n 1 Фамилия \n 2 Имя \n 3 Отчество \n 4 Телефон")
    list_menu = '1, 2, 3, 4'
    finde = input(">")
    if finde == '1': 
        s_name = input("Введите фамилию: ")
    if finde == '2': 
        s_name = input("Введите имя: ")
    if finde == '3': 
        s_name = input("Введите отчество: ")
    if finde == '4': 
        s_name = input("Введите телефон: ")
    elif finde not in list_menu :
        print('Ошибка ввода!' '\n' )
        return find_contact()

    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        print("Результат поиска: ")
        for line in file:
            line = line.split()
            if s_name in line[3]:
                print('\t'.join(line))
            if s_name in line[2]: 
                print('\t'.join(line)) 
        else:
            print("Контакт не найден.")  

# def del_contact():
#     with open('phonebook.txt', 'r', encoding='utf-8') as file:
#         file = file.read().split('\n')
#         open_phonbook()
#         number_contact = int(input("Введите номер контакта который хотите копировать: "))
#         for number, contact in enumerate(file, 1):
#             if number == number_contact:
#                 print(number_contact)
#                 with open('phonebook_copy.txt', 'a', encoding='utf-8') as file:

                

def copy_contact():
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        file = file.read().split('\n')
        open_phonbook()
        number_contact = int(input("Введите номер контакта который хотите копировать: "))
        for number, contact in enumerate(file, 1):
            if number == number_contact:
                print(number_contact)
                with open('phonebook_copy.txt', 'a', encoding='utf-8') as file:
                    file.write(f"{contact} \n")

def exit_menu():
    y = 'y'
    n = 'n'
    lock = input("Вы хотите выйти из телефонного справочника? y / да, n / нет" '\n')
    if lock == y:
        return None
    if lock == n:    
        main()
    elif lock != y and lock != n:
        print('Ошибка ввода!' '\n' )
        return exit_menu()
    
def main():
    isStop = 10
    while isStop != 0:
        print("   --- МЕНЮ ---   " '\n' "Выберите пункт меню: \n 1 Найти контакт \n 2 Добавить контакт \n 3 Открыть все контакты \n 4 Удалить контакт \n 5 Копировать контакт \n 0 Выход")
        isStop = int(input(">"))
        if isStop == 1: 
            find_contact()
            input("Нажмите Enter, чтобы продолжить. ")
        if isStop == 2: 
            add_new_contact()
            input("Нажмите Enter, чтобы продолжить. ")
        if isStop == 3: 
            open_phonbook()
            input("Нажмите Enter, чтобы продолжить. ")
        # if isStop == 4: 
        #     del_contact()
        #     input("Нажмите Enter, чтобы продолжить. ")
        if isStop == 5: 
            copy_contact()
            input("Нажмите Enter, чтобы продолжить. ")
            
        if isStop == 0: 
            exit_menu() 
        
main()   
