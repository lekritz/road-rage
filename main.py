# Setting the window on center of the screen
from pygame import display

WIDTH = 720
HEIGHT = 800
display.set_mode((WIDTH, HEIGHT))


# Importing
from pgzrun import go
from random import choice

# Variables
TITLE = "Road Rage"
mode = "menu"
CAR_IMAGES = ["blue_car", "pink_car", "red_car"]
road = Actor("road", (WIDTH - 70, HEIGHT), anchor=("right", "bottom"))
player = Actor("main_car", (WIDTH / 2, HEIGHT))
DELAY = 0.01
fuel_level = 1000
fuel_bags = [Actor("fuel_bag", (choice([WIDTH / 2 - 200, WIDTH / 2, WIDTH / 2
                                        + 200]),
                                -250))]
try:
    with open("highscore.hex", "r") as file:
        highscore = int(file.read(), base=16)
except FileNotFoundError:
    with open("highscore.hex", "w") as file:
        file.write("0")
    highscore = 0
except ValueError:
    mode = "hs corrupt"  # "hs" stands for "highscore".

score = 0

random_cars = [Actor(choice(CAR_IMAGES), (choice([WIDTH / 2 - 200, WIDTH / 2,
                                                  WIDTH / 2 + 200]), -250))]


def reset_all():
    global TITLE, mode, CAR_IMAGES, road, player, DELAY, fuel_level,\
        fuel_bags, highscore, score, random_cars, game_over
    TITLE = "Road Rage"
    mode = "menu"
    CAR_IMAGES = ["blue_car", "pink_car", "red_car"]
    road = Actor("road", (WIDTH - 70, HEIGHT), anchor=("right", "bottom"))
    player = Actor("main_car", (WIDTH / 2, HEIGHT))
    DELAY = 0.01
    fuel_level = 1000
    fuel_bags = [Actor("fuel_bag", (choice([WIDTH / 2 - 200, WIDTH / 2,
                                            WIDTH / 2 + 200]), -250))]

    with open("highscore.hex", "r") as file:
        highscore = int(file.read(), base=16)

    score = 0

    random_cars = [Actor(choice(CAR_IMAGES), (choice([WIDTH / 2 - 200,
                                                      WIDTH / 2, WIDTH
                                                      / 2 + 200]), -250))]


def draw():
    global DELAY
    if mode == "game":
        screen.fill((30, 200, 0))
        road.draw()
        player.draw()
        for car in random_cars:
            car.draw()
        for fuel_bag in fuel_bags:
            fuel_bag.draw()
        if fuel_level < 200:
            screen.draw.text(str(fuel_level/10).replace(".", ","), (70, 20),
                             fontsize=35, color="red", fontname="font")
        else:
            screen.draw.text(str(fuel_level/10).replace(".", ","), (70, 20),
                             fontsize=35, fontname="font")
    elif mode == "menu":
        screen.fill((4, 173, 238))
        player.draw()
        if player.y > WIDTH / 2:
            clock.schedule(up_one_px, DELAY)
        screen.draw.text("ROAD RAGE", center=(WIDTH / 2, 40),
                         fontsize=100, fontname="font")
        screen.draw.text("EXPLORE THE TRUE ROAD RAGE AND DRIVE YOUR CAR "
                         "AROUND THE CITY",
                         center=(WIDTH / 2, 100), fontsize=16, fontname="font")
        screen.draw.text("PRESS SPACE TO START THE GAME!",
                         center=(WIDTH / 2, 150), fontsize=35, fontname="font")
        screen.draw.text(f"HIGHSCORE: {highscore}", center=(WIDTH / 2, 200),
                         fontsize=30, fontname="font")
        DELAY += 0.01
    if mode == "game over":
        screen.fill((130, 127, 130))
        screen.draw.text("GAME OVER", center=(WIDTH / 2, HEIGHT / 2 -100),
                        fontsize=90, fontname="tiny", color="#f00000",
                        owidth=1.5, ocolor="white")
        screen.draw.text("PRESS SPACE TO CONTINUE", center=(WIDTH / 2, 400),
                         fontsize=40, fontname="font")
    if mode == "hs corrupt":
        screen.fill((0, 0, 0))
        screen.draw.text("FILE \"HIGHSCORE\" CORRUPT",
                         center=(WIDTH / 2, HEIGHT / 2 - 100),
                         fontsize=80, color="white")
        screen.draw.text("CONTACT SPECIALIST OR\nHOLD RIGHT-SHIFT+H+S+R TO"
                         " RESET.",
                         center=(WIDTH / 2, HEIGHT / 2 - 100),
                         fontsize=80, color="white")


def update():
    global fuel_level, mode, score
    if mode == "menu" and player.y < HEIGHT / 2:
        player.y = HEIGHT / 2
    elif mode == "game":
        fuel_level -= 3
        if fuel_level <= 0:
            mode = "game over"
        for bag in fuel_bags:
            for car in random_cars:
                while bag.colliderect(car):
                    bag.x = choice([WIDTH / 2 - 200, WIDTH / 2, WIDTH / 2 +
                                    200])
        update_road()
        update_random_cars()
        update_fuel_bags()
        player.y = HEIGHT / 2 + 200
        update_highscore()


def up_one_px():
    player.y -= 7


def update_road():
    road.y += 12
    if road.y >= HEIGHT + 200:
        road.y = HEIGHT


def new_random_car():
    random_cars.append(Actor(choice(CAR_IMAGES), (choice([WIDTH / 2 - 200,
                                                          WIDTH / 2, WIDTH
                                                          / 2 + 200]), -250)))


def new_fuel_bag():
    fuel_bags.append(Actor("fuel_bag", (choice([WIDTH / 2 - 200, WIDTH / 2,
                                                WIDTH / 2 + 200]), -250)))


def update_random_cars():
    global mode
    if random_cars[-1].y >= 400:
        new_random_car()
    if random_cars:
        for car in random_cars:
            car.y += 11.5
            if car.colliderect(player) or fuel_level <= 0:
                mode = "game over"
            elif car.top > HEIGHT:
                random_cars.remove(car)


def update_fuel_bags():
    global fuel_level
    if fuel_bags[-1].y >= 400:
        new_fuel_bag()
    for fuel_bag in fuel_bags:
        fuel_bag.y += 12
        if fuel_bag.colliderect(player):
            fuel_level = 500
            if len(fuel_bags) < 2:
                new_fuel_bag()
            fuel_bags.remove(fuel_bag)
        elif fuel_bag.y > HEIGHT + 250:
            fuel_bags.remove(fuel_bag)


def on_key_down(key):
    global mode
    if mode == "game":
        if key == keys.A or key == keys.LEFT:
            if player.x == WIDTH / 2 or player.x == WIDTH / 2 + 200:
                player.x -= 200
        elif key == keys.D or key == keys.RIGHT:
            if player.x == WIDTH / 2 - 200 or player.x == WIDTH / 2:
                player.x += 200
    elif mode == "menu":
        if key == keys.SPACE:
            mode = "game"
    elif mode == "game over":
        if key == keys.SPACE:
            reset_all()


def on_mouse_down(pos):
    global mode, player
    if mode == "menu":
        mode = "game"
    elif mode == "game over":
        reset_all()
    elif mode == "game":
        if 55 < pos[0] < 260 and player.x == 360:
            player.x = 160
        elif 444 < pos[0] < WIDTH - 55 and player.x == 360:
            player.x = 560
        elif 260 < pos[0] < 444:
            player.x = 360


def update_highscore():
    global score, highscore
    score += 1
    if score > highscore:
        with open("highscore.hex", "w") as self:
            self.write(hex(score)[2:])
        highscore += 1


def hard_reset_on_highscore_file() -> None:
    global highscore
    with open("highscore.hex", "w") as file:
        file.write("0")
    highscore = 0


go()
