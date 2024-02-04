# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номертелефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


import csv,os
from typing import List

def clear_console():
    os.system('clear')
def copy_to_file (file,data,export_ind):
    list_contacts = []
    counter = 0
    if len(data)>0:
        for i in export_ind:
            line = data[i-1].split(', ')
            list_contacts.append({})
            list_contacts[counter]['one_name'] = line[1]
            list_contacts[counter]['two_name'] = line[0]
            list_contacts[counter]['three_name'] = line[2]
            list_contacts[counter]['phone'] = line[3]                            
            counter+=1
  

        try:
            with open(file, 'w', newline='', encoding='utf-8') as csv_file:
                    fieldnames = list_contacts[0].keys()
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerows(list_contacts)  
            print ('Файл создан успешно')
        except Exception as exc:
            print ('Возникли проблемы при сохранении:',exc)


def edit_line (data,idx,file_name):
        print ("Что будем изменять 1 - Имя, 2 - Фамилию, 3 - Отчество, 4 - телефон:")
        answer = int(input())-1
        print ('Введите новое значение')
        pars = data[idx].split(', ')
        pars[answer] = input()
        data[idx] = ', '.join(pars)+'\n'
        print (['Ошибка редактирования','изменения зафиксированы'][save_data(file_name,data)]   )

def save_data (file,data):
    try:
        if len(data)>0:
            with open(file, 'w', encoding='utf-8') as f:
                f.seek(0)
                f.writelines(data)
                f.truncate()
            return True
    except:
        return False
    


def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    print()
    print('Содержимое справочника:')
    for line in enumerate(data):
        print(line[0]+1,line[1])
    print ()

def add_data(file):
    print('Введите данные контакта:')
    one_name = input('Введите имя: ')
    two_name = input('Введите фамилию: ')
    three_name = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{one_name}, {two_name}, {three_name}, {phone}\n')

def search_data(contacts: List[str]):
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def main():
    clear_console()
    file_name = 'phone_book.txt'
    if os.path.exists(file_name):
        print ('Найден и загружен телефонный справочник')
        data = read_file(file_name)
    flag = True

    while flag:
        print('0 - выход из программы')
        print('1 - добавить запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - редактировать запись')
        print('5 - удалить запись')
        print('6 - экспорт выбранных контактов в csv файл')       
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            add_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
             data = read_file(file_name)
             show_data(data) 
             print ('Введите номер строки для редактирования:') 
             idx = int(input())-1
             edit_line(data,idx,file_name)
        elif answer == '5': 
             data = read_file(file_name)
             show_data(data) 
             print ('Введите номер строки для удаления:') 
             idx = int(input())-1
             del data[idx]
             print (['Ошибка удаления','изменения зафиксированы'][save_data(file_name,data)]   )
                               

        elif answer == '6':
            print ("введите имя файла для экспорта (без расширения)", end = ' ')
            csv_file_name = input().strip()+'.csv'
            data = read_file(file_name)
            show_data(data)
            print ('Введите номера строк для импорта через запятую: ')
            export_num = list(map(int,input().split(',')))
            if max(export_num)>len(data):
                print ('Введеный номер строки больше максимальной, продолжение невозможно.') 
            else:
                copy_to_file ( csv_file_name ,data,export_num)    


if __name__ == '__main__':
    main()