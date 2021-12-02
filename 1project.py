#НУЖНЫЕ БИБЛИОТЕКИ
###############################################################################
from datetime import *
from tkinter import *
from tkinter import messagebox

#ФУНКЦИЯ ДЛЯ ВЫВОДА ИНФОРМАЦИИ
###############################################################################
def show_info():
    
    #ИНФОРМАЦИЯ РАЗБИВАЕТСЯ ПО МАССИВАМ
    ###############################################################################
    info = name_field.get()
    info_mass = info.split(' ')
    birth_date = birthdate_field.get().split('.')
    
    #ФИО И ДАТА РОЖДЕНИЯ РАЗБИВАЕТСЯ ПО ПЕРЕМЕННЫМ
    ###############################################################################
    second_name = info_mass[0].lower().capitalize()
    
    name = info_mass[1]
    name = name[0].upper()
    
    third_name = info_mass[2]
    third_name = third_name[0].upper()
    
    birth_day = int(birth_date[0])
    birth_month = int(birth_date[1])
    birth_year = int(birth_date[2])
    
    #АКТУАЛЬНАЯ ДАТА
    ###############################################################################
    day = datetime.now().day
    month = datetime.now().month
    year = datetime.now().year
    
    #ВЫЧИСЛЕНИЕ ВОЗРАСТА
    ###############################################################################
    age = year - birth_year
    
    if month > birth_month:
        age = age
    elif month == birth_month:
        if day >= birth_day:
            age = age
        else:
            age = age-1
    else:
        age = age-1
    
    #ОСНОВНАЯ ИНФОРМАЦИЯ О ПОЛЬЗОВАТЕЛЕ
    ###############################################################################
    info = 'Здравствуйте '+second_name+' '+name+'. '+third_name+'. на данный момент вам '+str(age)+' лет. '
    
    #В КАКОМ ВОЗРАСТЕ НУЖНО ПОЛУЧАТЬ ПАСПОРТ
    ###############################################################################
    pass1 = 14
    pass2 = 20
    pass3 = 45
    
    #ОСНОВНОЙ АЛГОРИТМ
    ###############################################################################
    answ = str()
    if age < pass1:
        dif = pass1-age
        
        time1 = date(year+int(dif), birth_month, birth_day)
        time2 = date(year, month, day)
        
        days = str(time1 - time2)
        days = days.split()[0]
        answ = 'Через '+str(days)+' дня(ей) Вам необходимо будет обратиться в ближайший МФЦ для получения паспорта.'
    elif age == pass1:
        answ = 'Вам необходимо обратиться в ближайший МФЦ для получения паспорта.'
    else:
        if age < pass2:
            dif = pass2-age
            
            time1 = date(year+int(dif), birth_month, birth_day)
            time2 = date(year, month, day)
            
            days = str(time1 - time2)
            days = days.split()[0]
            answ = 'Через '+str(days)+' дня(ей) Вам необходимо будет обратиться в ближайший МФЦ для замены паспорта.'
        elif age == pass2:
            answ = 'Вам необходимо обратиться в ближайший МФЦ для замены паспорта.'
        else:
            if age < pass3:
                dif = pass3-age
                
                time1 = date(year+int(dif), birth_month, birth_day)
                time2 = date(year, month, day)
                
                days = str(time1 - time2)
                days = days.split()[0]
                answ = 'Через '+str(days)+' дня(ей) Вам необходимо будет обратиться в ближайший МФЦ для замены паспорта.'
            elif age == pass3:
                answ = 'Вам необходимо обратиться в ближайший МФЦ для замены паспорта.'
            else:
                answ = 'После 45 лет замена паспорта не является необходимостью!'
    
    #ВЫВОД
    ###############################################################################
    if age > pass3:
        add_info = 'Однако если Вы в этом заинтересованы, обратитесь в ближайший МФЦ для замены паспорта.'
    else:
        add_info = 'Если Вы не получите паспорт в течении 90 дней, на Вас будет наложен штраф!'
    
    messagebox.showinfo('Рекомендация', info+'\n\n'+answ+'\n\n'+add_info)

#СПРАВКА
###############################################################################
def info():
    messagebox.showinfo('Справка', 'ИНСТРУКЦИЯ\n\nВ поле "ФИО" введите свою фамилию, имя и отчество, регистр не важен.\n\nВ поле "Дата рождения" введите свою дату рождения в формате (ДД.ММ.ГГГГ), в противном случае программа не запустится.\n\n@Костин Андрей')

#ИНТЕРФЕЙС
###############################################################################
root = Tk()
root.title("Приложение МФЦ")
root.configure(background = '#FFE4C4')
root.geometry("300x135")

label1 = Label(root, text = '         ФИО         ',bg = "#DEB887")
label1.grid(row = 0, column = 0, padx = 5)

name_field = Entry(root, font = "lucida 10")
name_field.grid(row = 0, column = 1, pady = 8)

label2 = Label(root, text = "Дата рождения", bg = '#DEB887')
label2.grid(row = 1, column = 0, padx = 5)

birthdate_field = Entry(root, font = "lucida 10")
birthdate_field.grid(row = 1, column = 1)

button = Button(root,text = "Ввод",bg = "#DEB887",command = show_info)
button.grid(row = 2, column = 1, pady = 8)

button_q = Button(root,text = "Справка",bg = "light blue",command = info)
button_q.grid(row = 3, column = 0, sticky = W, padx = 5)

root.mainloop()