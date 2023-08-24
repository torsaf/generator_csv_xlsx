import pandas as pd

print('Что нужно сделать?')
options = ['1', '2', '3']
a = None
while a not in options:
    a = input(' 1 = CSV -> XLSX \n 2 = XLSX -> CSV\n 3 = Выход\n Введи номер выбранного варианта: ')
    if a not in options:
        print('Некорректный выбор. Попробуйте еще раз.')

while a != '3':
    if a == '1':
        print('Хорошо. Сделаем CSV -> XLSX')
        name = input('Введи название файла, который нужно преобразовать: ')
        df = pd.read_csv(f'{name}.csv', sep=';', encoding='utf-8')
        writer = pd.ExcelWriter('Excel.xlsx')
        df.to_excel(writer, index=False)
        writer.save()
        print('Готово! Файл преобразован в .XLSX формат и называется Excel')
    elif a == '2':
        print('Хорошо. Сделаем XLSX -> CSV')
        name = input('Введи название файла, который нужно преобразовать: ')
        df = pd.read_excel(f'{name}.xlsx')
        df.to_csv('Text.csv', sep=';', index=False)
        print('Готово! Файл преобразован в .CSV формат и называется Text')
    a = None
    while a not in options:
        a = input(' 1 = CSV -> XLSX \n 2 = XLSX -> CSV\n 3 = Выход\n')
        if a not in options:
            print('Некорректный выбор. Попробуйте еще раз.')
            
print('Хорошо поработали!')