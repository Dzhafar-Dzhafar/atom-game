#cd C:\Users\nag_b\Desktop\atom-game
#py -m pip install -U pygame --user
#pip install jedi
#Python gameprogmy.py
import pygame

pygame.init()
win = pygame.display.set_mode((608, 492))
'''Рзрешение окна 608 на 492'''
pygame.display.set_caption("New game")
'''Наименование окна игры'''

'''Расписываем спрайты'''
walkRight = [pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'), pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'),
pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'), pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'),
pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'), pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png')]
'''Движение вправо, walkRight = [pygame.image.load('\png'), pygame.image.load('\png')..]'''
walkLeft = [pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'), pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'),
pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'), pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'),
pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png'), pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png')]
'''Движение влево walkLeft = [pygame.image.load('\png'), pygame.image.load('\png')..]'''
playerStand = pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-cat.png')
''''''
BF = pygame.image.load(r'C:\Users\nag_b\Desktop\atom-game\sprites\pixil-black.jpg')
'''Задний фон'''

clock = pygame.time.Clock()

x=300
y=460
'''Расположение объекта по координатам'''
widht = 31
'''Добавляем ширину'''
height = 30
'''Добавляем высоту'''
speed = 5
'''Добавляем прыжки'''
isJump = False #Прыгает сейчас объект или нет
jumpCount = 10
'''Создадим переменные для перемещения спрайта'''
left = False
right = False
animCaunt = 0
lastMove = 'right' #Изначально двигался на право
class projectile ():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
#Рисуем снаряд
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

def drawWindow():
    global animCaunt
    win.blit(BF, (0, 0)) #fill((0, 0, 0)) Задний фон пишем до введения объекта
    '''Осуществляем удаление следа объекта'''

    '''Добавим проверки'''
    '''ставим ограничение по выходу из списка спрайтов, 30 фрэймов в секунду'''
    if animCaunt + 1 >= 30: #если 6 спрайтов по 5 кадров в сек = 30
        animCaunt = 0

    if left:
        win.blit(walkLeft[animCaunt // 5], (x, y))
        animCaunt += 1
    elif right:
        win.blit(walkRight[animCaunt // 5], (x, y))
        animCaunt += 1
        '''Деление на 5 и округление до меньшего'''
        '''Если объект не двигается ни влево, ни вправо то: '''
    else:
        win.blit(playerStand, (x, y))

    for bullet in bullets:
        bullet.draw(win)

    #pygame.draw.rect(win, (0,255,0), (x, y, widht, height))
    '''win поверхность на которой будем рисовать наш объект'''
    '''указываем цвет через RGB'''
    '''далее указываем координаты, высоту и ширину нашего объекта'''

    '''Прописываем обновление для отображения объекта'''
    pygame.display.update()

'''Создаём игровой цикл true -> false -> exit'''
run = True
bullets = []
while run:
    clock.tick(30)
    '''Временной шаг хода цикла в миллисекундах'''

    '''Теперь мы будем отслеживать события'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 600 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet)) #Удаляем из списка bullets определённый снаряд

    '''Добавим учёт зажима кнопки с помощью списка кнопок'''
    keys = pygame.key.get_pressed()

    #Создаём кнопку снаряда
    if keys[pygame.K_f]:
        #Отслеживаем поворот персонажа для корректировки стороны полёта снаряда
        if lastMove == 'right':
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(projectile(round(x + widht // 2), (y + height // 2), 5, (255, 0, 0), facing)) #Снаряд выпускается по центру игрока + параметры

    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
        left = True
        right = False
        lastMove = 'left'
        '''Для левого зажима <-'''
    elif keys[pygame.K_RIGHT] and x < 600 - widht:
        x += speed
        left = False
        right = True
        lastMove = 'right'
        '''Для правого зажима ->'''
    else:
        left = False
        right = False
        animCaunt = 0

    if not(isJump):
        '''if keys[pygame.K_UP] and y > 5:
            y -= speed
        """Для зажима вверх"""

        if keys[pygame.K_DOWN] and y < 495 - height:
            y += speed
        """Для зажима вниз"""
        '''
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
    drawWindow()
pygame.quit()
'''Стопаем приложение'''
