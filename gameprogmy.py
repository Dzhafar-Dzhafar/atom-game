#cd C:\Users\nag_b\Desktop\atom-game
#py -m pip install -U pygame --user
#pip install jedi
#Python gameprogmy.py
import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
'''Рзрешение окна 500 на 500'''
pygame.display.set_caption("New game")
'''Наименование окна игры'''
x=230
y=460
'''Расположение объекта по координатам'''
widht = 30
'''Добавляем ширину'''
height = 30
'''Добавляем высоту'''
speed = 5
'''Добавляем прыжки'''
isJump = False #Прыгает сейчас объект или нет
jumpCount = 10

'''Создаём игровой цикл true -> false -> exit'''
run = True
while run:
    pygame.time.delay(30)
    '''Временной шаг хода цикла в миллисекундах'''

    '''Теперь мы будем отслеживать события'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    '''Добавим учёт зажима кнопки с помощью списка кнопок'''
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    '''Для левого зажима <-'''

    if keys[pygame.K_RIGHT] and x < 495 - widht:
        x += speed
    '''Для правого зажима ->'''

    if not(isJump):
        if keys[pygame.K_UP] and y > 5:
            y -= speed
        '''Для зажима вверх'''

        if keys[pygame.K_DOWN] and y < 495 - height:
            y += speed
        '''Для зажима вниз'''

        if keys[pygame.K_SPACE]:
            isJump = True
        '''Проверка нажатия пробела'''
    else:
        if jumpCount >= -10: #Начали прыжок
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2 #граница до падения и падение
            else:
                y -= (jumpCount ** 2) / 2 #шаг прыжка
            jumpCount -=1 #цикл падения
        else:
            isJump = False #Закончили прыжок
            jumpCount = 10
        '''Строим параболу'''

    '''Осуществляем удаление следа объекта'''
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0,255,0), (x, y, widht, height))
    '''win поверхность на которой будем рисовать наш объект'''
    '''указываем цвет через RGB'''
    '''далее указываем координаты, высоту и ширину нашего объекта'''

    '''Прописываем обновление для отображения объекта'''
    pygame.display.update()

pygame.quit()
'''Стопаем приложение'''
