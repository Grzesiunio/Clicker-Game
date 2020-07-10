import pygame
import time
from Items import Hotel
from Items import Motel
from Items import House

start_time = time.time()
# Initialize the pygame
pygame.init()

# Creating the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Clicker Game")
# icon = pygame.image.load('zdjecie.png')
# pygame.display.set_icon(icon)

# Gold
gold = 0

# Creating buttons
hotel_button = pygame.Rect(300, 120, 50, 50)
motel_button = pygame.Rect(300, 190, 50, 50)
house_button = pygame.Rect(300, 260, 50, 50)
# Keys
space_down = False
mouse_click_down = False

# Font
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# init classes
hotel = Hotel(0, 0)
motel = Motel(0,0)
house = House(0,0)

# Stopwatch
start = time.time()

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Pressing space to get gold
    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            space_down = True
    if space_down:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                gold = gold + 1
                space_down = False

    # hotel button
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 120:
            if pygame.mouse.get_pos()[0] <= 350 and pygame.mouse.get_pos()[1] <= 170:
                pygame.time.delay(120)
                hotel.hotel_buy(gold)
                if gold >= 20:
                    hotel.quantity += 1
                    gold -= 20
    # motel button
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 190:
            if pygame.mouse.get_pos()[0] <= 350 and pygame.mouse.get_pos()[1] <= 260:
                pygame.time.delay(120)
                motel.motel_buy(gold)
                if gold >= 1000:
                    motel.quantity += 1
                    gold -= 1000

    # House button
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 260:
            if pygame.mouse.get_pos()[0] <= 350 and pygame.mouse.get_pos()[1] <= 310:
                pygame.time.delay(120)
                house.house_buy(gold)
                if gold >= 100000:
                    house.quantity += 1
                    gold -= 100000
    # Hotel
    if int(time.time() % 30) == 1:
        pygame.time.delay(100)
        gold = gold + hotel.quantity
    # Motel
    if int(time.time() % 20) == 1:
        pygame.time.delay(90)
        gold = gold + 2*hotel.quantity
    # House
    if int(time.time() % 10) == 1:
        pygame.time.delay(80)
        gold = gold + 3*house.quantity
    # Text with gold
    textsurface = myfont.render('Your Gold: ' + str(gold), False, (0, 0, 0))
    text_hotel = myfont.render('Hotel quantity: ' + str(hotel.quantity), False, (0,0,0))
    text_motel = myfont.render('Motel quantity: ' + str(motel.quantity), False, (0,0,0))
    text_house = myfont.render('House quantity: ' + str(house.quantity), False, (0,0,0))
    text_stopwatch = myfont.render('Time: ' +str(int(time.time()-start)) +'s', False, (0,0,0))

    # Color screen
    screen.fill((0, 255, 0))
    # Button draw
    pygame.draw.rect(screen, [255, 0, 0], hotel_button)
    pygame.draw.rect(screen, [255,0, 0], motel_button)
    pygame.draw.rect(screen, [255,0, 0], house_button)
    screen.blit(textsurface, (0, 0))
    screen.blit(text_hotel, (10, 120))
    screen.blit(text_motel, (10, 190))
    screen.blit(text_house, (10, 260))
    screen.blit(text_stopwatch, (620,0))
    pygame.display.update()

# TODO:
# Najlepszy czas w jakim udalo sie ukonczyc gre
# Muzyka, sounds effect
