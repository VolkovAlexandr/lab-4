import datetime
try:
    print('Введите дату отправления в формате ДД/ММ/ГГ ЧЧ:ММ')
    date1 = datetime.datetime.strptime(input(),"%d/%m/%y %H:%M")
except ValueError:
    print('неверный формат даты')
    exit()
try:
    print('Введите дату отправления в формате ДД/ММ/ГГ ЧЧ:ММ')
    date2 = datetime.datetime.strptime(input(), "%d/%m/%y %H:%M")
except ValueError:
    print('неверный формат даты')
    exit()
print('Время в пути', date1 - date2)