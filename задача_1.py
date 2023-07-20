def print_info(temp):
    for i, contact in enumerate(temp):
        print(f'{i+1}. {contact}')

def edit_info(temp):
    index = int(input('Введите номер контакта который нужно изменить')) - 1
    new_info = input('Введите новую информацию для контакта')
    temp[index] = new_info

def delete_info(temp):
    index = int(input('Введите номер контакта который нужно удалить: ')) - 1    
    del temp[index]

def read_file():
    with open('my_file.txt', 'r', encoding='utf-8') as file:
        temp = file.readlines()
    return temp

def write_file(temp):
    with open('my_file.txt', 'w', encoding='utf-8') as file:
        file.writelines(temp)

def menu():
    data = read_file()
    while True:
        print('Выберите действие ')
        print('1 - вывести на экран')
        print('2 - Выход из программы')
        print('3 - Изменение данных')
        print('4 - Удаление данных')
        choice = int(input('ваш выбор: '))
        if choice == 1:
            print_info(data)
        elif choice == 2:
            break
        elif choice == 3:
            edit_info(data)
            write_file(data)
        elif choice == 4: 
            delete_info(data)
            write_file(data)   

if __name__ == '__main__':
    menu()            



